import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from flask import Flask, request
import tempfile
import time
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/webhook/send-teams-task', methods=['POST'])
def send_message():
    data = request.get_json()
    task = data.get("task")
    assignee = data.get("assignee")
    deadline = data.get("deadline")
    email = data.get("email")
    
    #setup chrome so don't have to log in everytime
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=/Users/vietnguyen/selenium-profile-1")
    chrome_options.add_argument("--profile-directory=Profile 1")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no--sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver,20)
    
    try:
        driver.get("https://teams.microsoft.com")
        sleep(5)
        
        #load cookies from previous session before opening Teams
        try:
            with open("/Users/vietnguyen/Desktop/teams_cookies.pkl","rb") as cookie_file:
                cookies = pickle.load(cookie_file)
                for cookie in cookies:
                    driver.add_cookie(cookie)
            driver.get("https://teams.microsoft.com")
        except Exception as e:
            print("Warning: Could not load cookies:",e)

       # Navigate to Teams main chat page
        driver.get("https://teams.microsoft.com/_#/chat")
        sleep(8)

        #Locate Ray's existing chat
        chat_xpaths = [
            '//span[contains(text(), "Ray .")]',
            '//div[contains(@data-tid, "chat-list")]//span[contains(text(), "Ray .")]',
            '//button[contains(@aria-label, "Ray .")]',
        ]

        # Wait for chat list sidebar to load and search for "Ray"
        try:
            ray_chat = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Ray ."]')))
            ray_chat.click()
            print(" Opened existing chat with Ray.")
        except Exception as e:
            raise Exception(" Could not find Ray in chat list. Make sure Ray is pinned or recently chatted.") from e

        sleep(5)
        
        # Wait for the message box and click
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
        ActionChains(driver).move_to_element(message_box).click().perform()
        sleep(1)
       
        # Format and send the message
        formatted_message = f"Task: {task}\nAssigned to: {assignee}\nDeadline: {deadline}"
        for line in formatted_message.split('\n'):
            message_box.send_keys(line)
            message_box.send_keys(Keys.SHIFT, Keys.ENTER)
            sleep(0.2)
                    
        message_box.send_keys(Keys.RETURN)
        print("Message sent successfully.")
        sleep(2)    
    except Exception as e:
        print("Error sending message:",e)
        raise e
            
    finally:
        driver.quit()
            
    return {"status": "Message sent"}, 200

if __name__=='__main__':
    app.run(port=5001)
#   app.run(host="0.0.0.0", port=5001)