import sqlite3


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_user_id TEXT UNIQUE NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    exp INTEGER NOT NULL DEFAULT 0,
    stamina INTEGER NOT NULL DEFAULT 100,
    affection INTEGER NOT NULL DEFAULT 0,
    mood TEXT NOT NULL DEFAULT 'normal',
    auto_daily_enabled INTEGER NOT NULL DEFAULT 0,
    last_login_date TEXT,
    neko_streak INTEGER NOT NULL DEFAULT 0,
    last_neko_date TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ft_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    ft_user_id TEXT UNIQUE NOT NULL,
    ft_login TEXT NOT NULL,
    access_token TEXT NOT NULL,
    refresh_token TEXT NOT NULL,
    token_expires_at TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS daily_claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    claim_date TEXT NOT NULL,
    source TEXT NOT NULL,
    exp_gained INTEGER NOT NULL DEFAULT 10,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, claim_date)
);

CREATE TABLE IF NOT EXISTS neko_claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    claimed_date TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, claimed_date)
);

CREATE TABLE IF NOT EXISTS ft_location_rewards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    ft_location_id TEXT NOT NULL,
    ft_login TEXT NOT NULL,
    host TEXT,
    begin_at TEXT NOT NULL,
    exp_gained INTEGER NOT NULL DEFAULT 10,
    notified_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, ft_location_id)
);

CREATE TABLE IF NOT EXISTS achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    hidden INTEGER NOT NULL DEFAULT 0,
    reward_exp INTEGER NOT NULL DEFAULT 0,
    reward_affection INTEGER NOT NULL DEFAULT 0,
    reward_stamina INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    achievement_id INTEGER NOT NULL,
    unlocked_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    UNIQUE (user_id, achievement_id)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task_name TEXT NOT NULL,
    completed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE (user_id, task_name)
);
"""


INITIAL_ACHIEVEMENTS = (
    (
        "first_register",
        "First Registration",
        "Linked your first registration flow.",
        0,
        0,
        5,
        0,
    ),
    (
        "first_daily",
        "First Daily",
        "Claimed your first 42 login daily reward.",
        0,
        10,
        3,
        0,
    ),
    (
        "daily_3_streak",
        "Three Day Streak",
        "Claimed 42 login daily rewards for 3 days in a row.",
        0,
        30,
        5,
        0,
    ),
    (
        "daily_7_streak",
        "One Week Streak",
        "Claimed 42 login daily rewards for 7 days in a row.",
        0,
        70,
        10,
        0,
    ),
    (
        "level_5",
        "Rising Apprentice",
        "Reached level 5.",
        0,
        50,
        0,
        0,
    ),
    (
        "level_10",
        "Trusted Partner",
        "Reached level 10.",
        0,
        100,
        0,
        0,
    ),
    (
        "neko_7_days",
        "Chosen by Neko",
        "Ran /neko for 7 consecutive days.",
        1,
        0,
        0,
        0,
    ),
)


def _column_names(connection: sqlite3.Connection, table_name: str) -> set[str]:
    rows = connection.execute(f"PRAGMA table_info({table_name})").fetchall()
    return {str(row[1]) for row in rows}


def _add_missing_achievement_columns(connection: sqlite3.Connection) -> None:
    columns = _column_names(connection, "achievements")
    additions = {
        "hidden": "INTEGER NOT NULL DEFAULT 0",
        "reward_exp": "INTEGER NOT NULL DEFAULT 0",
        "reward_affection": "INTEGER NOT NULL DEFAULT 0",
        "reward_stamina": "INTEGER NOT NULL DEFAULT 0",
    }

    for column_name, definition in additions.items():
        if column_name not in columns:
            connection.execute(
                "ALTER TABLE achievements "
                f"ADD COLUMN {column_name} {definition}"
            )


def _add_missing_user_columns(connection: sqlite3.Connection) -> None:
    columns = _column_names(connection, "users")
    additions = {
        "neko_streak": "INTEGER NOT NULL DEFAULT 0",
        "last_neko_date": "TEXT",
    }

    for column_name, definition in additions.items():
        if column_name not in columns:
            connection.execute(
                f"ALTER TABLE users ADD COLUMN {column_name} {definition}"
            )


def _seed_initial_achievements(connection: sqlite3.Connection) -> None:
    connection.executemany(
        """
        INSERT INTO achievements (
            code,
            name,
            description,
            hidden,
            reward_exp,
            reward_affection,
            reward_stamina
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(code) DO UPDATE SET
            name = excluded.name,
            description = excluded.description,
            hidden = excluded.hidden,
            reward_exp = excluded.reward_exp,
            reward_affection = excluded.reward_affection,
            reward_stamina = excluded.reward_stamina
        """,
        INITIAL_ACHIEVEMENTS,
    )


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.executescript(SCHEMA_SQL)
    _add_missing_user_columns(connection)
    _add_missing_achievement_columns(connection)
    _seed_initial_achievements(connection)
    connection.commit()
