import os

from typing import Tuple
from http.server import BaseHTTPRequestHandler, HTTPServer

from Backend.DBController.DBConnection import DBConnection
from Backend.Functions.login import login
from Backend.Functions.profile import getProfileInfo
from Backend.Functions.testSearch import testSearch


class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
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
                content_body = "Error in the dispatch function"

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

                if requestContents.startswith("/GETPROFILEINFO"):
                        userHash = requestContents.split("?")[1].replace("%20", " ")
                        content_body = getProfileInfo(self.__class__.activeUsers[userHash], self.__class__.db_conn)

                return content_type, content_body


def run():
        print('starting server...')

        server_address = ('127.0.0.1', 8081)

        httpd = HTTPServer(server_address, TestHTTPServerRequestHandler)

        print('running server...')
        httpd.serve_forever()


run()
