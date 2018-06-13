from Backend.DBController.DBConnection import DBConnection

def newAuction (receivedUsername,receivedName, receivedCategory, receivedPicture, receivedPrice, receivedStartD, receivedEndD, receivedDesc, receivedFabCountry, receivedFabYear, receivedCondition, receivedMaterial, receivedColor, receivedSpecialCarac, db_handler: DBConnection):

    #print(receivedUsername)
    receivedContent = receivedName.split ("::::")[1]
    if receivedContent == "":
        message='COMPULSORY FIELD IS EMPTY: ITEM NAME'
        return message.encode()

    receivedContent1 = receivedCategory.split ("::::")[1]
    if receivedContent1 == "":
        message='COMPULSORY FIELD IS EMPTY: CATEGORY'
        return message.encode()

    receivedContent2 = receivedPicture.split ("::::")[1]
    if receivedContent2 == "":
        message='COMPULSORY FIELD IS EMPTY: LINK TO A PICTURE'
        return message.encode()

    receivedContent3 = receivedPrice.split ("::::")[1]
    if receivedContent3 == "":
        message = 'COMPULSORY FIELD IS EMPTY: START PRICE'
        return message.encode()

    receivedContent4 = receivedStartD.split ("::::")[1]
    if receivedContent4 == "":
        message = 'COMPULSORY FIELD IS EMPTY: START DATE'
        return  message.encode()

    receivedContent5 = receivedEndD.split ("::::")[1]
    if receivedContent5 == "":
        message = 'COMPULSORY FIELD IS EMPTY: END DATE'
        return message.encode()

    if receivedContent4 > receivedContent5:
        message = 'START DATE MUST BE LOWER THAN END DATE'
        return message.encode ( )

    receivedContent6 = receivedDesc.split ("::::")[1]

    receivedContent1 = receivedContent1.split ("%20")[0]
    id_category = db_handler.execute(f"select category_id from categories where INSTR(category_name,'{receivedContent1}') > 0  ")
    category_id=id_category[0][0]

    id_item = db_handler.execute(f"select max(item_id) from items")
    id = id_item[0][0] + 1

    us_id = db_handler.execute(f"select user_id from SITE_USERS where username like '{receivedUsername}'")
    username_id = us_id[0][0]
    if receivedContent6 != "":
        result = db_handler._DEBUG_dbCursor.execute (f"insert into ITEMS values('{id}','{username_id}','{receivedContent}','{category_id}','{receivedContent2}','{receivedContent3}',TO_TIMESTAMP('{receivedContent4}','yyyy-mm-dd'), TO_TIMESTAMP('{receivedContent5}','yyyy-mm-dd'),'{receivedContent6}')")
        db_handler.execute('commit')
    else:
        result = db_handler._DEBUG_dbCursor.execute (f"insert into ITEMS values('{id}','{username_id}','{receivedContent}','{category_id}','{receivedContent2}','{receivedContent3}',TO_TIMESTAMP('{receivedContent4}','yyyy-mm-dd'), TO_TIMESTAMP('{receivedContent5}','yyyy-mm-dd'),null)")
        db_handler.execute ('commit')

    id_tag = db_handler.execute(f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedFabCountry.split ("::::")[0]
    receivedContent7 = receivedFabCountry.split ("::::")[1]
    if receivedContent7 != "":
        result =db_handler._DEBUG_dbCursor.execute(f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute('commit')

    id_tag = db_handler.execute (f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedFabYear.split ("::::")[0]
    receivedContent7 = receivedFabYear.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute ( f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute('commit')

    id_tag = db_handler.execute (f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedCondition.split ("::::")[0]
    receivedContent7 = receivedCondition.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute ('commit')

    id_tag = db_handler.execute (f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedMaterial.split ("::::")[0]
    receivedContent7 = receivedMaterial.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute ('commit')

    id_tag = db_handler.execute (f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedColor.split ("::::")[0]
    receivedContent7 = receivedColor.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute ('commit')

    id_tag = db_handler.execute (f"select max(id) from tags")
    tag_id = id_tag[0][0] + 1
    receivedCategory = receivedSpecialCarac.split ("::::")[0]
    receivedContent7 = receivedSpecialCarac.split ("::::")[1]
    if receivedContent7 != "":
        result = db_handler._DEBUG_dbCursor.execute (
            f"insert into TAGS values('{tag_id}','{id}','{receivedCategory}','{receivedContent7}')")
        db_handler.execute ('commit')

    if result != []:
        message="SUCCCES"
    else:
        message="FAIL"

    return message.encode()
