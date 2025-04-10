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

    fname = "Ayan"
    lname= "Khan"
    uname = "ayan123"
    myemail = "ak@gmail.com"
    pwd = "1234"

    # Example Web Test (Google Search)
    driver.get("http://127.0.0.1:8000/signup")

    time.sleep(2)  # Wait for page to load

    firstname = driver.find_element(By.ID, "firstname")
    time.sleep(1) # Pause to see the filled-out form before submission
    lastname = driver.find_element(By.ID, "lastname")
    time.sleep(1) 
    username = driver.find_element(By.ID, "username")
    time.sleep(1) 
    email = driver.find_element(By.ID, "email")
    time.sleep(1) 
    password = driver.find_element(By.ID, "password")
    time.sleep(1) 

    print(f"Name entered: {fname} {lname}") 
    print(f"Email entered: {myemail}")

    # Enter user data
    firstname.send_keys(fname)
    print(f"Entered first name: {fname}")

    lastname.send_keys(lname)
    print(f"Entered last name: {lname}")

    username.send_keys(uname)
    print(f"Entered username: {uname}")

    email.send_keys(myemail)
    print(f"Entered email: {myemail}")

    password.send_keys(pwd)
    print(f"Entered password: {pwd}")

    # Locate and click submit button
    submit_button = driver.find_element(By.ID, "submit")
    print("Located 'Submit' button.")

    submit_button.click()
    print("Clicked the 'Submit' button.")

    time.sleep(2)  # Wait for results to load

    # Confirm successful submission
    print("Signup form submitted. Waiting for response...")

except Exception as e:
    print(f"Error during the test: {e}")

finally:
    driver.quit()
    print("WebDriver closed.")