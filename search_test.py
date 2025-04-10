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
    driver.get("http://127.0.0.1:8000/")
    print(f"Navigated to {driver.current_url}")

    time.sleep(2)  # Wait for page to load

    # Find the search box and enter a query
    search_query = driver.find_element(By.ID, "searchbox")
    print("Search box located successfully.")

    search_query.send_keys("iphone")
    print("Search query 'iphone' entered.")

    # Find the search button and click
    submit_button = driver.find_element(By.ID, "searchbtn")
    time.sleep(1)
    print("Search button located successfully.")

    submit_button.click()
    print("Search submitted.")

    time.sleep(3)  # Wait for results to load

    # Retrieve and print search results (example: product titles)
    search_results = driver.find_elements(By.CLASS_NAME, "product_title")  # Adjust the class name as per your HTML
    if search_results:
        print("Search Results:")
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}. {result.text}")
    else:
        print("No search results found.")

except Exception as e:
    print(f"Error during the test: {e}")

finally:
    driver.quit()
    print("WebDriver closed.")