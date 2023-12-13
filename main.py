from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config
from selenium.webdriver.chrome.options import Options
import os
import glob


download_path="C:\\Users\\mdiop\\PycharmProjects\\Sterling project\sterling\\files"

pattern = "*.xlsx"

for fichier in glob.glob(os.path.join(download_path, pattern)):
    os.remove(fichier)
#create options for chrome
options = Options()

prefs = {
    "download.default_directory" : "C:\\Users\\mdiop\\PycharmProjects\\Sterling project\\sterling\\files",
    "download.prompt_for_download": False,
    "download.directory_upgrade":  True,
    "safebrowsing.enabled": True }

options.add_experimental_option("prefs", prefs)
username = ""
password = ""
driver = webdriver.Chrome(options=options)

driver.get("https://www.supply-chain.ibm.com/launch/")

time.sleep(5)

connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Log in']")
connexion_button.click()

time.sleep(5)

username_field = driver.find_element(By.ID, "username")

username_field.send_keys(username)

connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Continue']")
connexion_button.click()

time.sleep(5)

password_field = driver.find_element(By.ID, "password")

password_field.send_keys(password)

connexion_button = driver.find_element(By.XPATH, "//button[text()= 'Log in']")
connexion_button.click()

time.sleep(15)

link1 = driver.find_element(By.LINK_TEXT, "Document Tracking")
link1.click()

time.sleep(15)

window_ids = driver.window_handles
driver.switch_to.window(window_ids[1])
link2 = driver.find_element(By.LINK_TEXT, "SJVO1001")
link2.click()

time.sleep(10)

link3 = driver.find_element(By.LINK_TEXT, "Views")
link3.click()

time.sleep(10)
link4 = driver.find_element(By.LINK_TEXT, "Document Inbox")
link4.click()

time.sleep(10)
link4 = driver.find_element(By.ID, "btnDownload")
link4.click()

time.sleep(10)
link5 = driver.find_element(By.ID, "rdButtonXlsx")
link5.click()

time.sleep(10)
link6 = driver.find_element(By.ID, "Button1")
link6.click()

time.sleep(5)
link7 = driver.find_element(By.ID, "btnReturn")
link7.click()

time.sleep(10)

link8 = driver.find_element(By.LINK_TEXT, "Views")
link8.click()

time.sleep(10)
link9 = driver.find_element(By.LINK_TEXT, "Document Outbox")
link9.click()

time.sleep(10)
link10 = driver.find_element(By.ID, "btnDownload")
link10.click()

time.sleep(10)
link11 = driver.find_element(By.ID, "rdButtonXlsx")
link11.click()

time.sleep(10)
link12 = driver.find_element(By.ID, "Button1")
link12.click()

time.sleep(5)
link13 = driver.find_element(By.ID, "btnReturn")
link13.click()
#download_button = driver.find_element(By.XPATH, "//button[text()= 'Download Document Inbox View")
#download_button.click()
time.sleep(50)
driver.quit()





