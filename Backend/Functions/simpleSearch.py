from Backend.DBController.DBConnection import DBConnection


def simpleSearch(toBeSearched: str, db_handler: DBConnection) -> bytes:
    result = db_handler.execute(f"SELECT PICTURE, P_NAME, TO_CHAR(S_PRICE), TO_CHAR(END_DATE) FROM ITEMS WHERE P_NAME LIKE '%{toBeSearched}%'")[:9]

    print("RESULT:",result)
    #del result[4]

    # firstName, lastName, email, _, country, city, tel, picLink = result

    for ind in range(len(result)):
        print(len(result), ind)
        print(result[ind])
        result[ind] = '?'.join(result[ind])
        print(result[ind])

    result2 = "#".join(result)

    print("REZULTAT  FINAL:", result2)

    return result2.encode()