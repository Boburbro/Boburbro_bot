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

def showFIKR():
    """Bazadan fikrlarni ko'ramiz"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    db.commit()
    rows = sql.execute("SELECT * FROM fk_son")
    a = (rows.fetchall())[0][0]
    db.close()
    return a


def addFIKR():
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    key = showFIKR()
    sql.execute(f"UPDATE fk_son SET son = '{str(int(key)+ 1)}' WHERE son = '{key}'")
    db.commit()
    db.close()


def showMQ():
    """Bazadan fikrlarni ko'ramiz"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    db.commit()
    rows = sql.execute("SELECT * FROM fk_mq")
    a = (rows.fetchall())[0][0]
    db.close()
    return a


def addMQ(son: str):
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    key = showMQ()
    sql.execute(f"UPDATE fk_mq SET son = '{str(int(key)+ int(son))}' WHERE son = '{key}'")
    db.commit()
    db.close()

def gerSMEm():
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    rows = sql.execute("SELECT * FROM users")
    users = []
    for row in rows:
        users.append(str(row[0]))
    db.commit()
    db.close()

    return len(users)

def getSta():
    text = 'Statistika:\n'
    text += f'Faydalanuvchilar soni: {gerSMEm()}\n'
    text += f'Fikrlar soni: {showFIKR()}\n'
    text += f'Baxolar miqdori: {int(showMQ())/int(showFIKR())}⭐️\n'


    return text
    
