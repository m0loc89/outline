from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DocumentPage(BasePage):
    NEW_DOC_BUTTON = (By.XPATH, "//button[contains(., 'New document')]")
    TITLE_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='Title']")
    
    def crear_documento(self, titulo):
        self.wait.until(EC.element_to_be_clickable(self.NEW_DOC_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.TITLE_INPUT)).send_keys(titulo)