import unittest
from datetime import UTC, datetime
from types import SimpleNamespace

from src.commands.campusnow import (
    _campus_all_embed,
    register_campusnow_command,
)
from src.services.campus_now_service import CampusAll, CampusNow, ClusterNow


class _FakeTree:
    def __init__(self) -> None:
        self.commands: list[str] = []

    def command(self, name: str, description: str):
        del description

        def decorator(func):
            self.commands.append(name)
            return func

        return decorator


class CampusNowCommandTests(unittest.TestCase):
    def test_campus_commands_are_registered(self) -> None:
        bot = SimpleNamespace(tree=_FakeTree())

        register_campusnow_command(bot)

        self.assertIn("campus", bot.tree.commands)
        self.assertIn("campusnow", bot.tree.commands)
        self.assertIn("campusall", bot.tree.commands)

    def test_campusall_embed_uses_compact_fields(self) -> None:
        fetched_at = datetime.now(UTC)
        campus_all = CampusAll(
            campus=CampusNow(
                active_count=128,
                pc_count=300,
                crowd_percent=42.7,
                comment="hidden campus comment",
                fetched_at=fetched_at,
            ),
            clusters=(
                ClusterNow(
                    cluster_id="c1",
                    cluster_name="koi",
                    active_count=14,
                    seat_count=56,
                    crowd_percent=25.0,
                    comment="hidden cluster comment",
                    fetched_at=fetched_at,
                ),
                ClusterNow(
                    cluster_id="c2",
                    cluster_name="ume",
                    active_count=4,
                    seat_count=74,
                    crowd_percent=5.4,
                    comment="hidden cluster comment",
                    fetched_at=fetched_at,
                ),
                ClusterNow(
                    cluster_id="c3",
                    cluster_name="washi",
                    active_count=3,
                    seat_count=46,
                    crowd_percent=6.5,
                    comment="hidden cluster comment",
                    fetched_at=fetched_at,
                ),
                ClusterNow(
                    cluster_id="c4",
                    cluster_name="fuji",
                    active_count=10,
                    seat_count=48,
                    crowd_percent=20.8,
                    comment="hidden cluster comment",
                    fetched_at=fetched_at,
                ),
            ),
        )

        embed = _campus_all_embed(campus_all)

        self.assertIsNone(embed.description)
        self.assertEqual(len(embed.fields), 6)
        self.assertEqual(embed.fields[0].name, "Campus")
        self.assertEqual(
            embed.fields[0].value,
            "\u4eba\u6570/\u5e2d\u6570: **128 / 300**\n"
            "\u200b\u6df7\u96d1\u7387: **42.7%**",
        )
        self.assertFalse(embed.fields[0].inline)
        self.assertEqual(embed.fields[1].name, "c1/koi")
        self.assertEqual(
            embed.fields[1].value,
            "\u4eba\u6570/\u5e2d\u6570: **14 / 56**\n"
            "\u200b\u6df7\u96d1\u7387: **25.0%**",
        )
        self.assertTrue(embed.fields[1].inline)
        self.assertEqual(embed.fields[4].name, "\u200b")
        self.assertEqual(embed.fields[4].value, "\u200b")
        self.assertFalse(embed.fields[4].inline)
        self.assertEqual(embed.fields[5].name, "c4/fuji")
        self.assertNotIn("hidden", embed.fields[0].value)
        self.assertNotIn("hidden", embed.fields[1].value)


if __name__ == "__main__":
    unittest.main()
