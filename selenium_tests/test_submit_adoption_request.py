from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open Login Page
driver.get("http://127.0.0.1:8000/accounts/login/")

time.sleep(2)

# Login
driver.find_element(By.NAME, "username").send_keys("public_test_01")
driver.find_element(By.NAME, "password").send_keys("PawsConnectTest123!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)

# Open Adoption Home
driver.get("http://127.0.0.1:8000/rescue/adoption/")

time.sleep(2)

# Click Browse Available Animals
driver.find_element(By.LINK_TEXT, "Browse Available Animals").click()

time.sleep(2)

# Click View Details (Bobby)
view_button = driver.find_element(By.LINK_TEXT, "View Details")

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    view_button
)

time.sleep(2)

view_button.click()

time.sleep(2)

# Enter Adoption Request Message
driver.find_element(By.NAME, "message").send_keys(
    "I would like to adopt Bobby and provide him with a safe home, regular veterinary care, nutritious food, daily exercise, and lifelong love and attention."
)

time.sleep(2)

# Submit Adoption Request
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    submit_button
)

time.sleep(2)

submit_button.click()

time.sleep(3)

# Check Result
if "/rescue/my-adoption-requests/" in driver.current_url.lower():
    print("===================================")
    print("ADOPTION REQUEST TEST RESULT: PASS ✅")
    print("Adoption request submitted successfully.")
    print("===================================")
else:
    print("===================================")
    print("ADOPTION REQUEST TEST RESULT: FAIL ❌")
    print("Adoption request was not submitted.")
    print("Current URL:", driver.current_url)
    print("===================================")

time.sleep(3)

driver.quit()