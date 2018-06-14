from Backend.DBController.DBConnection import DBConnection

def mostRecent(db_conn: DBConnection):

    result = db_conn.execute(f"SELECT PICTURE, P_NAME, TO_CHAR(S_PRICE), TO_CHAR(END_DATE) FROM ITEMS ORDER BY END_DATE ASC")[:9]

    print("Result: ", result)

    for ind in range(len(result)):
        print(len(result), ind)
        print(result[ind])
        result[ind] = '?'.join(result[ind])
        print(result[ind])

    lastresult = "#".join(result)

    print("REZULTAT  FINAL:", lastresult)

    return lastresult.encode()


