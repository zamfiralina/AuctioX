from Backend.DBController.DBConnection import DBConnection

def getItemFields (receivedAuctionId, db_handler: DBConnection):
    result = db_handler.execute(f"select p_name,s_price,s_date,end_date,description from ITEMS where item_id='{receivedAuctionId}'")
    nume = result[0][0]
    s_price = result[0][1]
    s_date = result[0][2]
    end_date = result[0][3]
    description = result[0][4]
    message = nume + "?" + str(s_price) + "?" + str(s_date) + "?" + str(end_date) + "?" + description

    return message.encode()