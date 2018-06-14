from Backend.DBController.DBConnection import DBConnection

def getAuction (receivedUsername, db_handler: DBConnection)->bytes:
    user_id = db_handler.execute (f"select user_id from SITE_USERS where username like '{receivedUsername}'")[0][0]
    response_nr = db_handler.execute (f"select count(item_id) from items where user_id like '{user_id}' ")[0][0]
    #[1][0]
    response = db_handler.execute (f"select item_id from items where user_id like '{user_id}' ")
    #print(str(response[0][0]))
    #return str(response[0][0]).encode()

    string1 = str(response_nr) + "?"
    for i in range(0,response_nr):
         raspuns = response[i][0]
         string = str(raspuns) + "?"
         string1 = string1 + string

    #print(string1)
    return string1.encode()