
import requests
import json
##
#C:\Users\KumarSundaram>python monday_test.py
#<Response [200]>
#{'data': {'boards': [{'id': '2722205215', 'name': 'projectplan'}]}, 'account_id': 12286202}
#<Response [200]>
#{'data': {'boards': [{'items': [{'id': '2722205274', 'name': 'test'}, {'id': '2722205288', 'name': 'task #2'}, {'id': '2722793861', 'name': 'WHAT IS UP MY FRIENDS!'}]}]}, 'account_id': 12286202}
# https://support.monday.com/hc/en-us/articles/360013483119-API-Quickstart-Tutorial-Python

with open('mykey.json') as f:
   data = json.load(f)
print(data)
apiKey = data["apiKey"]
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query2 = '{ boards (limit:100) {id name} }'
data = {'query' : query2}

r = requests.post(url=apiUrl, json=data, headers=headers)
print(r)
print(r.json())

#/////////////////////////// create items
#{'data': {'boards': [{'id': '2722205215', 'name': 'projectplan'}]}, 'account_id': 12286202}
query3 = 'mutation{ create_item (board_id:2722205215, item_name:"WHAT IS UP MY FRIENDS!") { id } }'
data = {'query' : query3}

#r = requests.post(url=apiUrl, json=data, headers=headers) # make request
#print(r.json())

#/// qry
#--data-raw '{"query": "query { boards (ids: 12345678) { name state board_folder_id owner { id }}}"}'
#--data-raw '{"query": "query { boards (ids: 12345678) { name state board_folder_id owner { id }}}"}'

#/////////////////////////// query all items under
query3 = ' { boards (ids: 2722205215) { items {id name }}}'
data = {'query' : query3}
r = requests.post(url=apiUrl, json=data, headers=headers)
print(r)
print(r.json())

##https://api.developer.monday.com/docs/items-queries

