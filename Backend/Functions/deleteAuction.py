from Backend.DBController.DBConnection import DBConnection

def deleteAuction (receivedAuctionId, db_handler: DBConnection):
    #db_handler._DEBUG_dbCursor.execute(f"CREATE OR REPLACE VIEW COPY_ITEMS as select * from ITEMS;")
    #db_handler._DEBUG_dbCursor.execute(f"CREATE OR REPLACE TRIGGER DELETE_ITEM INSTEAD OF delete ON COPY_ITEMS BEGIN delete from TAGS where item_id =:OLD.item_id; delete from ITEMS where item_id =:OLD.item_id;END;")
    #result = db_handler._DEBUG_dbCursor.execute(f"delete from COPY_ITEMS where item_id='{receivedAuctionId}'")
    #db_handler.execute('commit')
    result = db_handler._DEBUG_dbCursor.execute(f"delete from copy_items where item_id='{receivedAuctionId}'")
    db_handler.execute('commit')
    print(result)
    if result != []:
        message="DELETE SUCCCES"
    else:
        message="FAIL"

    return message.encode()