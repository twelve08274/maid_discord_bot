import unittest
from types import SimpleNamespace

from src.commands.where import register_where_command


class _FakeTree:
    def __init__(self) -> None:
        self.commands: list[str] = []

    def command(self, name: str, description: str):
        del description

        def decorator(func):
            self.commands.append(name)
            return func

        return decorator


class WhereCommandTests(unittest.TestCase):
    def test_where_debug_is_not_registered_by_default(self) -> None:
        bot = SimpleNamespace(tree=_FakeTree())

        register_where_command(bot)

        self.assertIn("where", bot.tree.commands)
        self.assertNotIn("where_debug", bot.tree.commands)

    def test_where_debug_is_registered_when_debug_enabled(self) -> None:
        bot = SimpleNamespace(tree=_FakeTree())

        register_where_command(bot, debug_enabled=True)

        self.assertIn("where", bot.tree.commands)
        self.assertIn("where_debug", bot.tree.commands)


if __name__ == "__main__":
    unittest.main()
