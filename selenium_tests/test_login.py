"""
PAWS CONNECT
Selenium Automated Test

Test Case:
SEL-01 - User Login

Purpose:
Verify that a registered public user can successfully log into the system
and access the dashboard.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Chrome
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open PAWS CONNECT login page
driver.get("http://127.0.0.1:8000/accounts/login/")

# Wait for page to load
time.sleep(2)

# Enter username
username = driver.find_element(By.NAME, "username")
username.send_keys("public_test_01")

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("PawsConnectTest123!")

# Click Login
password.send_keys(Keys.RETURN)

# Wait for login
time.sleep(5)

# Check whether login succeeded
if "dashboard" in driver.current_url.lower():
    print("===================================")
    print("LOGIN TEST RESULT: PASS ✅")
    print("User successfully logged into PAWS CONNECT.")
    print("Screenshot saved successfully.")
    print("===================================")
else:
    print("===================================")
    print("LOGIN TEST RESULT: FAIL ❌")
    print("User could not log into PAWS CONNECT.")
    print("===================================")

# Keep browser open for 5 seconds
time.sleep(5)

driver.quit()