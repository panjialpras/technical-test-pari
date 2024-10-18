import json

def send_json_response(handler, status_code, data):    
    handler.send_response(status_code)
    handler.send_header('Content-Type', 'application/json')
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode())

def send_error_response(handler, status_code, message):
    send_json_response(handler, status_code, {'error': message})
