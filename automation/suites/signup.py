from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import xlrd
import time



#add chromedriver path 
driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("http://krmct002.kartrocket.com/register")
driver.implicitly_wait(30)
driver.maximize_window()

# read data from excel
book = xlrd.open_workbook("/home/ankkur/Desktop/sigupdata.xls") # in my case the directory contains the excel file named excel.xls
sheet=book.sheet_by_index(0)
row=sheet.nrows
print row-1

timestr = time.strftime("%Y%m%d-%H%M%S")
time1=time.strftime("%H%M%S%m%d")
mobile=time1
print mobile


with open('/home/ankkur/Desktop/'+timestr+'_login'+'.csv', 'a') as the_file:
    for i in range(1,row):
        firstname= (sheet.cell_value(i,0))
        lastname= (sheet.cell_value(i,1))
        company=(sheet.cell_value(i,2))
        #email1=(sheet.cell_value(i,3))
        email='ankur.pandey+'+timestr+'@kartrocket.com'
        password1=(sheet.cell_value(i,4))
        password=(str(password1).rstrip('.0'))
        #mobile1=(sheet.cell_value(i,5))
        #mobile=(str(mobile1).rstrip('.0'))
        #mobile=timestr


        #print (firstname +' '+ password )
        driver.implicitly_wait(10)
        
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys(firstname)
       
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys(lastname)

        driver.find_element_by_name("company_name").clear()
        driver.find_element_by_name("company_name").send_keys(company)
        
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        
        driver.find_element_by_id("signUp").click()


# assert for mobile number pop up
        wait=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,("mobile"))))
        driver.find_element_by_name("mobile").send_keys(mobile)
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector("body > div.wrapper.ng-scope > div > div.content.register-bg.pv-xl.ng-scope > div > div > div.col-md-4 > div:nth-child(2) > div > div > form > div:nth-child(2) > div > div > div > button").click()
        
        

        try:
            print "hello"
        except:
            #the_file.write(username +',' + password  +',' + 'fail\n')
            print "lost" 
            
        