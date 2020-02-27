# simple http server, guide followed
# from geeksradarhq.

from http.server import BaseHTTPRequestHandler, HTTPServer

#htttp handler request
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #send response status code
        self.send_response(200)

        #send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        #send message back to client
        message = "hello world"
        #write as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return 

def run():
    print('starting server...')
    # server settings
    server_address = ('127.0.0.1', 8081)
    htttpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    htttpd.serve_forever()

run()