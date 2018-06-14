from Backend.DBController.DBConnection import DBConnection


def editAuction(receivedItemId, receivedName, receivedCategory, receivedPicture, receivedPrice, receivedStartD,
               receivedEndD, receivedDesc, receivedFabCountry, receivedFabYear, receivedCondition, receivedMaterial,
               receivedColor, receivedSpecialCarac, db_handler: DBConnection):

    receivedContent = receivedName.split ("::::")[1]

    if receivedContent != "":
        result = db_handler._DEBUG_dbCursor.execute ( f"update ITEMS set p_name='{receivedContent}' where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedContent1 = receivedCategory.split ("::::")[1]

    if receivedContent1 != "":
        receivedContent1 = receivedContent1.split ("%20")[0]
        category_id = db_handler.execute (f"select category_id from categories where INSTR(category_name,'{receivedContent1}') > 0")[0][0]
        result = db_handler._DEBUG_dbCursor.execute (f"update ITEMS set category_id ='{category_id}' where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedContent2 = receivedPicture.split ("::::")[1]

    if receivedContent2 != "":
        result = db_handler.execute(f"update ITEMS set picture ='{receivedContent2}' where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedContent3 = receivedPrice.split ("::::")[1]
    if receivedContent3 != "":
        result = db_handler._DEBUG_dbCursor.execute (f"update ITEMS set s_price ='{receivedContent3}' where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedContent4 = receivedStartD.split ("::::")[1]
    receivedContent5 = receivedEndD.split ("::::")[1]

    if receivedContent4 > receivedContent5:
        message = 'START DATE MUST BE LOWER THAN END DATE'
        return message.encode ( )

    if receivedContent4 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update ITEMS set s_price =TO_TIMESTAMP('{receivedContent4}','yyyy-mm-dd') where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    if receivedContent5 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update ITEMS set end_price =TO_TIMESTAMP('{receivedContent5}','yyyy-mm-dd') where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()


    receivedContent6 = receivedDesc.split ("::::")[1]

    if receivedContent6 != "":
        result = db_handler._DEBUG_dbCursor.execute (f"update ITEMS set description = '{receivedContent6}' where item_id='{receivedItemId}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedCategory = receivedFabCountry.split ("::::")[0]
    receivedContent7 = receivedFabCountry.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode ( )

    receivedCategory = receivedFabYear.split ("::::")[0]
    receivedContent7 = receivedFabYear.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode()

    receivedCategory = receivedCondition.split ("::::")[0]
    receivedContent7 = receivedCondition.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode ( )

    receivedCategory = receivedMaterial.split ("::::")[0]
    receivedContent7 = receivedMaterial.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode ( )

    receivedCategory = receivedColor.split ("::::")[0]
    receivedContent7 = receivedColor.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')
        if result == []:
            message = "EDIT FAIL"
            return message.encode ( )

    receivedCategory = receivedSpecialCarac.split ("::::")[0]
    receivedContent7 = receivedSpecialCarac.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"update TAGS set characteristic_value ='{receivedContent7}'"
            f"where item_id='{receivedItemId}' and characteristic_name like'{receivedCategory}'")
        db_handler.execute ('commit')


    if result == []:
        message = "EDIT FAIL"
    else:
        message = "EDIT SUCCESS"

    return message.encode()

