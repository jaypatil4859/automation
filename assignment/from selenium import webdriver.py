from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import logging

#create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#create a file handler
handler = logging.FileHandler("selenium.log")
handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)
logger.addHandler(console_handler)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://atg.party/")

# Check HTTP response code
response = requests.get(driver.current_url)
logger.info(f"HTTP response code: {response.status_code}")

# Log the reponse time
start_time = time.time()
driver.get("https://atg.party/")
end_time = time.time()
logger.info(f"Response time: {start_time - end_time} seconds")

# Click on login
login_button = driver.find_element(By.XPATH, "/html/body/nav/div/div/div/div[2]/div/button[2]").click()

# Fill in the email and password
email = driver.find_element(By.ID, "email_landing")
password = driver.find_element(By.ID, "password_landing")
email.send_keys("wiz_saurabh@rediffmail.com")
password.send_keys("Pass@123")
password.send_keys(Keys.RETURN)

# wait for login to complete and load Create article page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "create-btn-dropdown")))
driver.find_element(By.ID,"create-btn-dropdown").click()
create_article = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/nav/div/div[3]/div/div[1]/div/div/a[1]").click()

# fill in the title and description
title = driver.find_element(By.NAME, "title")

description = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div")

title.send_keys("your title here")
description.send_keys("your description")

#upload a cover image
upload_image = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/input")
upload_image.send_keys("/home/jay/assignment/cover.jpg")

time.sleep(5)
#click on post
post_article = driver.find_element(By.ID, "hpost_btn")
post_article.click()

# Wait for the page to redirect and log the new url
WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

logger.info(f"Redirected to: {driver.current_url}")

# Close the driver
driver.quit() 

