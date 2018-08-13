import requests,json
import xlrd,time
from termcolor import colored
from colorama import Fore, Back, Style



CRED = '\033[91m'
CEND = '\033[0m'
CGREEN= '\033[32m'

# read data from excel
book = xlrd.open_workbook("/home/ankkur/Desktop/testdata.xls") # in my case the directory contains the excel file named excel.xls
sheet=book.sheet_by_index(0)
row=sheet.nrows
print row-1
timestr = time.strftime("%Y%m%d-%H%M%S")
#print timestr

url = "http://krmct000.kartrocket.com/"

login=url+"v1/auth/login"


with open('/home/ankkur/Desktop/'+timestr+'_login'+'.csv', 'a') as the_file:

    for i in range(1,row):
        email= (sheet.cell_value(i,0))
        password1= (sheet.cell_value(i,1))
        password=(str(password1).rstrip('.0'))
        

        payload=json.dumps({"email":email,"password":password})

        print payload
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
                }

    
        response_login = requests.post(login, data=payload, headers=headers)
        status=str(response_login.status_code)
        text=  ((response_login.json()))
        
        if (response_login.status_code==200):
            the_file.write( email +',' + password  +',' + 'the test case has passed'+','+status +','+'\n')
            
            print ("passed\n")
            token="Bearer"+' '+text["token"]
            #print token
            get_order=url+"v1/orders/processing"
            headers = {'Authorization':token}
         
            # GET ALL ORDERS
            order=requests.get(get_order, headers=headers)
            processing_order=(order.json())
            #print("<<<<<<<<<<  Running GET ALL ORDERS API   >>>>>>>>>>> ")
            
            if (order.status_code==200):

                #print processing_order
                print (CGREEN+"Total Number of products = " + str(processing_order["meta"]["pagination"]["total"])+CEND)
            else:

                print (CRED+"Error in api " +" " +  get_order + " " + processing_order["message"]+CEND)
                #print (processing_order["message"])

# GET BALANCE 

                balance_api=url+"v1/courier/applied_weight"
                headers = {'Authorization':token}

                balance=requests.get(balance_api,headers=headers)
                user_balance=balance.json()
                if (balance.status_code==200):
                    print (CGREEN+"api " + balance_api+ " " + " is " + "passed  and "+ "took"+ " " + str(balance.elapsed.total_seconds())+ "seconds" +CEND)
                    print ("Balance amount"+ str(user_balance["data"]["response"]["balance_amount"] ) )           
                else:
                    print (CRED+"Error in api " +" " +  balance_api + "is" + balance["message"]+CEND)  


#GET ALL DETAILS 

            order_detail=url+"v1/orders/show/12224"
            headers = {'Authorization':token}
            detail=requests.get(order_detail, headers=headers)
            detail_orders=(detail.json())
            #print detail_orders
            #print("<<<<<<<<<<  Running GET ORDER DETAILS API   >>>>>>>>>>> \n")
            #print ("The api responded with " +str( detail.status_code)+  "  "+ "status")
            if (detail.status_code==200):
                print (CGREEN+"api " + order_detail + " " + " is " + "passed  and "+ "took"+ " " + str(detail.elapsed.total_seconds())+ "seconds" +CEND)
                
                
            else:
                print (CRED+"Error in api " +" " +  detail + "is" + detail_orders["message"]+CEND)  
           # print ("Total Number of products = " + str(processing_order["meta"]["pagination"]["total"]))


# FETCH ORDERS

            

#overview api 

            overview_api=url+"v1/dashboard/overview"
            headers = {'Authorization':token}
            overview=requests.get(overview_api,headers=headers)
            if(overview.status_code==200):
                print(CGREEN+"api" + " " + overview_api+ "" + "is passed and took "   + str(overview.elapsed.total_seconds()) +CEND )
            else: 

                print (CRED+"Error in api " +  overview_api  +" "  +CEND)
         

# product api 

            products_api=url+"v1/dashboard/top/products"
            headers = {'Authorization':token}
            product=requests.get(overview_api,headers=headers)
            if(product.status_code==200):
                print(CGREEN+"api" + " "+ products_api+ " " + "is" + " passed and took "   + str(product.elapsed.total_seconds()) +CEND )
            else: 

                print (CRED+"Error in api " + products_api  +" "  +CEND)

#orders count

            order_count_api=url+"v1/orders/count"
            headers = {'Authorization':token}
            order_count=requests.get(order_count_api,headers=headers)
            #print order_count.status_code   
            if(order_count.status_code==200):
                
                print(CGREEN+"api" + " "+ order_count_api+ " " + "is" + " passed and took "   + str(order_count.elapsed.total_seconds()) +CEND )
   
        
            
            else:

                print (CRED+"Error in api " + order_count_api  +" "  +CEND)
            
        else:
            print ("failed with "+' ' +str(response_login.status_code))
            
            the_file.write( email +',' + password  +',' + 'the test case has failed'+','+status +'\n')
     