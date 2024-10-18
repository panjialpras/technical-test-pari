import json
from http.server import BaseHTTPRequestHandler
from models import get_all_categories, get_all_items, get_item, create_category, create_item, update_item, delete_item
from utils import send_json_response, send_error_response

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            send_json_response(self, 200, {'message': 'Hello, World!'})
        elif self.path == '/categories':
            categories = [{'id': cat[0], 'name': cat[1]} for cat in get_all_categories()]
            send_json_response(self, 200, categories)
        elif self.path == '/items':
            items = [{'id': itm[0], 'category_id': itm[1], 'name': itm[2], 'description': itm[3], 'price': itm[4]} for itm in get_all_items()]
            send_json_response(self, 200, items)
        elif self.path.startswith('/items/'):
            try:
                item_id = int(self.path.split('/')[-1])
                data = get_item(item_id)
                if data:
                    item = {'id': data[0], 'category_id': data[1], 'name': data[2], 'description': data[3], 'price': data[4]}
                    send_json_response(self, 200, item)
                else:
                    send_error_response(self, 404, 'Item not found')
            except ValueError:
                send_error_response(self, 400, 'Invalid item ID')
        else:
            send_error_response(self, 404, 'Not Found')

    def do_POST(self):
        if self.path == '/categories':
            category_data = self._get_json_data()
            if category_data:
                create_category(category_data.get('name'))
                send_json_response(self, 201, {'status': 'Category added'})
        elif self.path == '/items':
            item_data = self._get_json_data()
            if item_data:
                create_item(item_data['category_id'], item_data['name'], item_data['description'], item_data['price'])
                send_json_response(self, 201, {'status': 'Item created successfully'})
        else:
            send_error_response(self, 404, 'Not Found')

    def do_PUT(self):
        if self.path.startswith('/items/'):
            try:
                item_id = int(self.path.split('/')[-1])
                item_data = self._get_json_data()
                if item_data:
                    update_item(item_id, item_data['name'], item_data['description'], item_data['price'])
                    send_json_response(self, 200, {'message': 'Item updated'})
            except ValueError:
                send_error_response(self, 400, 'Invalid request')

    def do_DELETE(self):
        if self.path.startswith('/items/'):
            try:
                item_id = int(self.path.split('/')[-1])
                delete_item(item_id)
                send_json_response(self, 200, {'message': 'Item deleted'})
            except ValueError:
                send_error_response(self, 400, 'Invalid request')

    def _get_json_data(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            return json.loads(post_data)
        except json.JSONDecodeError:
            send_error_response(self, 400, 'Invalid JSON')
            return None
