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

        print driver.title
        print driver.current_url
        balance=driver.find_element_by_xpath("/html/body/div[3]/header/nav/div[2]/ul[2]/li[1]/div/div/span[2]")
        print balance.text
        driver.get("http://krmct002.kartrocket.com/addorder/linked?redirect_url=")
        driver.implicitly_wait(60)

        driver.find_element_by_id("form_order_id").send_keys(timestr)

        select = Select(driver.find_element_by_name('channel_id'))
        select.select_by_visible_text("MANUAL")


        driver.find_element_by_id("form_first_name").send_keys("autotester")
        driver.find_element_by_id("form_last_name").send_keys("lastname")
        driver.find_element_by_id("form_email").send_keys("autotester@test.com")
        driver.find_element_by_id("form_mobile").send_keys("9999999999")
        driver.find_element_by_id("form_address_1").send_keys("autotester-1")


        select=Select(driver.find_element_by_id("form_region"))
        select.select_by_value("1483")


        driver.find_element_by_id("form_city").send_keys("Delhi")
        driver.find_element_by_id("form_post_code").click()
        driver.find_element_by_id("form_post_code").send_keys("110059")


        
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()

        
        
        #(driver.find_element_by_id("warehouse")).click()
        #select.select_by_value("object:1503")
        driver.find_element_by_name("order_items.0.name").send_keys("product1")
        #.find_element_by_css_selector("#viewallorder > div.content.ng-valid.ng-valid-maxlength.ng-valid-pattern.ng-valid-required.ng-valid-date.ng-dirty.ng-valid-parse > div > div.panel.panel-default > div.panel-wrapper > div > div:nth-child(6) > div > div > div:nth-child(1) > div > table > tbody > tr > td:nth-child(1) > div > input").send_keys("product1")
        driver.find_element_by_id("form_enter_sku").send_keys("123456")
        driver.find_element_by_id("form_enter_hsn").send_keys("12345")
        driver.find_element_by_id("form_enter_qty").send_keys("1")
        driver.find_element_by_id("form_enter_price").send_keys("555")
        driver.find_element_by_name("weight").send_keys("0.45")
        driver.find_element_by_name("length").send_keys("10")
        driver.find_element_by_name("breadth").send_keys("11")
        driver.find_element_by_name("height").send_keys("13")
        select=Select(driver.find_element_by_id("form_payment_method"))
        select.select_by_value("COD")
        driver.find_element_by_id("form_add_order").click()

        #current_url=driver.current_url
        #print current_url
        
        
        #shipnow
        driver.find_element_by_css_selector("#ordertable > tbody > tr:nth-child(1) > td:nth-child(10) > div > button").click()
        
        # ship button
        element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/button")))
        element.click()
        print element.text
        
        #driver.implicitly_wait(60)

 
        element=WebDriverWait(driver,10).until (EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.modal-body.pb0.pl0.pr0.file-wrapper > div.row.mv-lg.text-center > button.btn.btn-sm.ph-xl.btn-blue.mr-lg")))
        element.click()
        print element.text

        
        driver.implicitly_wait(60)



       
        
       







        #driver.close()
          
        

