import requests,json
import xlrd,time



login=url+"v1/auth/login"
payload=json.dumps({"email":"ankur.pandey+stage@kartrocket.com","password":"123456"})
headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
                }

    
response_login = requests.post(login, data=payload, headers=headers)
status=str(response_login.status_code)
print status
text=  ((response_login.json()))
token="Bearer"+' '+text["token"]
print token




def get(self,api_url):
    balance_api=url+"v1/courier/applied_weight"
    headers = {'Authorization':token}

    balance=requests.get(balance_api,headers=headers)
    user_balance=balance.json()
    if (balance.status_code==200):
        print (CGREEN+"api " + balance_api+ " " + " is " + "passed  and "+ "took"+ " " + str(balance.elapsed.total_seconds())+ "seconds" +CEND)
        print ("Balance amount"+ str(user_balance["data"]["response"]["balance_amount"] ) )           
    else:
        print (CRED+"Error in api " +" " +  balance_api + "is" + balance["message"]+CEND