import http.server
from handlers import RequestHandler

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()
