from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome options
chrome_options = Options()

# Uncomment the next line to run in headless mode
# chrome_options.add_argument("--headless")

# Set the path to the chromedriver executable
service = Service("chromedriver.exe") 

try:
    # Start the Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Example Web Test (Google Search)
    driver.get("http://127.0.0.1:8000/login") 
    print(f"Navigated to {driver.current_url}")

    time.sleep(2)  # Wait for page to load


    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("ayan9")
    password.send_keys("ayan9")

    # Find the search button and click
    submit_button = driver.find_element(By.ID, "submit")
    time.sleep(1)

    submit_button.click()
    print("Login form submitted.")

    time.sleep(3)  # Wait for results to load

    # cart  
    cartbtn = driver.find_element(By.ID, "cartbtn")
    cartbtn.click()
    print("cart button clicked.")

    time.sleep(3)  # Wait for results to load    

except Exception as e:
    print(f"Error during the test: {e}")

finally:
    driver.quit()
    print("WebDriver closed.")