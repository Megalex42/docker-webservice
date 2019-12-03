#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import urllib
import pymongo

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}\n".format(self.path).encode('utf-8'))
        #respond to getTasks, and then send the tasks
        if self.path == "/getTasks":
            logging.info("Getting tasks")
            #using db as alias for the db in docker compose file
            client = pymongo.MongoClient("mongodb://db:27017/")
            db = client["bcit"] 
            col = db["tasks"]
            for row in col.find():
                string = str(row) + "\n"
                self.wfile.write(string.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}\n".format(self.path).encode('utf-8'))
        #responds to addTask. split parameters and then insert
        data = post_data.decode('utf-8')
        if self.path == "/addTask":
            logging.info("Adding a task")
            title=""
            description=""
            start_date=""
            end_date=""
            priority=""
            category=""
            status=""
            qsl = urllib.parse.parse_qsl(data)
            for text in qsl:
                if (text[0] == "title"):
                    title = text[1]
                if (text[0] == "description"):
                    description = text[1]
                if (text[0] == "start_date"):
                    start_date = text[1]
                if (text[0] == "end_date"):
                    end_date = text[1]
                if (text[0] == "priority"):
                    priority = text[1]
                if (text[0] == "category"):
                    category = text[1]
                if (text[0] == "status"):
                    status = text[1]
            logging.info("Adding: title=" + title + \
                        ", description=" + description + \
                        ", start_date=" + start_date + \
                        ", end_date=" + end_date + \
                        ", priority=" + priority + \
                        ", category=" + category + \
                        ", status=" + status)
            #using db as alias for the db in docker compose file
            client = pymongo.MongoClient("mongodb://db:27017/")
            db = client["bcit"] 
            col = db["tasks"]
            entry = {"title": title, "description": description, "start_date": start_date, "end_date": end_date, "priority": priority, "category": category, "status": status }
            row = col.insert_one(entry)
            logging.info("inserted @ " + str(row.inserted_id))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()