import sqlite3


def is_registered_user(
    connection: sqlite3.Connection,
    user_id: int,
) -> bool:
    row = connection.execute(
        """
        SELECT 1
        FROM users
        WHERE discord_user_id = ?
        """,
        (str(user_id),),
    ).fetchone()
    return row is not None


def is_user_in_guild(
    connection: sqlite3.Connection,
    user_id: int,
    guild_name: str,
) -> bool:
    row = connection.execute(
        """
        SELECT 1
        FROM users
        JOIN user_guilds ON user_guilds.user_id = users.id
        JOIN guilds ON guilds.id = user_guilds.guild_id
        WHERE users.discord_user_id = ?
          AND guilds.name = ?
        """,
        (str(user_id), guild_name),
    ).fetchone()
    return row is not None


def get_command_requirement(
    connection: sqlite3.Connection,
    command_name: str,
) -> sqlite3.Row | None:
    return connection.execute(  # type: ignore[no-any-return]
        """
        SELECT
            command_requirements.command_name,
            command_requirements.required_level,
            guilds.name AS required_guild_name,
            guilds.display_name AS required_guild_display_name
        FROM command_requirements
        LEFT JOIN guilds
            ON guilds.id = command_requirements.required_guild_id
        WHERE command_requirements.command_name = ?
        """,
        (command_name,),
    ).fetchone()


def get_user_guilds(
    connection: sqlite3.Connection,
    user_id: int,
) -> list[sqlite3.Row]:
    rows = connection.execute(
        """
        SELECT guilds.name, guilds.display_name, user_guilds.joined_at
        FROM users
        JOIN user_guilds ON user_guilds.user_id = users.id
        JOIN guilds ON guilds.id = user_guilds.guild_id
        WHERE users.discord_user_id = ?
        ORDER BY guilds.name
        """,
        (str(user_id),),
    ).fetchall()
    return list(rows)


def list_guilds(connection: sqlite3.Connection) -> list[sqlite3.Row]:
    rows = connection.execute(
        """
        SELECT name, display_name
        FROM guilds
        ORDER BY name
        """
    ).fetchall()
    return list(rows)


def get_guild_by_name(
    connection: sqlite3.Connection,
    guild_name: str,
) -> sqlite3.Row | None:
    return connection.execute(  # type: ignore[no-any-return]
        """
        SELECT id, name, display_name
        FROM guilds
        WHERE name = ?
        """,
        (guild_name,),
    ).fetchone()


def join_user_guild(
    connection: sqlite3.Connection,
    user_id: int,
    guild_name: str,
) -> bool:
    user = connection.execute(
        """
        SELECT id
        FROM users
        WHERE discord_user_id = ?
        """,
        (str(user_id),),
    ).fetchone()
    guild = get_guild_by_name(connection, guild_name)
    if user is None or guild is None:
        return False

    cursor = connection.execute(
        """
        INSERT OR IGNORE INTO user_guilds (user_id, guild_id)
        VALUES (?, ?)
        """,
        (int(user["id"]), int(guild["id"])),
    )
    connection.commit()
    return cursor.rowcount > 0


def leave_user_guild(
    connection: sqlite3.Connection,
    user_id: int,
    guild_name: str,
) -> bool:
    cursor = connection.execute(
        """
        DELETE FROM user_guilds
        WHERE user_id = (
            SELECT id
            FROM users
            WHERE discord_user_id = ?
        )
          AND guild_id = (
            SELECT id
            FROM guilds
            WHERE name = ?
        )
        """,
        (str(user_id), guild_name),
    )
    connection.commit()
    return cursor.rowcount > 0


def check_command_access(
    connection: sqlite3.Connection,
    user_id: int,
    command_name: str,
) -> tuple[bool, str | None]:
    user = connection.execute(
        """
        SELECT id, level
        FROM users
        WHERE discord_user_id = ?
        """,
        (str(user_id),),
    ).fetchone()
    if user is None:
        return False, "You are not registered yet. Use /register first."

    requirement = get_command_requirement(connection, command_name)
    if requirement is None:
        return True, None

    required_level = int(requirement["required_level"])
    current_level = int(user["level"])
    if current_level < required_level:
        return (
            False,
            f"This command requires level {required_level}. "
            f"Your current level is {current_level}.",
        )

    required_guild_name = requirement["required_guild_name"]
    if required_guild_name is not None and not is_user_in_guild(
        connection,
        user_id,
        str(required_guild_name),
    ):
        display_name = requirement["required_guild_display_name"]
        return (
            False,
            f"This command requires membership in {display_name}.",
        )

    return True, None
