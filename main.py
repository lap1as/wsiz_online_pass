from config import password,login
from selenium import webdriver as WB
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time




driver = WB.Chrome(service=ChromeService(ChromeDriverManager().install()))

def login_wsiz(username, password,browser):
    """login"""
    driver.get("https://wu.wsiz.edu.pl/Home/Index")
    driver.find_element(By.ID, 'UserLogin_I').send_keys(username)
    driver.find_element(By.ID, 'Password_I').send_keys(password, Keys.ENTER)
   
def getting_webex_link(browser):
    """getting webex lesson"""
    driver.find_element(By.CLASS_NAME, "info").click()
    driver.find_element(By.CSS_SELECTOR, "#Scheduler_aptsBlock_AptDiv4 > table > tr > td.schedule-webex-image-agenda > div").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#AptToolTipWebex").click()
    time.sleep(4)

def main():
    login_wsiz(login,password,driver)
    getting_webex_link(driver)


if __name__ == "__main__":
    main()

"""
popup id AptToolTipWebex

"""