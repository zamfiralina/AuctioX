import os

from typing import Tuple
from http.server import BaseHTTPRequestHandler, HTTPServer

import itertools

from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.editAuction import editAuction
from Backend.Functions.getAuctionsAsXML import getAuctionsAsXML
from Backend.Functions.getItemFields import getItemFields
from Backend.Functions.newBid import newBid
from Backend.Functions.advancedSearch import advancedSearchPage
from Backend.Functions.changeInfo import changeInfo
from Backend.Functions.deleteAuction import deleteAuction
from Backend.Functions.getAuctions import getAuction
from Backend.Functions.getAuctionsAsJson import getAuctionsAsJson
from Backend.Functions.getAuctionsAsPDF import getAuctionsAsPDF
from Backend.Functions.itemDetails import getItemDetails
from Backend.Functions.login import login, logout
from Backend.Functions.mostRecent import mostRecent
from Backend.Functions.newAuction import newAuction
from Backend.Functions.profile import getProfileInfo
from Backend.Functions.register import register
from Backend.Functions.simpleSearch import simpleSearchPage
from Backend.Functions.testSearch import testSearch


class Server(BaseHTTPRequestHandler):
        db_conn = DBConnection.connect("WEB", "WEB", "localhost")

        activeUsers = dict()

        content_types = {'.css': 'text/css',
                         '.gif': 'image/gif',
                         '.htm': 'text/html',
                         '.html': 'text/html',
                         '.jpeg': 'image/jpeg',
                         '.jpg': 'image/jpg',
                         '.js': 'text/javascript',
                         '.png': 'image/png',
                         '.text': 'text/plain',
                         '.txt': 'text/plain'}

        frontend_files = set(itertools.chain.from_iterable(files for _, _, files in os.walk('..\\Frontend')))

        def do_GET(self):
                self.send_response(200)

                content_type, content_body = self.dispatch()

                self.send_header('Content-type', content_type)

                self.end_headers()

                try:
                        self.wfile.write(content_body)

                except Exception as e:
                        print("==========================================================================\n"
                              + str(e) +
                              f'\nRequest:                             \n'
                              f'   type       : <{self.command}>     \n'
                              f'   path       : <{self.path}>        \n'
                              f'   requestline: <{self.requestline}> \n'
                              f'      requestline.split(" ")[0]: <{self.requestline.split(" ")[0]}> \n'
                              f'      requestline.split(" ")[1]: <{self.requestline.split(" ")[1]}> \n'
                              f'      requestline.split(" ")[2]: <{self.requestline.split(" ")[2]}> \n'
                              "========================================================================\n")

        def do_POST(self):
                print('\n\n===\n\nyey\n\n===\n\n')

        def dispatch(self) -> Tuple[str, bytes]:

                print(f'Request:                             \n'
                      f'   type       : <{self.command}>     \n'
                      f'   path       : <{self.path}>        \n'
                      f'   requestline: <{self.requestline}> \n'
                      f'      requestline.split(" ")[0]: <{self.requestline.split(" ")[0]}> \n'
                      f'      requestline.split(" ")[1]: <{self.requestline.split(" ")[1]}> \n'
                      f'      requestline.split(" ")[2]: <{self.requestline.split(" ")[2]}> \n')

                content_type = "text/html"
                content_body = "Error in the dispatch function".encode()

                requestContents = self.requestline.split()[1]

                if requestContents == '/' or requestContents == self.path and requestContents.split('/')[
                        -1] in self.frontend_files:
                        print('PATH ', self.path, '\nCONT ', requestContents)
                        if self.path == '/' or self.path == '/favicon.ico':
                                self.path = '/index.html'
                        content_type = self.__class__.content_types[os.path.splitext(self.path)[1]]
                        content_body = open('../Frontend' + self.path, 'rb').read()

                if requestContents.startswith("/SEARCH"):
                        toBeSearched = requestContents.split("?")[1]
                        content_body = testSearch(toBeSearched, self.__class__.db_conn)

                if requestContents.startswith("/LOGIN"):
                        receivedUsername = requestContents.split("?")[1]
                        receivedPassword = requestContents.split("?")[2]
                        content_body = login(receivedUsername, receivedPassword, self.__class__.db_conn,
                                             self.__class__.activeUsers)
                        print(content_body)

                if requestContents.startswith("/LOGOUT"):
                        userHash = requestContents.split("?")[1].replace("%20", " ")
                        content_body = logout(userHash, self.__class__.activeUsers)

                if requestContents.startswith("/GETPROFILEINFO"):
                        userHash = requestContents.split("?")[1].replace("%20", " ")
                        content_body = getProfileInfo(self.__class__.activeUsers[userHash], self.__class__.db_conn)

                if requestContents.startswith("/REGISTER"):
                        print(requestContents)
                        fname = requestContents.split("?")[1]
                        lname = requestContents.split("?")[2]
                        username = requestContents.split("?")[3]
                        password = requestContents.split("?")[4]
                        country = requestContents.split("?")[5]
                        city = requestContents.split("?")[6]
                        tel = requestContents.split("?")[7]
                        email = requestContents.split("?")[8]
                        link = requestContents.split("?")[9]
                        content_body = register(fname, lname, username, password, country, city, tel, email, link,
                                                self.__class__.db_conn)

                if requestContents.startswith("/CHANGE"):
                        newFirstName = requestContents.split("?")[1]
                        newLastName = requestContents.split("?")[2]
                        newPass = requestContents.split("?")[3]
                        newCity = requestContents.split("?")[4]
                        newTel = requestContents.split("?")[5]
                        newEmail = requestContents.split("?")[6]
                        newLink = requestContents.split("?")[7]
                        userHash = requestContents.split("?")[8].replace("%20", " ")
                        if userHash in self.activeUsers:
                                username = self.activeUsers[userHash]
                                content_body = changeInfo(newFirstName, newLastName, newPass, newCity, newTel, newEmail, newLink,
                                                          self.__class__.db_conn, username)
                        else:
                                content_body = "You are not logged in.".encode()

                if requestContents.startswith("/ISUSERLOGGEDIN"):
                        print("requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers",
                              requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers)
                        if requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers:
                                content_body = "USERLOGGEDINSUCCESS".encode()
                        else:
                                # except Exception as e:
                                content_body = "USERLOGGEDINFAIL".encode()

                if requestContents.startswith("/NEWAUCTION"):
                        #TODO: verify if user is logged in
                        # print (requestContents)
                        receivedName = requestContents.split("???")[1].replace("%20", " ")
                        receivedCategory = requestContents.split("???")[2].replace("%20", " ")
                        receivedPicture = requestContents.split("???")[3].replace("%20", " ")
                        receivedPrice = requestContents.split("???")[4].replace("%20", " ")
                        receivedStartD = requestContents.split("???")[5].replace("%20", " ")
                        receivedEndD = requestContents.split("???")[6].replace("%20", " ")
                        receivedDesc = requestContents.split("???")[7].replace("%20", " ")
                        receivedFabCountry = requestContents.split("???")[8].replace("%20", " ")
                        receivedFabYear = requestContents.split("???")[9].replace("%20", " ")
                        receivedCondition = requestContents.split("???")[10].replace("%20", " ")
                        receivedMaterial = requestContents.split("???")[11].replace("%20", " ")
                        receivedColor = requestContents.split("???")[12].replace("%20", " ")
                        receivedSpecialCarac = requestContents.split("???")[13].replace("%20", " ")
                        receivedUsernameHash = requestContents.split("???")[14].replace("%20", " ")
                        print("UsernameHash", receivedUsernameHash)
                        receivedUsername = self.__class__.activeUsers[receivedUsernameHash]
                        content_body = newAuction(receivedUsername, receivedName, receivedCategory, receivedPicture,
                                                  receivedPrice, receivedStartD, receivedEndD, receivedDesc,
                                                  receivedFabCountry, receivedFabYear, receivedCondition,
                                                  receivedMaterial, receivedColor, receivedSpecialCarac,
                                                  self.__class__.db_conn)


                        # print(requestContents,requestContents.startswith("/NEWAUCTION"))

                if requestContents.startswith("/GETSIMPLESEARCHRESULTSPAGE"):
                        page, itemName = requestContents.replace("%20", " ").split("?")[1:]
                        print("to be searched: ", itemName)
                        print("page:", page)
                        content_body = simpleSearchPage(itemName.lower(), page, self.__class__.db_conn)

                if requestContents.startswith("/RECENT"):
                    content_body = mostRecent(self.__class__.db_conn)

                if requestContents.startswith("/GETADVANCEDSEARCHRESULTSPAGE"):
                        page, tags = requestContents.replace("%20", " ").split("!")[1:]
                        content_body = advancedSearchPage(page, tags, self.db_conn)

                if requestContents.startswith("/GETITEMDETAILS"):
                        itemId = int(requestContents.split("?")[-1])
                        content_body = getItemDetails(itemId, self.db_conn)

                if requestContents.startswith ("/USERAUCTIONS"):
                        receivedUsernameHash = requestContents.split ("?")[1].replace ("%20", " ")
                        receivedUsername = self.__class__.activeUsers[receivedUsernameHash]
                        content_body = getAuction(receivedUsername, self.__class__.db_conn)

                if requestContents.startswith ("/DELETE"):
                        receivedAuctionId = requestContents.split ("?")[1]
                        print (receivedAuctionId)
                        content_body = deleteAuction(receivedAuctionId, self.__class__.db_conn)
                        print ("out of function")

                if requestContents.startswith("/GETJSONEXPORT"):
                        userHash = requestContents.replace('%20', ' ').split('?')[1]
                        content_body = getAuctionsAsJson(self.db_conn)

                if requestContents.startswith("/GETPDFEXPORT"):
                        userHash = requestContents.replace('%20', ' ').split('?')[1]
                        content_body = getAuctionsAsPDF(self.db_conn)
                        content_type = 'application/pdf'

                if requestContents.startswith("/GETXMLEXPORT"):
                        userHash = requestContents.replace('%20', ' ').split('?')[1]
                        content_body = getAuctionsAsXML(self.db_conn)
                        content_type = 'text/xml'

                if requestContents.startswith("/NEWBID"):
                        offer    = requestContents.replace('%20', ' ').split('?')[1]
                        itemId   = requestContents.replace('%20', ' ').split('?')[2]
                        userHash = requestContents.replace('%20', ' ').split('?')[3]
                        content_body = newBid(itemId, offer, self.db_conn)

                if requestContents.startswith ("/EDIT"):
                    receivedName = requestContents.split ("???")[1].replace ("%20", " ")
                    receivedCategory = requestContents.split ("???")[2].replace ("%20", " ")
                    receivedPicture = requestContents.split ("???")[3].replace ("%20", " ")
                    receivedPrice = requestContents.split ("???")[4].replace ("%20", " ")
                    receivedStartD = requestContents.split ("???")[5].replace ("%20", " ")
                    receivedEndD = requestContents.split ("???")[6].replace ("%20", " ")
                    receivedDesc = requestContents.split ("???")[7].replace ("%20", " ")
                    receivedFabCountry = requestContents.split ("???")[8].replace ("%20", " ")
                    receivedFabYear = requestContents.split ("???")[9].replace ("%20", " ")
                    receivedCondition = requestContents.split ("???")[10].replace ("%20", " ")
                    receivedMaterial = requestContents.split ("???")[11].replace ("%20", " ")
                    receivedColor = requestContents.split ("???")[12].replace ("%20", " ")
                    receivedSpecialCarac = requestContents.split ("???")[13].replace ("%20", " ")
                    receivedItemId = requestContents.split ("???")[14].replace ("%20", " ")
                    #print ("ItemId", receivedItemId)
                    content_body = editAuction (receivedItemId, receivedName, receivedCategory, receivedPicture,
                                               receivedPrice, receivedStartD, receivedEndD, receivedDesc,
                                               receivedFabCountry, receivedFabYear, receivedCondition, receivedMaterial,
                                               receivedColor, receivedSpecialCarac, self.__class__.db_conn)



                if requestContents.startswith("/GETITEMFIELDS"):
                    receivedAuctionId = requestContents.split ("???")[1]
                    #print("LICITATIA ACTIVA" + receivedAuctionId)
                    content_body = getItemFields(receivedAuctionId, self.__class__.db_conn)

                return content_type, content_body


def run():
        print('starting server...')

        server_address = ('127.0.0.1', 8081)

        httpd = HTTPServer(server_address, Server)

        print('running server...')
        httpd.serve_forever()


run()
