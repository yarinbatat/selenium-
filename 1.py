from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

time.sleep(3)

chromedriver_path = r"C:\Users\USER\PycharmProjects\DevOps1302\Selenium\chromedriver_win32"


# Create Chrome options object
options = Options()
options.add_argument("executable_path=" + chromedriver_path)

# Initialize the Chrome webdriver
driver = webdriver.Chrome(options=options)


# driver.get("http://google.com")
# print("url:" + driver.current_url)
# time.sleep(2)
# driver.refresh()
# driver.close()

driver.get("file://C:/Users/USER/PycharmProjects/DevOps1302/tip_calc/index.html")
# time.sleep(2)
# driver.find_element(by="id", value="peopleamt").send_keys("50")
# time.sleep(5)

# driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[2]").click()
# time.sleep(5)