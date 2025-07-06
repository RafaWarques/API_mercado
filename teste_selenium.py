from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_binary = r"C:\chromefortesting\chrome-win64\chrome.exe"
chromedriver_path = r"C:\chromefortesting\chromedriver-win64\chromedriver.exe"

chrome_options = Options()
chrome_options.binary_location = chrome_binary
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.paodeacucar.com/produto/152956/banana-nanica-granel-800g-(aprox--3-a-4-unid)")

wait = WebDriverWait(driver, 15)
price_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'TextComponent') and contains(text(), 'R$')]"))
)

preco_str = price_element.text.replace("R$", "").replace(",", ".").strip()
preco_float = float(preco_str)

driver.quit()
print(f"Preço da banana: R$ {preco_float:.2f}")
