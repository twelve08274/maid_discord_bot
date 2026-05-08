def determine_mood(stamina: int) -> str:
    if stamina < 20:
        return "sleepy"
    if stamina < 40:
        return "tired"
    if stamina < 70:
        return "normal"
    return "happy"


def mood_display_name(mood: str) -> str:
    names = {
        "happy": "Happy",
        "normal": "Normal",
        "tired": "Tired",
        "sleepy": "Sleepy",
    }
    return names.get(mood, "Unknown")


def mood_to_color(mood: str) -> int:
    colors = {
        "happy": 0xFFD700,
        "normal": 0x7EC8E3,
        "tired": 0xFFA500,
        "sleepy": 0x9B9B9B,
    }
    return colors.get(mood, 0xAAAAAA)


def mood_asset_path(mood: str) -> str:
    paths = {
        "happy": "assets/happy.png",
        "normal": "assets/normal.png",
        "tired": "assets/tired.png",
        "sleepy": "assets/sleepy.png",
    }
    return paths.get(mood, "assets/normal.png")


def level_group(level: int) -> str:
    """levelをグループ名に変換する。"""
    if level <= 5:
        return "low"
    if level <= 10:
        return "mid"
    return "high"


def character_image_path(level: int, mood: str) -> str:
    """levelとmoodの組み合わせで画像パスを返す。"""
    group = level_group(level)
    return f"assets/{group}_{mood}.png"
