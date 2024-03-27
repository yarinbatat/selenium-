# Tip calc orig
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file://C:/Users/USER/PycharmProjects/DevOps1302/tip_calc/index.html")
sleep(2)
billamt = dr.find_element(by="id", value="billamt")
# dr.find_element(By.ID, value="billamt").send_keys("100")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[4]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQuality").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
#sleep(10)
expected = "8"
assert expected == actual
time.sleep(10)

