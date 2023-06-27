from data.config import ADMINS
def isAdmin(chat_id: str):
    """Admin yoki odiy userligini aniqlaydi"""
    if str(chat_id) in ADMINS:return True
    else:return False
def isNewMember(chat_id: str):
    """Yangi yoki eski user ligini aniqlaydi"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    rows = sql.execute("SELECT * FROM users")
    users = []
    for row in rows:
        users.append(str(row[0]))
    db.commit()
    db.close()
    if str(chat_id) in users:
        return False
    else:
        return True

def addNewMember(chat_id: str):
    """Yangi userni bazaga saqlaydi"""
    try:
        import sqlite3
        db = sqlite3.connect('baza.db')
        sql = db.cursor()
        sql.execute(f"INSERT INTO users VALUES ('{chat_id}')")
        db.commit()
        db.close()
        return True
    except:
        return False
