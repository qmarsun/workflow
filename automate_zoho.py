from urllib.request import DataHandler
import requests
import json
import os
import sys
import glob
#def test():
#https://www.zoho.com/crm/developer/docs/api/v2/auth-request.html

def cleanup():
    dir=r"C:\Users\KumarSundaram\Downloads\self_client*.json"
    print(dir)
    for file in glob.glob(dir):
        print(f"removing the file {file}")
        os.remove(file)

def get_token():
    filepath=r"C:\Users\KumarSundaram\Downloads\self_client.json"
    f = open(filepath)
    data=json.load(f)
    f.close()
    return data


def insert_records():
    import requests
    import json

    url = 'https://www.zohoapis.com/crm/v2/Leads'

    headers = {
    'Authorization': 'Zoho-oauthtoken 1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be',
    }

    #headers =  {"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656472923084,"client_id":"1000.J6BMS9G17IDORUIU6L2Q1CEH93J3NX","client_secret":"8727c049c0d3966137e51f9b573d07a5bab79f8c73","code":"1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be","grant_type":"authorization_code"}

    
#1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be

    request_body = dict()
    record_list = list()

    record_object_1 = {
        'Company': 'Zylker',
        'Email': 'p.daly@zylker.com',
        'Last_Name': 'Daly',
        'First_Name': 'Paul',
        'Lead_Status': 'Contacted',
    }

    record_object_2 = {
        'Last_Name': 'Dolan',
        'First_Name': 'Brian',
        'Email': 'brian@villa.com',
        'Company': 'Villa Margarita'
    }

    record_list.append(record_object_1)

    record_list.append(record_object_2)

    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))
    print('response ',response)
    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())

#insert_records()


def get_refresh_access_token(key):
    print(key)
    apiUrl = "https://accounts.zoho.com/oauth/v2/token"
    r = requests.post(url=apiUrl, data=key )
    print(r)
    print('gen tocken', r.json())
    response=r.json()
    accesss_token = response["access_token"]
    refresh_token = response["refresh_token"]
    print(f'access tokenn {accesss_token}')
    print(f'refrsh token {refresh_token}')
    return(accesss_token,refresh_token)

#/////////////// main
#cleanup()
key=get_token()
#download the api key
#https://api-console.zoho.com/
print(key)
print(get_refresh_access_token(key))
sys.exit(0)
#///////////////////////////////
#   
