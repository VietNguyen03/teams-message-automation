from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle 
import time

options = Options()
options.add_argument("--user-data-dir=/Users/vietnguyen/selenium-profile-temp")

driver = webdriver.Chrome(options=options)
driver.get("https://teams.microsoft.com")

time.sleep(20)

#saved cookies
cookies = driver.get_cookies()
with open("teams_cookies.pkl","wb") as file:
    pickle.dump(cookies,file)

print("Cookies saved successfully.")
driver.quit()