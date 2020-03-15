from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class reusableClass:
    @staticmethod
    def initilizeDriver():
        option = Options()
        option.add_argument("--headless")
        global Driver
        Driver = webdriver.Chrome(executable_path="lib/chromedriver.exe", chrome_options=option)
        Driver.maximize_window()
        Driver.implicitly_wait(10)

    def getBaseURL(url):
        Driver.get(url)

    def closeDriver(self):
        Driver.close()

    def enterByID(locator, data):
        Driver.find_element_by_id(locator).send_keys(data)

    def clickByID(locator):
        Driver.find_element_by_id(locator).click()
