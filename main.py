from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.options import Options
import os
import glob

# Set the download path
download_path = "C:\\Users\\"

# Specify the pattern to delete existing .xlsx files
pattern = "*.xlsx"
for fichier in glob.glob(os.path.join(download_path, pattern)):
    os.remove(fichier)  # Delete each file

# Create options for Chrome
options = Options()

# Set preferences for Chrome, including download directory and behavior
prefs = {
    "download.default_directory" : download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade":  True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

# Replace with your username and password
username = ""
password = ""

# Initialize WebDriver with options
driver = webdriver.Chrome(options=options)

# Open the target URL
driver.get("https://www.supply-chain.ibm.com/launch/")
time.sleep(5)  # Wait for the page to load

# Find and click the login button
connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Log in']")
connexion_button.click()
time.sleep(5)

# Input username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(username)

# Proceed to the next login step
connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Continue']")
connexion_button.click()
time.sleep(5)

# Input password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Finalize the login
connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Log in']")
connexion_button.click()
time.sleep(15)

# Navigate through the website to access and download documents
# Replace the following 'link' and 'button' click operations with actual navigational steps as per the website

# Close the browser after the operations
time.sleep(50)  # Wait for downloads to complete
driver.quit()
