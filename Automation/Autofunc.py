from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from datetime import datetime
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Function to log in to the web application
def login(username, password, url):
    driver.get(url)
    driver.maximize_window()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputEmail"))).send_keys(username)
        driver.find_element_by_id("inputPassword").send_keys(password)
        driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()
    except TimeoutException:
        print("Login failed: Input fields not found or page not fully loaded within 10 seconds.")

# Function to upload file
def upload_file(file_path):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Inventory')]"))).click()
        time.sleep(2)  # Waiting for page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Upload New Inventory')]"))).click()
        time.sleep(2)  # Waiting for modal to load
        driver.find_element_by_id("inventoryInput").send_keys(file_path)
        time.sleep(2)  # Waiting for upload to complete
    except TimeoutException:
        print("Upload failed: Element not found or page not fully loaded within 10 seconds.")


# Function to capture screenshot
def capture_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshot_{timestamp}.png")

# Function to record video
def record_video():
    # Code to record video using external tool or library
    pass
# URL and login credentials
url = "https://demo.dealsdray.com/"
username = "mis@dealsdray.com"
password = "mis@dealsdray.com"
file_path = "pythonProject/demo-data.xlsx"

# Start Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening browser window)
driver = webdriver.Chrome(options=chrome_options)

# Start Firefox WebDriver
firefox_options = Options()
firefox_options.headless = True  # Run in headless mode
driver = webdriver.Firefox(options=firefox_options)


# Login to the web application
login(username, password, url)

# Upload file
upload_file(file_path)

# Validate page (Add your validation checks here)

# Record video
record_video()

# Capture screenshot of final output
capture_screenshot()

# Quit WebDriver
driver.quit()
