import os

from typing import Tuple
from http.server import BaseHTTPRequestHandler, HTTPServer

from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.changeInfo import changeInfo
from Backend.Functions.login import login, logout
from Backend.Functions.newAuction import newAuction
from Backend.Functions.profile import getProfileInfo
from Backend.Functions.register import register
from Backend.Functions.simpleSearch import simpleSearch
from Backend.Functions.testSearch import testSearch


class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
        db_conn = DBConnection.connect("WEB", "WEB", "localhost")

        activeUsers = dict()

        content_types = {'.css' : 'text/css',
                         '.gif' : 'image/gif',
                         '.htm' : 'text/html',
                         '.html': 'text/html',
                         '.jpeg': 'image/jpeg',
                         '.jpg' : 'image/jpg',
                         '.js'  : 'text/javascript',
                         '.png' : 'image/png',
                         '.text': 'text/plain',
                         '.txt' : 'text/plain'}

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

                if requestContents == '/' or requestContents == self.path and self.path == self.path.split('?')[0]:
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
                        content_body = login(receivedUsername, receivedPassword, self.__class__.db_conn, self.__class__.activeUsers)
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
                    content_body = register(fname, lname, username, password, country, city, tel, email, link, self.__class__.db_conn)

                if requestContents.startswith("/CHANGE"):
                    newFirstName = requestContents.split("?")[1]
                    newLastName = requestContents.split("?")[2]
                    newCity = requestContents.split("?")[3]
                    newTel = requestContents.split("?")[4]
                    newEmail = requestContents.split("?")[5]
                    newLink = requestContents.split("?")[6]
                    userHash = requestContents.split("?")[7].replace("%20", " ")
                    if userHash in self.activeUsers:
                        username = self.activeUsers[userHash]
                        content_body = changeInfo(newFirstName, newLastName, newCity, newTel, newEmail, newLink, self.__class__.db_conn, username)
                    else:
                        content_body = "You are not logged in.".encode()

                if requestContents.startswith("/ISUSERLOGGEDIN"):
                        # try:
                        #         # if requestContents.split("?")[1] in self.__class__.activeUsers:
                        #         #         print("HASH ",self.activeUsers[requestContents.split("?")[1]])
                        #         #         content_body = "USERLOGGEDINSUCCESS".encode()
                        #         # else:
                        #         #         content_body = "USERLOGGEDINFAIL".encode()
                        #         userHash = self.__class__.activeUsers[requestContents.split("?")[1]]
                        print("requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers", requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers)
                        if requestContents.split('?')[1].replace('%20', ' ') in self.activeUsers:
                                content_body = "USERLOGGEDINSUCCESS".encode()
                        else:
                        # except Exception as e:
                                content_body = "USERLOGGEDINFAIL".encode()

                if requestContents.startswith("/NEWAUCTION"):
                        #print (requestContents)
                        receivedName = requestContents.split ("?")[1]
                        receivedCategory = requestContents.split ("?")[2]
                        receivedPicture = requestContents.split ("?")[3]
                        receivedPrice = requestContents.split ("?")[4]
                        receivedStartD = requestContents.split ("?")[5]
                        receivedEndD = requestContents.split ("?")[6]
                        receivedDesc = requestContents.split ("?")[7]
                        receivedFabCountry= requestContents.split ("?")[8]
                        receivedFabYear = requestContents.split ("?")[9]
                        receivedCondition = requestContents.split ("?")[10]
                        receivedMaterial = requestContents.split ("?")[11]
                        receivedColor = requestContents.split ("?")[12]
                        receivedSpecialCarac = requestContents.split ("?")[13]
                        receivedUsernameHash = requestContents.split("?")[14].replace("%20", " ")
                        receivedUsername = self.__class__.activeUsers[receivedUsernameHash]
                        content_body = newAuction (receivedUsername,receivedName, receivedCategory, receivedPicture, receivedPrice, receivedStartD, receivedEndD, receivedDesc, receivedFabCountry, receivedFabYear, receivedCondition, receivedMaterial, receivedColor, receivedSpecialCarac, self.__class__.db_conn)


                        #print(requestContents,requestContents.startswith("/NEWAUCTION"))

                if requestContents.startswith("/GETSIMPLESEARCHRESULTS"):
                    itemName = requestContents.split("?")[1]
                    content_body = simpleSearch(itemName, self.__class__.db_conn)

                return content_type, content_body


def run():
        print('starting server...')

        server_address = ('127.0.0.1', 8081)

        httpd = HTTPServer(server_address, TestHTTPServerRequestHandler)

        print('running server...')
        httpd.serve_forever()


run()
