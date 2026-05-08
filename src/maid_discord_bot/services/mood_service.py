# services/mood_service.py

def determine_mood(stamina: int) -> str:
    """staminaの値からmoodを判定する。"""
    if stamina < 20:
        return "sleepy"
    if stamina < 40:
        return "tired"
    if stamina < 70:
        return "normal"
    return "happy"


def mood_display_name(mood: str) -> str:  # ← 旧: mood_to_japanese
    """moodを日本語に変換する。"""
    table = {
        "happy": "元気",
        "normal": "普通",
        "tired": "疲れ気味",
        "sleepy": "しょんぼり",
    }
    return table.get(mood, "不明")


def mood_to_color(mood: str) -> int:
    """moodに応じたEmbedの色（16進数）を返す。"""
    colors = {
        "happy":  0xFFD700,
        "normal": 0x7EC8E3,
        "tired":  0xFFA500,
        "sleepy": 0x9B9B9B,
    }
    return colors.get(mood, 0xAAAAAA)


def mood_asset_path(mood: str) -> str:  # ← 旧: mood_to_image_path
    """moodに応じた立ち絵のファイルパスを返す。"""
    paths = {
        "happy":  "assets/happy.png",
        "normal": "assets/normal.png",
        "tired":  "assets/tired.png",
        "sleepy": "assets/sleepy.png",
    }
    return paths.get(mood, "assets/normal.png")
