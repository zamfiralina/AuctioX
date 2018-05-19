from http.server import BaseHTTPRequestHandler, HTTPServer

from Backend.DBController.DBConnection import DBConnection


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    db_conn = DBConnection.connect("WEB", "WEB", "localhost")

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # =================================GET==============================================#
    def do_GET(self):
        print(self.db_conn.version())

        if self.path == '/':
            self.path = '/index.html'

        self.path = ".../Frontend" + self.path
        try:
            file_to_open = open(self.path[1:]).read( )
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)

        self.end_headers()

        self.wfile.write (bytes(file_to_open, "utf8"))

    #================================POST=====================================#
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers( )
        #self.wfile.write ("<html><body><h1>POST!</h1></body></html>")
        


def run():
    print('starting server...')

    # Server settings
    server_address = ('127.0.0.1', 8085)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
