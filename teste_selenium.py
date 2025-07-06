from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_binary = r"C:\chromefortesting\chrome-win64\chrome.exe"
driver_path = r"C:\chromefortesting\chromedriver-win64\chromedriver.exe"

options = Options()
options.binary_location = chrome_binary
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

try:
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")
    print("✅ Título da página:", driver.title)
    driver.quit()
except Exception as e:
    print("❌ Erro ao iniciar o Chrome:")
    print(e)
