from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
time.sleep(30)

a=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/label/input")
a.click()
a.send_keys("Manasa"+Keys.ENTER)

b=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]")#this finds message type field
for i in range(5):
	b.click()
	time.sleep(3)
	string="Again"
	time.sleep(5)
	b.send_keys(string+Keys.ENTER)