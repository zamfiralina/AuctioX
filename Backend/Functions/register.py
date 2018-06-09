from Backend.Functions.unicodeHash import unicodeHash


def register(fname, lname, username, password, country, city , tel, email, link, db_handler):
    result = db_handler.execute(f"SELECT USERNAME FROM SITE_USERS WHERE USERNAME LIKE '{username}'")

    if result != []:
        message = "USERNAME ALREADY EXISTS."
    else:
        id_user = db_handler.execute("SELECT COUNT(USERNAME) FROM SITE_USERS")
        id = id_user[0][0] + 1
        print(id_user[0][0])

       #statement = db_handler.execute()
        hashPassword = unicodeHash(password)
        statement = db_handler.execute(f"INSERT INTO SITE_USERS VALUES ({id},'{fname}','{lname}','{email}', '{username}', '{hashPassword}', '{country}', '{city}', '{tel}', '{link}' )")
        print(statement)
        db_handler.execute("Commit")
        verify = db_handler.execute(f"SELECT * FROM SITE_USERS WHERE USER_ID = {id}")
        print(verify)
        if verify != []:
            message = "INSERT SUCCES."
        else:
            message = "INSERT FAIL."
    return message.encode()