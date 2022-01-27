from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	# def do_GET(self):
	# 	self.send_response(200)
	# 	self.headers['Content-Type'] = 'text/html; charset=UTF-8'
	# 	self.end_headers()
	# 	self.wfile.write(b'Hello, world!')



	def do_GET(self):

		self.send_response(200)

		with open('chat_history.json') as json_file:    

			data = json.load(json_file)

			json_to_pass = json.dumps(data)

			self.send_response(code=200, message='here is your data')
			self.send_header(keyword='Content-type', value='application/json')
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()
			self.wfile.write(json_to_pass.encode('utf-8'))

	# def do_POST(self):
	# 	content_length = int(self.headers['Content-Length'])
	# 	body = self.rfile.read(content_length)
	# 	self.send_response(200)
	# 	self.end_headers()
	# 	response = BytesIO()
	# 	response.write(b'This is POST request. ')
	# 	response.write(b'Received: ')
	# 	response.write(body)
	# 	self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()