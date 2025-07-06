from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = FastAPI()

@app.get("/")
def healthcheck():
    return {"status": "API funcionando"}

@app.get("/preco-banana")
def get_banana_price():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        # Corrigido: agora com Service + ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        url = "https://www.paodeacucar.com/produto/152956/banana-nanica-granel-800g-(aprox--3-a-4-unid)"
        driver.get(url)

        wait = WebDriverWait(driver, 15)
        price_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'TextComponent') and contains(text(), 'R$')]"))
        )

        preco_str = price_element.text.replace("R$", "").replace(",", ".").strip()
        preco_float = float(preco_str)

        driver.quit()
        return {"preco": preco_float}
    except Exception as e:
        return {"erro": str(e)}
