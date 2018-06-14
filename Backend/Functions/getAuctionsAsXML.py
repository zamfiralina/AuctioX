import xml.etree.cElementTree as ET
from Backend.DBController.DBConnection import DBConnection


def getAuctionsAsXML(db_handler : DBConnection):
    result = db_handler.execute(f"SELECT TO_CHAR(ITEM_ID), P_NAME, TO_CHAR(S_PRICE), DESCRIPTION, TO_CHAR(END_DATE) FROM ITEMS  WHERE SYSDATE < END_DATE")
    auctions = ET.Element("auctions")
    for ind in range(len(result)):
        item = ET.SubElement(auctions, "item")
        for ind2 in range(5):
            if(ind2 % 5 == 0):
                ET.SubElement(item, "item_id").text = result[ind][ind2]
            if (ind2 % 5 == 1):
                ET.SubElement(item, "item_name").text = result[ind][ind2]
            if (ind2 % 5 == 2):
                ET.SubElement(item, "item_price").text = result[ind][ind2]
            if (ind2 % 5 == 3):
                ET.SubElement(item, "item_description").text = result[ind][ind2]
            if (ind2 % 5 == 4):
                ET.SubElement(item, "end_date").text = result[ind][ind2]

    tree = ET.ElementTree(auctions)
    tree.write('auctions.xml')