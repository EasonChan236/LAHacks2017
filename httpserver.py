import time
import simplejson
import BaseHTTPServer
import videoGenerationAPI
import urlparse
import webGenAPI
import searchAPI
import simplejson as json


HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8293 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()




#POST TO POST TEXT/URL
    def do_POST(self):
        self._set_headers()
        print self.__dict__
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print self.data_string
        args = urlparse.parse_qs(self.data_string)
	print args

        #GET TO SEARCH
        if("search" in self.path):
            res = searchAPI.search(args["searchText"][0])
            print res
            self.wfile.write(json.dumps([{"title":t, "url":u} for t , u in res]))
        elif("weburl" in self.path):
            webGenAPI.generateVideoFromURL(args["text"][0], "output", args["language"][0], args["sex"][0])
            self.wfile.write('<script>location="http://13.88.30.233:8000/video.html";</script>')
        else:
            videoGenerationAPI.generateSentenceVideo(args["text"][0], "output", args["language"][0], args["sex"][0])
            self.wfile.write('<script>location="http://13.88.30.233:8000/video.html";</script>')

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
