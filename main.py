def get_admins(ADMINS) -> list:
    '''ADMINS LISTNI TEXTGA AYLANTRADI'''
    if len(ADMINS) == 1:
        return f"{ADMINS[0]}"
    elif len(ADMINS) > 1:
        admin_text = ''
        for admin in ADMINS:
            admin_text += f'{admin},'
        return admin_text
    elif len(ADMINS) == 0:
        print('TypeError')
        exit()
    else:
        print('SyntaxError')
        exit()

def env_write(admins:list,token:str,ip:str):
    '''.env FAYL YOZADI'''
    text=f'''ADMINS={admins}
BOT_TOKEN={token}
ip={ip}'''
    with open('.env', 'w') as f:
        f.write(text)

def maid_body():
    """MAIN QISMI"""
    admin_list = []
    ADMINS = input('Admin kiriting>')
    admin_list.append(ADMINS)
    while ADMINS != '':
        ADMINS = input('Admin kiriting>')
        if ADMINS == "":pass
        else:admin_list.append(ADMINS)
    BOT_TOKEN = input("Bot tokeni kiriting>")
    ip = 'localhost'
    env_write(admins=get_admins(ADMINS=admin_list),token=BOT_TOKEN,ip=ip)

if __name__ == '__main__':maid_body()
else:exit()



