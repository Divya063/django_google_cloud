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

data={
	'first_name': "Name"
}
response1 = session.put('http://oscar-assignment.appspot.com/oscarapi/v1/mymodel/1/', data=data)
#print(response.content)
