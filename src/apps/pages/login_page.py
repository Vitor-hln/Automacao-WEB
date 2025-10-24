# Logar na conta a ser utilizada
from apps.driver import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LogarUsuario:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def logar(self, login, senha):
        actions.digitar(self.driver, By.NAME, "field-username", login)
        actions.digitar(self.driver, By.NAME, "field-password", senha)
        actions.clicar(self.driver, By.NAME, "btn-login")
