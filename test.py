import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json


# this will persist the session cookies automatically for us
session = requests.Session()
#retry = Retry(connect=3, backoff_factor=0.5)
#adapter = HTTPAdapter(max_retries=retry)
#session.mount('http://', adapter)
response = session.get('http://oscar-assignment.appspot.com/oscarapi/v1/mymodel/1/')
string = response.content.decode('utf-8')
json_obj = json.loads(string)
print(json_obj)

"""
response

{"date_created": "2019-04-26T02:20:20.693574", "first_name": "Name", "hash": "504138882", "id": 1, "is_default_for_billing": false, "is_default_for_shipping": false, "last_name": "Rani", "line1": "GITA college,Badaraghunathpur,Janla", "line2": "Bhubaneshwar", "line3": "", "line4": "Bhubaneshwar", "notes": "", "num_orders_as_billing_address": 0, "num_orders_as_shipping_address": 0, "phone_number": "+919162801813", "postcode": "752054", "resource_uri": "/oscarapi/v1/mymodel/1/", "search_text": "Name Rani GITA college,Badaraghunathpur,Janla Bhubaneshwar Bhubaneshwar Odisha 752054 Republic of India", "state": "Odisha", "title": "Miss"}
"""

data={
	'first_name': "Aapnik",
	'last_name': "empty"
}
response1 = session.put('http://127.0.0.1:8000/oscarapi/v1/put_request/1/', data=data)
print(response1.content)

"""
New response (GET request)

{'date_created': '2019-04-26T02:20:20.693574', 'first_name': 'Aapnik', 'hash': '92110107', 'id': 1, 'is_default_for_billing': False, 'is_default_for_shipping': False, 'last_name': 'empty', 'line1': 'GITA college,Badaraghunathpur,Janla', 'line2': 'Bhubaneshwar', 'line3': '', 'line4': 'Bhubaneshwar', 'notes': '', 'num_orders_as_billing_address': 0, 'num_orders_as_shipping_address': 0, 'phone_number': '+919162801813', 'postcode': '752054', 'resource_uri': '/oscarapi/v1/mymodel/1/', 'search_text': 'Aapnik empty GITA college,Badaraghunathpur,Janla Bhubaneshwar Bhubaneshwar Odisha 752054 Republic of India', 'state': 'Odisha', 'title': 'Miss'}

"""

