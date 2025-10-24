# Página princial da plataforma
# Até disciplinas
from utils.actions import clicar, digitar,clicar_por_texto
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class pagina_principal:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def acessar_disciplinas(self):
        clicar(self.driver, By.XPATH, "//div[contains(text(), 'Acadêmico')]")
        clicar(self.driver, By.XPATH, "//a[@href='/plataforma/academic/course']")

    def selecionar_filtros(self):
        clicar(self.driver, By.XPATH, "//button[contains(., 'Filtros')]")
        clicar(self.driver, By.ID, "list-courses-more-filters-status")
        clicar(self.driver, By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[3]/aside/div[1]/div/div[2]/label[2]/div/div/div/div[1]/div[1]/div[3]")
        
        for i in range(2):
            try:
                clicar(self.driver, By.XPATH, "/html/body/div[5]/div/div/div[1]/div[2]/div/div")
            except:
                pass
        
        clicar_por_texto(self.driver, "Aplicar filtros")
       
    
        
