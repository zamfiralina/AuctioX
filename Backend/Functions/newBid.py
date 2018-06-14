from Backend.DBController.DBConnection import DBConnection


def newBid(itemId: str, offer: str, db_conn: DBConnection) -> bytes:

        currentPrice = int(db_conn.execute(f"SELECT S_PRICE FROM ITEMS WHERE ITEM_ID = {itemId}")[0][0])

        if currentPrice >= int(offer):
                return b'BID_TL'


        db_conn.execute(f"UPDATE ITEMS SET S_PRICE = {offer} WHERE ITEM_ID = {itemId}")
        db_conn.execute("COMMIT")

        return b'BID_A'
