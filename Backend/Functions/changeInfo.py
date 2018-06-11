from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.unicodeHash import unicodeHash


def changeInfo(newFirstName, newLastName, newCity, newTel, newEmail, newLink, db_conn: DBConnection, username):
    ok=1
    if newFirstName != "":
        result1 = db_conn.execute(f"UPDATE SITE_USERS SET FIRST_NAME='{newFirstName}' WHERE username LIKE '{username}'")
        if result1 == []:
            ok = 0
        else:
            db_conn.execute("Commit")

    if newLastName != "":
        result2 = db_conn.execute(f"UPDATE SITE_USERS SET LAST_NAME='{newLastName}' WHERE username LIKE '{username}'")
        if result2 == []:
            ok=0
        else:
            db_conn.execute("Commit")

    if newCity != "":
        result3 = db_conn.execute(f"UPDATE SITE_USERS SET CITY='{newCity}' WHERE username LIKE '{username}'")
        if result3 == []:
            ok=0
        else:
            db_conn.execute("Commit")

    if newTel != "":
        result4 = db_conn.execute(f"UPDATE SITE_USERS SET TELEPHONE ='{newTel}' WHERE username LIKE '{username}'")
        if result4 == []:
            ok=0
        else:
            db_conn.execute("Commit")

    if newEmail != "":
        result5 = db_conn.execute(f"UPDATE SITE_USERS SET EMAIL='{newEmail}' WHERE username LIKE '{username}'")
        if result5 == []:
            ok=0
        else:
            db_conn.execute("Commit")

    if newLink != "":
        result6 = db_conn.execute(f"UPDATE SITE_USERS SET LINK_PIC='{newLink}' WHERE username LIKE '{username}'")
        if result6 == []:
            ok=0
        else:
            db_conn.execute("Commit")



    if ok == 1:
        message = "Update successful."
    else:
        message = "Update failed."

    return message.encode()
