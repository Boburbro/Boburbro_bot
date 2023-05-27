from data.config import ADMINS
def isAdmin(chat_id: str) -> str:
    """Admin yoki odiy userligini aniqlaydi"""
    if str(chat_id) in ADMINS:return True
    else:return False
