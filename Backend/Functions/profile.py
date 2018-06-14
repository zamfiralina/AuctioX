from Backend.DBController.DBConnection import DBConnection


def getProfileInfo(username: str, db_conn: DBConnection) -> bytes:
        result = list(db_conn.execute(f"SELECT * FROM SITE_USERS WHERE USERNAME LIKE '{username}'")[0][1:])

        del result[4]

        #firstName, lastName, email, _, country, city, tel, picLink = result

        return "???".join(result).encode()