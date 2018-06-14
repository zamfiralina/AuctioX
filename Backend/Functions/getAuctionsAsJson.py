import json

def getAuctionsAsJson(db_handler):
    result = db_handler.execute(f"SELECT ITEM_ID, P_NAME, S_PRICE, DESCRIPTION, TO_CHAR(END_DATE) FROM ITEMS  WHERE SYSDATE < END_DATE")

    auctions = dict()

    for ind in range(len(result)):
        auctions[str(ind)] = {
                'Name': result[ind][1],
                'Price': result[ind][2],
                'Description': result[ind][3],
                'End date' : result[ind][4]
            }


    jsn = json.dumps(auctions)

    print(auctions)
    print()
    print(jsn)