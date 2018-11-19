
import requests,json
from pprint import pprint


company_id=raw_input("enter company_id ")

url = "https://apiv2.shiprocket.in/"

login=url+"v1/auth/login?company_id="+company_id
#   print login
payload=json.dumps({"email":"ankur.pandey+ap@kartrocket.com","password":"fuYtJCBjKfav"})
headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
                }

    
response_login = requests.post(login, data=payload, headers=headers)
status=str(response_login.status_code)
#sprint status
text=  ((response_login.json()))
token="Bearer"+' '+text["token"]
#print token


balance_api=url+"v1/courier/applied_weight"
headers = {'Authorization':token}

balance=requests.get(balance_api,headers=headers)
user_balance=balance.json()
if (balance.status_code==200):
   
    pprint(  balance.json())      
else:
    print ("error")

shipment_api=url+"v1/shipments"
shipment=requests.get(shipment_api,headers=headers)
pprint (shipment.json())


bulk_pickup_api=url+"v1/courier/generate/pickup"
headers = {'Authorization':token}
payload=  {"shipment_id":["2590584"]}
bulk_pickup=requests.post(bulk_pickup_api,payload,headers)

print bulk_pickup.status_code

