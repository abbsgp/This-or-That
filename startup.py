# server.py
import http.server
import os
import socketserver # Our http server handler for http requests
import threading

FRONTEND_PORT = 8000
BACKEND_PORT = 5000
IPADDRESS = "127.0.0.1"

def runbackend():
    os.system("cd backend && uvicorn server:app --reload --host "+str(IPADDRESS)+" --port "+str(BACKEND_PORT))
    #uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")
    
try:
    t1 = threading.Thread(target=runbackend)
    t1.start()
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((IPADDRESS, FRONTEND_PORT), Handler) as httpd:
        httpd.serve_forever()

except Exception as E:
    t1.join()
    print ("\033[91mError: Shutdown occuring.\033[00m")
    print (E)
    
except KeyboardInterrupt:
    t1.join()
    print ("\033[91mServer Shutdown By User\033[00m")