from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/adize/Desktop/DevOps%20Course/tip_calc/tip_calc/index.html")

billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys(100)

s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()

# stam adding shit for git to notice
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys(5)

driver.find_element(by="id", value = "calculate").click()

expected = "2.00"
actual = driver.find_element(by="id", value = "tip").text

if expected == actual:
    print("tip calc safe")
else:
    print("problem with tip calc")

sleep(5)
driver.close()