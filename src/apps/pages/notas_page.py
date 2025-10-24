# Importa suas funções de ação
from utils import actions 
# Imports do Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InserirNotas:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    
    def processar_disciplina(self,disciplina):
        

        actions.digitar(((self.driver,By.ID, "291")))
        actions.clicar(((self.driver, By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/table/tbody/tr[1]/td[9]/div/button/span/i")))
        actions.clicar(((self.driver, By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[2]")))
        
        actions.procurar_elemento(self.driver,
                                  by=By.CSS_SELECTOR,
                                  value="input[placeholder='Buscar por código ou nome']",
                                  action="digitar",
                                  text=disciplina)
        
        
        