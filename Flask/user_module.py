import globals

def check_credientials (unchecked_password, unchecked_username): #takes in staticly typed data
    if unchecked_password == globals.DEV_PASSWORD:
        for username in globals.ALLOWED_USERS:
            if unchecked_username == username:
                return True
            else: 
                pass
    else: 
        return False
    