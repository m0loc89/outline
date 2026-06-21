import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_inicio_sesion_oauth(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()
    
    # Validamos la redirección (Éxito)
    WebDriverWait(driver, 10).until(EC.url_contains("/auth/slack"))
    assert "auth/slack" in driver.current_url

@pytest.mark.parametrize("email, password", [("", "pass"), ("invalido", "wrong")])
def test_login_fallido(driver, email, password):
    login_page = LoginPage(driver)
    login_page.load()
    # Aquí puedes añadir lógica para probar campos de texto si los tuvieras
    assert True # Placeholder para tus pruebas de error

def test_creacion_documento(driver):
    # Aquí iría tu lógica de DocumentPage
    assert True 

def test_titulo_largo(driver):
    assert True

def test_caso_frontera(driver):
    assert True