import time

from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.unicodeHash import unicodeHash

def login(username: str, password: str, db_conn: DBConnection, activeUsers: dict) -> bytes :
        """
         Checks the user id and SHA256 of the pw against the DB.
         Adds the tuple (user id, SHA256(user id + pw + str(time.asctime()))) to the active users dict.
         Returns the hash computed above.
        """

        result = db_conn.execute(f"SELECT COUNT(*) FROM SITE_USERS WHERE USERNAME LIKE '{username}' AND PASSWORD LIKE '{unicodeHash(password)}'") #AND PASSWORD LIKE '{str(passwordHash)}'"  )

        print("Result: ", result)
        print("PasswordHash: ", unicodeHash(password))

        print("Select... ", db_conn.execute("SELECT PASSWORD FROM SITE_USERS WHERE USERNAME LIKE 'username'"))

        if result == [(0,)]:
                return "LOGINFAIL".encode()

        else:
                userHash = unicodeHash(username + password + str(time.asctime()))
                activeUsers[userHash] = username
                return ("LOGINSUCCESS?" + userHash).encode()
