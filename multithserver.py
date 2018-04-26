#!/bin/env python
import threading
import os
import sys
try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

server = ThreadingSimpleServer(('', port), SimpleHTTPRequestHandler)
try:	
	print("serving at port %s" %port)
	httpd = threading.Thread(target=server.serve_forever())
	httpd.daemon = True
	httpd.start()
    	
except KeyboardInterrupt:
			server.server_close()
			print("Finished")

        
