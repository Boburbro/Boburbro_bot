txt = """
@xinuxuz @linux_uzbek - linux
@uzbwindows - win
@python_uz - python
@dartuzb @flutterwithakmaljon - dart va flutter 
@Androidchilar - android
@Java_UZB - java

"""
def SQLadd_():
    """Bazaga key va text qo'shadi"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    sql.execute(f"INSERT INTO guruh VALUES ('{txt}', 'g1')")
    db.commit()
    db.close()

def SQLcreate_():
    """Baza va bazani ichiga reak tableni qo'shadi, tableni ichida 2 ta qiymat key va text"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    sql.execute('CREATE TABLE IF NOT EXISTS guruh (gtext TEXT, key TEXT)')
    db.commit()
    db.close()

# # # def SQLDelete_(key: str):
# # #     """Bazada bor key ni text bilan o'chiradi"""
# # #     import sqlite3
# # #     db = sqlite3.connect('baza.db')
# # #     sql = db.cursor()
# # #     sql.execute(f"DELETE FROM reak WHERE key='{key}'")
# # #     db.commit()
# # #     db.close()



def showMQ():
    """Bazadan key orqali malumotlar olamiz"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    db.commit()
    rows = sql.execute("SELECT * FROM guruh")
    a = (rows.fetchall())[0][0]
    db.close()
    return a

def SQLupdareByKey_(a):
    """Bazadagi textni key orqali update qiladi"""
    import sqlite3
    db = sqlite3.connect('baza.db')
    sql = db.cursor()
    sql.execute(f"UPDATE guruh SET gtext = '{a}' WHERE key = 'g1'")
    db.commit()
    db.close()

# # def addMQ(son: str):
# #     import sqlite3
# #     db = sqlite3.connect('baza.db')
# #     sql = db.cursor()
# #     key = showMQ()
# #     sql.execute(f"UPDATE fk_mq SET son = '{str(int(key)- int(son))}' WHERE son = '{key}'")
# #     db.commit()
# #     db.close()

# # if __name__ == '__main__':
# #     #SQLupdareByKey_()
# #     showMQ()
    
    

# from googletrans import Translator
# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.text)


# SQLcreate_()
# SQLadd_()
showMQ()
# SQLupdareByKey_(txt)
showMQ()