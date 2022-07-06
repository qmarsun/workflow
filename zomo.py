import requests
import json

## https://www.zoho.com/invoice/api/v3/oauth/#overview

def insert_records():
    import requests
    import json

    url = 'https://www.zohoapis.com/crm/v2/Leads'
    

    headers = {
    'Authorization': 'Zoho-oauthtoken 1000..',
    }

    #headers =  {"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656472923084,"client_id":"1000.","client_secret":"","code":"1000..","grant_type":"authorization_code"}

   

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

#///////////////////////////////
#     

#stockname, lastclosedprice, date
#adsf, 23.23 20220622
#bcd, 234.34, 20220622
#...
##...
#...
#===========================
#==>
#endofdayprice =
#[
#    {
#        stickname=
#        lastclosedprice
#        date
#    },
#    {
#    }
#]
#//////////////////
# readfile line by line
# eachline split into variable
# varibale insert to arrayofdict values

n_code"}
inputdata = {
        "scope":["ZohoInvoice.fullaccess.all"],
        "expiry_time":1656465804033,
        "client_id":"1000.",
        "client_secret":"",
        "code":"1000..",
        "grant_type":"authorization_code"}
#print(input)
#apiUrl = "https://accounts.zoho.com/oauth/v2/token"
#r = requests.post(url=apiUrl, json=inputdata )
#print(r)
#print(r.json())

apiurl="https://accounts.zoho.com/oauth/v2/auth?"\
"scope=ZohoInvoice.fullaccess.all"\
"&client_id=1000."\
"&state=testing"\
"&response_type=code&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
#print(apiurl)
#r = requests.post(url=apiurl )
#print(r)
#print(r.json())
#with open('zomooutput.html', 'w') as f:
#    f.write(str(r))

# generate access and refresh tokem
#https://accounts.zoho.com/oauth/v2/token?code=1000.dd7e47321d48b8a7e312e3d6eb1a9bb8.b6c07ac766ec11da98bf6a261e24dca4&client_id=1000.0SRSZSY37WMZ69405H3TMYI2239V&client_secret=fb0196010f2b70df8db2a173ca2cf59388798abf&redirect_uri=http://www.zoho.com/invoice&grant_type=authorization_code

#curl "https://www.zohoapis.com/crm/v2/Leads?converted=true&approved=true"
#-X GET
#-H "Authorization: Zoho-oauthtoken 1000.8cb99dxxxxxxxxxxxxx9be93.9b8xxxxxxxxxxxxxxxf"

#1000.cef7bf1a6a4dc8bfe44447581b30bf07.ff117a6cdac8943595405883365833be
apiurl="https://accounts.zoho.com/oauth/v2/token?"\
"gran_type=authorization_code" \
"&client_id=1000."\
"&client_secret="\
"&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
#print(apiurl)
##r = requests.post(url=apiurl )
#print(r)
#print(r.json())

# crm
# campaigns
# connect 
# work drive 
  # (Grant workflow)

#////////////////////
# Quickbooks==>
#///////////////////
#HTML, CSS,Javascript
#Monday, zoho and Quickbooks , local files
#===================

#https://www.zoho.com/crm/developer/docs/api/v2/
#https://www.zoho.com/crm/developer/docs/api/v2/auth-request.html

#//////////////////'a

#https://api-console.zoho.com/

#input_data={"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656589263315,"client_id":"1000.","client_secret":"","code":"1000..","grant_type":"authorization_code"}
input_data={"scope":["ZohoInvoice.fullaccess.all"],"expiry_time":1656617619965,"client_id":"1000.","client_secret":"","code":"1000..","grant_type":"authorization_code"}
apiUrl = "https://accounts.zoho.com/oauth/v2/token"
#r = requests.post(url=apiUrl, json=input_data )
#print(r)
#print(r.json())

apiurl="https://accounts.zoho.com/oauth/v2/token?"\
"gran_type=authorization_code" \
"&client_id=1004."\
"&client_secret="\
"&redirect_uri=http://www.zoho.com/invoice&access_type=offline"
r = requests.post(url=apiUrl, json=input_data )
print(r)
print('token',r.json())a
