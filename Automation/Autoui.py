from selenium import webdriver
import os
from datetime import datetime

# List of resolutions and devices
resolutions = {
    "Desktop": [(1920, 1080), (1366, 768), (1536, 864)],
    "Mobile": [(360, 640), (414, 896), (375, 667)]
}

# List of browsers
browsers = ["Chrome", "Firefox"]

# Function to capture screenshot
def capture_screenshot(browser, resolution, url, device):
    driver = getattr(webdriver, browser)()
    driver.set_window_size(*resolution)
    driver.get(url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_path = f"{device}/{resolution[0]}x{resolution[1]}"
    os.makedirs(folder_path, exist_ok=True)
    driver.save_screenshot(f"{folder_path}/{timestamp}.png")
    driver.quit()

# URL to sitemap
sitemap_url = "https://www.getcalley.com/page-sitemap.xml"

# Parse sitemap and extract URLs
# Code for parsing sitemap is not included here

# Iterate over resolutions, devices, and browsers
for device, resolutions_list in resolutions.items():
    for resolution in resolutions_list:
        for browser in browsers:
            capture_screenshot(browser, resolution, sitemap_url, device)
