import requests
import json
import urllib3

# Disable warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Function to obtain the token
def get_token(address, user, password):
    url = f"http://{address}/identity-manager/api/v1.0/auth/token"
    headers = {
        "content-type": "application/json"
    }
    payload = {
        "name": user,
        "password": password
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extract the token from the response
    token = response.json().get('access_token')
    if not token:
        raise ValueError("Token not found in response")

    return token

# Function to browse the axes
def browse_data(address, token, group):
    url = f"https://{address}/automation/api/v1.0/{group}/?type=browse"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }


    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()

# Function to get axis value
def get_value(address, token,variable):
    url = f"https://{address}/automation/api/v1.0/{variable}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()


# Function to set axis value
def set_value(address,token, variable, _type, _value):
    url = f"https://{address}/automation/api/v1.0/{variable}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }
    data ={
        "type": _type,
        "value": _value   
    }

    data=data

    response = requests.put(url, data=json.dumps(data),headers=headers, verify=False)

   
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()