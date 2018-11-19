from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import xlrd,unittest
import time,math
from selenium.webdriver.remote.webelement import WebElement





#add chromedriver path 
driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("http://krmct002.kartrocket.com/login")
driver.implicitly_wait(30)
driver.maximize_window()

class Auth():
    def login(self,readFile):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        time1=time.strftime("%H%M%S%m%d")
        order_id=time1

    



    # read data from excel
        book = xlrd.open_workbook(readFile) # in my case the directory contains the excel file named excel.xls
        sheet=book.sheet_by_index(0)
        row=sheet.nrows
        print row-1

        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open('/home/ankkur/Desktop/'+timestr+'_login'+'.csv', 'a') as the_file:

            for i in range(1,row):
                username= (sheet.cell_value(i,0))
                password1= (sheet.cell_value(i,1))
                password=(str(password1).rstrip('.0'))
                print (str(password1).rstrip('.0'),username)

                driver.implicitly_wait(10)

            try:
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/form/div[1]/input").clear()
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/form/div[1]/input").send_keys(username)
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/form/div[2]/input").clear()
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/form/div[2]/input").send_keys(password)
                    driver.find_element_by_css_selector("button[type=submit]").click()
                    driver.implicitly_wait(10)
                    
                    elem1=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"type-header")))
                    print elem1.text
                    assert elem1.text=='Welcome to Shiprocket'
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    print driver.current_url
                    print driver.title

                    driver.find_element_by_id("app.processing").click()
                    print driver.current_url
                    print driver.title
                    
                    driver.get("http://krmct002.kartrocket.com/addorder/quick?redirect_url=")

            except:
                print Exception