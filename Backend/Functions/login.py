import hashlib
import time

from Backend.DBController.DBConnection import DBConnection


def login(username: str, password: str, db_conn: DBConnection) -> bytes :
        """
         Checks the user id and SHA256 of the pw against the DB.
         Adds the tuple (user id, SHA256(user id + pw + str(time.asctime()))) to the active users dict.
         Returns the hash computed above.
        """
        passwordHash: bytes = hashlib.sha256((username + password + str(time.asctime())).encode()).digest()

        result = db_conn.execute(f"SELECT COUNT(*) FROM WEB.SITE_USERS WHERE USERNAME LIKE '{username}' AND PASSWORD LIKE '{str(passwordHash)}';"  )

        print(result)

