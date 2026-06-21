from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Selector robusto para el botón de autenticación
    SLACK_LOGIN_BUTTON = (By.XPATH, "//*[contains(text(), 'Slack')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get("http://localhost:3000")

    def login(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        button = self.wait.until(EC.element_to_be_clickable(self.SLACK_LOGIN_BUTTON))
        button.click()