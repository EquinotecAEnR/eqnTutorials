import requests
from requests.auth import HTTPBasicAuth

# Replace these with your actual values
url = "http://192.168.1.1/influxdb/api/v2/write?org=734ad6f0b9da802a&bucket=b64001fc2501d809&precision=ns"
token = "VkrvI5kKVRc4MWjLhbnQtxgej2LFZ2yyG6Jz36ZPKrdux0QWwh8HMCUNZ6jtUkubddP9qOc2xpbSDwNgdBY5wA=="
username = "boschrexroth"
password = "boschrexroth"

# Data to be sent
data = """
airSensors,sensor_id=TLM0201 temperature=73.97038159354763,humidity=35.23103248356096,co=0.48445310567793615 1630424257000000000
airSensors,sensor_id=TLM0202 temperature=75.30007505999716,humidity=35.651929918691714,co=0.5141876544505826 1630424257000000000
"""

# Headers
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "text/plain; charset=utf-8",
    "Accept": "application/json"
}

# Making the POST request with Basic Authentication and SSL verification disabled
response = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth(username, password), verify=False)

# Print the response
print("Status Code:", response.status_code)
print("Response Text:", response.text)
