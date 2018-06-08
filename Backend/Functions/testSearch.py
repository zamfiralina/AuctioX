def testSearch(toBeSearched, db_handler):
    result = db_handler.execute("SELECT TITLE FROM ITEMS WHERE TITLE LIKE '" + toBeSearched + "'")

    if result != []:
        message = "SUCCESS"
    else:
        message = "FAIL"
    return message.encode()