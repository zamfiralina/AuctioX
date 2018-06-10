from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.profile import getProfileInfo

def changeInfo(newFirstname, newLastname, newCity, newTel, newEmail, newLink, db_conn: DBConnection):
    user=getProfileInfo(newFirstname,db_conn)

    result = db_conn.execute(f"UPDATE SITE_USERS SET FIRST_NAME='{newFirstname}', LAST_NAME='{newLastname}', CITY='{newCity}', TELEPHONE='{newTel}', EMAIL='{newEmail}', LINK_PIC='{newLink}' WHERE USERNAME LIKE {'user'}")

    if result != []:
        message = "merge"
    else:
        message = "tot merge, dar nu e numele"
    print(message)