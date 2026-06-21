import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Fixture que inicializa el WebDriver de Chrome antes de cada prueba
    y garantiza su cierre correcto al finalizar, evitando fugas de recursos.

    Se ejecuta en modo headless porque el pipeline de GitHub Actions
    no cuenta con entorno gráfico.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()
