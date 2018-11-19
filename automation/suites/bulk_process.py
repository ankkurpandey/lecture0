from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import xlrd
import time,math
from selenium.webdriver.remote.webelement import WebElement




timestr = time.strftime("%Y%m%d-%H%M%S")
time1=time.strftime("%H%M%S%m%d")
order_id=time1

#add chromedriver path 
driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("http://krmct002.kartrocket.com/login")
driver.implicitly_wait(30)
driver.maximize_window()



# read data from excel
book = xlrd.open_workbook("/home/ankkur/Desktop/testdata.xls") # in my case the directory contains the excel file named excel.xls
sheet=book.sheet_by_index(0)
row=sheet.nrows
print row-1

timestr = time.strftime("%Y%m%d-%H%M%S")


with open('/home/ankkur/Desktop/'+timestr+'_login'+'.csv', 'a') as the_file:

    for i in range(1,row):
        username= (sheet.cell_value(i,0))
        password1= (sheet.cell_value(i,1))
        password=(str(password1).rstrip('.0'))
        print str(password1)

        driver.implicitly_wait(60)

    
        #driver.find_element_by_class_name("account_email").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(username)
        #driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/form/div[2]/input").clear()
        driver.find_element_by_name("account_password").send_keys(password)
        driver.find_element_by_css_selector("button[type=submit]").click()
        driver.implicitly_wait(60)
        elem1=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.panel-body.bb0.pt-xl.ph-xl.pb.ng-scope > div > button")))
        #print elem1.text
       
       
       
       
        #elem=driver.find_element_by_css_selector("body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.panel-body.bb0.pt-xl.ph-xl.pb.ng-scope > div > button")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print driver.current_url
        print driver.title

        driver.get("http://krmct002.kartrocket.com/orders/processing?page=1&perPage=15&shop=&ids=")
        driver.implicitly_wait(60)


        # Bulk Shipment 

        driver.get("http://krmct002.kartrocket.com/orders/manifests?page=1&perPage=100")
        driver.implicitly_wait(10)
        
        elem1=WebDriverWait(driver,10).until(EC.presence_of_element_located((driver.find_element_by_id("//*[@id=ordertable]/thead/tr/th[1]"))))
        print elem1.text()

        #print(driver.find_element_by_id("//*[@id=ordertable]/thead/tr/th[1]").text())

        
        
        
        
        
        
        
        
        
        
        
        
        
        #elem1=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.wrapper.ng-scope > section > div > div > div.header-wrapper > div.pull-right.navbar-right.ml > div.pull-right.upload-file.pfx.ng-scope > div.fileupload.button.fileupload-new.mr-sm.pfx.ng-scope > span.btn.btn-default.upload.pfx")))
        #driver.execute_script("arguments[0].click();", elem1)

        
        #elem2 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.modal-body.pb0.file-wrapper.ng-scope > div:nth-child(1) > div.bootstrap-filestyle.input-group > span > label > span"))) 
        #driver.execute_script("arguments[0].click();", elem2)
        
        
        
        
       # elem2=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.modal-body.pb0.file-wrapper.ng-scope > div:nth-child(1) > div.bootstrap-filestyle.input-group > span > label > span")))
        #driver.execute_script("arguments[0].click();", elem2)
        #elem2.click()
        

       # driver.find_element_by_css_selector("body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.modal-body.pb0.file-wrapper.ng-scope > div:nth-child(1) > div.bootstrap-filestyle.input-group > span > label").click()
        
        #driver.find_element_by_css_selector("body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.modal-body.pb0.file-wrapper.ng-scope > div:nth-child(1) > div.bootstrap-filestyle.input-group > span > label > span").send_keys("/home/ankkur/Downloads/order.csv")    
        
        #driver.find_element_by_css_selector("body > div.wrapper.ng-scope > section > div > div > div.header-wrapper > div.pull-right.navbar-right.ml > div.pull-right.upload-file.pfx.ng-scope > div.fileupload.button.fileupload-new.mr-sm.pfx.ng-scope > span.btn.btn-default.upload.pfx").click()
