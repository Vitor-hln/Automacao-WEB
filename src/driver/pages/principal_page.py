# Página princial da plataforma
# Até disciplinas
from driver import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class pagina_principal:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def acessar_disciplinas(self):
        actions.clicar(self.driver, By.XPATH, "//div[contains(text(), 'Acadêmico')]")
        actions.clicar(self.driver, By.XPATH, "//a[contains(text(), 'Disciplinas')]")

    def selecionar_filtros(self):
        actions.clicar(self.driver, By.XPATH, "//button[contains(., 'Filtros')]")
        actions.clicar(self.driver, By.ID, "list-courses-more-filters-status")
        actions.clicar(self.driver, By.CSS_SELECTOR, ".vue-treeselect__option-label")
