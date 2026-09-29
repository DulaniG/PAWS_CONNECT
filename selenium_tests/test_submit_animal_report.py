"""
PAWS CONNECT
Selenium Automated Test

Test Case:
SEL-02 - Submit Animal Report

Purpose:
Verify that a registered public user can successfully submit
a new street animal report.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time

# Start Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open login page
driver.get("http://127.0.0.1:8000/accounts/login/")

time.sleep(2)

# Login
driver.find_element(By.NAME, "username").send_keys("public_test_01")
password = driver.find_element(By.NAME, "password")
password.send_keys("PawsConnectTest123!")
password.send_keys(Keys.RETURN)

time.sleep(5)

# Open Report Animal page
driver.get("http://127.0.0.1:8000/rescue/report/")

time.sleep(2)

# Select animal type
Select(driver.find_element(By.NAME, "animal_type")).select_by_index(1)

# Select animal condition
Select(driver.find_element(By.NAME, "condition")).select_by_index(1)

# Description
driver.find_element(By.NAME, "description").send_keys(
    "Friendly puppy waiting near the bus stop. Appears healthy but alone."
)

# Upload image
image_path = os.path.join(
    os.getcwd(),
    "selenium_tests",
    "test_data",
    "puppy_test.jfif"
)

driver.find_element(By.NAME, "image").send_keys(image_path)

# Latitude
driver.find_element(By.NAME, "latitude").send_keys("6.841200")

# Longitude
driver.find_element(By.NAME, "longitude").send_keys("79.965400")

# Location description
driver.find_element(By.NAME, "location_description").send_keys(
    "Near Kottawa Bus Stand"
)

# Map link
driver.find_element(By.NAME, "map_link").send_keys(
    "https://maps.google.com"
)

# Enter reporter contact phone
driver.find_element(By.NAME, "reporter_contact_phone").send_keys("0771234567")

# Find submit button
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Scroll button into view
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    submit_button
)

time.sleep(2)

submit_button.click()

time.sleep(5)

# Wait for report submission
time.sleep(5)

# Check whether report submission succeeded
if "my-reports" in driver.current_url.lower():
    print("===================================")
    print("ANIMAL REPORT TEST RESULT: PASS ✅")
    print("Animal report submitted successfully.")
    print("===================================")
else:
    print("===================================")
    print("ANIMAL REPORT TEST RESULT: FAIL ❌")
    print("Animal report was not submitted.")
    print("===================================")

time.sleep(5)

driver.quit()