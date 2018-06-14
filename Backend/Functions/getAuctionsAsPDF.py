import fpdf
from fpdf import  FPDF

from Backend.DBController.DBConnection import DBConnection


def getAuctionsAsPDF(db_handler: DBConnection) -> bytes:
    result = db_handler.execute(f"SELECT TO_CHAR(I.ITEM_ID), I.P_NAME, TO_CHAR(I.S_PRICE), TO_CHAR(I.S_DATE), TO_CHAR(I.END_DATE), C.CATEGORY_NAME FROM ITEMS I JOIN CATEGORIES C ON I.CATEGORY_ID = C.CATEGORY_ID WHERE SYSDATE < I.END_DATE")

    print(result)
    results = ""
    nrobiecte = 0
    for ind in range(len(result)):
        for ind2 in range(6):
            if(ind2 % 6 == 0):
                results += ' Item id: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            if(ind2 % 6 == 1):
                results += ' Name: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            if(ind2 % 6 == 2):
                results += ' Price: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            if(ind2 % 6 == 3):
                results += ' Start date: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            if(ind2 % 6 == 4):
                results += ' End date: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            if(ind2 % 6 == 5):
                results += ' Category: ' + result[ind][ind2] + 'endl'
                nrobiecte += 1
            # if(ind2 % 6 == 6):
            #     results += ' Characteristic name: ' + result[ind][ind2]
            # if(ind2 % 6 == 7):
            #     results += 'Characteristic value: ' + result[ind][ind2]
        curItemId = result[ind][0]
        tags = db_handler.execute(f"SELECT CHARACTERISTIC_NAME, CHARACTERISTIC_VALUE FROM TAGS where ITEM_ID = {curItemId}")
        for index in range(len(tags)):
                results += tags[index][0] + ' : ' + tags[index][1] + 'endl'
                nrobiecte += 1

    print(results)
    print('NR OBIECTE: ', nrobiecte)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    for index in range(nrobiecte):
        curString = results.split('endl')[index]
        pdf.cell(0, 10, curString, 0, 2)
    pdf.output('auctionsPDF.pdf', 'F')

    return open('auctionsPDF.pdf', 'rb').read()

