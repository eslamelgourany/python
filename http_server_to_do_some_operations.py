import http.server
import socketserver
import cgi
from urllib.parse import urlparse

import random

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        # get params send as data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                        'CONTENT_TYPE':self.headers['Content-Type'],
            })


        query_dict = {key: form.getvalue(key) for key in form.keys()}
        min.append(int(query_dict["min_value"]))
        max.append(int(query_dict["max_value"]))
        num.append(int(query_dict["num_values"]))

        # prepare response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(("NEW CONFIG SAVED"+str(query_dict)).encode())

    def do_GET(self):
        """Respond to a GET request."""
        if self.path in ["/config" or "/config/"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html_form = """
    
            <form method="post" action="/">
                Minimum value : <input type="text" name="min_value"><br>
                Maximum value : <input type="text" name="max_value"><br>
                Number of values: <input type="text" name="num_values"><br>
                <input type="submit" value="SUBMIT">
                <img src ="https://4.bp.blogspot.com/-n_Rbq-EbrUI/VYpnO3LaPoI/AAAAAAAAB5M/pE6BVeJANCs/s1600/Good%2BLuck%2B%25287%2529.jpg"/>
    
            """
            self.wfile.write(html_form.encode())

        elif self.path == "/":
             self.send_response(200)
             self.send_header("Content-type", "text/html")
             self.end_headers()
             lst = list()
             for i in range(int(num[0])):
                 lst.append(str(random.randint(min[0], max[0])))
             self.wfile.write(" ".join(lst).encode())
min = []
max = []
num = []

PORT = 8000
ADDRESS = "147.32.90.148"

httpd = socketserver.TCPServer((ADDRESS, PORT), MyRequestHandler)

print("Serving at port", PORT)
httpd.serve_forever()