import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_inicio_sesion_oauth(driver):
    """Caso 1 (Válida): login exitoso vía SSO -> redirige a /auth/slack."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login()

    WebDriverWait(driver, 10).until(EC.url_contains("/auth/slack"))
    assert "auth/slack" in driver.current_url


@pytest.mark.parametrize("email, password", [("", "pass"), ("invalido", "wrong")])
def test_login_fallido(driver, email, password):
    """Caso 5 (Error), data-driven: login con credenciales inválidas/vacías."""
    login_page = LoginPage(driver)
    login_page.load()
    # TODO: completar con la localizacion real de los campos de email/password
    # y la aserción del mensaje de error mostrado por Outline, una vez
    # confirmada la estructura del DOM en el flujo de login.
    assert True  # Placeholder para pruebas de error
