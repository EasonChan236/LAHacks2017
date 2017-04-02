import time
import simplejson
import BaseHTTPServer
import videoGenerationAPI
import urlparse


HOST_NAME = 'localhost'
PORT_NUMBER = 8293 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_POST(self):
        self._set_headers()
        print self.__dict__
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print self.data_string
        args = urlparse.parse_qs(self.data_string)

        videoGenerationAPI.generateSentenceVideo(args["text"][0], "output", args["language"][0], args["sex"][0])

        self.send_header("Location:", "http://13.88.30.233:8000/video.html")

        #f = open("video.html")
        #self.wfile.write(f.read())
        return
    

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
