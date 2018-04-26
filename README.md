# Multithreaded-PyServer
Multithreaded python server used to serve files in a directory.Threading is used to support request from multiple clients,a new thread is created whenever a new client connects.This is can be modified by creating new processes instead of threads for process management and socket management like which process opens which socket and how much data it is transmitting etc.

**Usage**: python multithserver.py port_number /path/to/directory/

**Requirements:-**
              **1**.socketserver(Python 3.*) or SocketServer(Python 2.7)
              **2**.http.server(Python 3.*) or BaseHTTPServer(Python 2.7)
              
All the above packages comes pre-installed with respective python versions.

**For more details:-**
https://docs.python.org/3/library/socketserver.html
https://docs.python.org/3/library/http.server.html
https://docs.python.org/2/library/socketserver.html
https://docs.python.org/2/library/basehttpserver.html
