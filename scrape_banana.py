from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Caminhos atualizados conforme seu ambiente
chrome_binary = r"C:\chromefortesting\chrome-win64\chrome.exe"
chromedriver_path = r"C:\chromefortesting\chromedriver-win64\chromedriver.exe"

chrome_options = Options()
chrome_options.binary_location = chrome_binary
# chrome_options.add_argument("--headless")  # DESATIVE durante debug
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=chromedriver_path)

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.paodeacucar.com/produto/152956/banana-nanica-granel-800g-(aprox--3-a-4-unid)")

    wait = WebDriverWait(driver, 15)

    # Espera por um <p> com a classe identificada
    price_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'TextComponent') and contains(text(), 'R$')]"))
)


    # Extrai e limpa o texto
    preco_str = price_element.text.replace("R$", "").replace(",", ".").strip()
    preco_float = float(preco_str)

    driver.quit()
    print(json.dumps({"preco_banana": preco_float}))

except Exception as e:
    driver.quit()
    print(json.dumps({"erro": str(e)}))
