from Backend.DBController.DBConnection import DBConnection


def getItemDetails(itemId: int, db_conn: DBConnection) -> bytes:
        itemDetails  = list(db_conn.execute(f"SELECT TO_CHAR(ITEM_ID), TO_CHAR(USER_ID), P_NAME, TO_CHAR(CATEGORY_ID), PICTURE, TO_CHAR(S_PRICE), TO_CHAR(S_DATE), TO_CHAR(END_DATE), DESCRIPTION FROM ITEMS WHERE ITEM_ID = {itemId}")[0])

        itemCategory = db_conn.execute(f"SELECT CATEGORY_NAME FROM CATEGORIES WHERE CATEGORY_ID = {itemDetails[3]}")[0][0]

        itemTags     = db_conn.execute(f"SELECT CHARACTERISTIC_NAME, CHARACTERISTIC_VALUE FROM TAGS WHERE ITEM_ID = {itemId}")
        itemTags     = "!".join(f"{tag_name}~{tag_val}" for tag_name, tag_val in itemTags)

        itemSeller, itemTlf, itemEmail, itemLocation   = db_conn.execute(f"SELECT USERNAME, TELEPHONE, EMAIL, COUNTRY||', '||CITY FROM SITE_USERS WHERE USER_ID = {itemDetails[1]}")[0]

        itemDetails.append(itemCategory)
        itemDetails.append(itemTags)
        itemDetails.append(itemSeller)
        itemDetails.append(itemTlf)
        itemDetails.append(itemEmail)
        itemDetails.append(itemLocation)

        return "?".join(itemDetails).encode()
