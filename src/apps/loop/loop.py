from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.actions import clicar, digitar,clicar_por_texto
import time

class looper:
    def __init__(self, driver):
        self.driver = driver

    def acessar_disciplinas(self, disciplina):
        try:
            campo_digitavel = WebDriverWait(self.driver, 10). until(
                EC.element_to_be_clickable((By.ID, "291"))
            )
            campo_digitavel.clear()
            campo_digitavel.send_keys(disciplina)
        # teste de limpar campo
       # campo_digitavel(Keys.CONTROL, "a")   
       # campo_digitavel(Keys.BACKSPACE)       
         
            # 3 pontos
            clicar(self.driver, By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/main/div/    div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/table/tbody/tr[1]/td[9]/   div/ button/span/i") 
            # Grade de notas
            clicar(self.driver,By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[2]")
        except Exception as e:
            print(f"{e}")
        
    def adicionar_notas(self):
        # Troca o foco para a nova aba
        driver = webdriver.Chrome()
        nova_aba = driver.window_handles[-1]
        driver.switch_to.window(nova_aba)    
        
        # Adicionar notas de AD
        clicar(self.driver,By.CSS_SELECTOR, "button i.mdi-plus")
        digitar(self.driver, By.ID, "input-73", 'AD')
        digitar(self.driver, By.ID, "input-77", 'AD')
        clicar_por_texto(self.driver, "Salvar")
        
        # Adiciona notas de AI
        clicar(self.driver,By.CSS_SELECTOR, "button i.mdi-plus")
        digitar(self.driver, By.ID, "input-73", 'AD')
        digitar(self.driver, By.ID, "input-77", 'AD')
        clicar_por_texto(self.driver, "Salvar")
        
        #fecha a aba de notas
        clicar_por_texto(self.driver, "Fechar")
    
    def abrir_menu_formula_nota_final(self, timeout=10):

        try:
            wait = WebDriverWait(self.driver, timeout)

            # 1. Localiza o cabeçalho da coluna "3ª Nota"
            nota_header_locator = (By.XPATH, "//th[.//span[contains(text(), '3ª Nota')]]")
            nota_header = wait.until(EC.presence_of_element_located(nota_header_locator))

            # 2. Move o mouse para cima do cabeçalho para revelar o menu
            ActionChains(self.driver).move_to_element(nota_header).perform()

            # 3. Localiza o botão de três pontos dentro do cabeçalho
            three_dots_locator = (By.XPATH, ".//button[contains(@class, 'mdi-dots-vertical')]")
            three_dots_button = wait.until(EC.element_to_be_clickable(three_dots_locator))

            # 4. Clica no botão de três pontos
            three_dots_button.click()

            # 5. Localiza e clica na opção "Fórmula nota final"
            formula_option_locator = (By.XPATH, "//*[contains(@class, 'v-list-item__title') and     contains(text(), 'Fórmula nota final')]")
            formula_option = wait.until(EC.element_to_be_clickable(formula_option_locator))
            formula_option.click()

            print("Opção 'Fórmula nota final' selecionada com sucesso!")

        except Exception as e:
            print(f"Erro ao abrir o menu da coluna '3ª Nota': {e}")
    
    def inserir_formula(self):
        
        # Insere a formula final nos campos
        clicar(self.driver, By.ID, "arithmetic--abrir-parênteses")
        clicar(self.driver, By.ID, "variable--1ª-ad")
        clicar(self.driver, By.ID, "arithmetic--adição")
        clicar(self.driver,By.ID, "arithmetic--abrir-parênteses")
        clicar(self.driver,By.ID, "variable--2ª-ai")
        clicar(self.driver,By.ID, 'arithmetic--multiplicação')
        clicar(self.driver,By.ID, "arithmetic--valor")
        
        digitar(self.driver,By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[7]/div/div/div/div/div/div/input", "2")
        
        for i in range(2):
            try:
                clicar(self.driver,By.ID, "arithmetic--fechar-parênteses")
            except:
                pass
            
        clicar(self.driver,By.ID, "arithmetic--divisão")
        clicar(self.driver,By.ID, "arithmetic--valor")
        
        digitar(self.driver,By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[11]/div/div/div/div/div/div/input")
        
    def validar_formula(self):
        
        clicar(self.driver,By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[1]/div/div[3]/button[1]")
        
        clicar(self.driver,By.XPATH, "//button[normalize-space() = 'Validar e salvar fórmula']")
        
        clicar(self.driver, By.XPATH, "//div[contains(@class,  'v-toolbar__title') and contains(., 'Fechar')]/  preceding-sibling::button")
        time.sleep(6)
        
    
        
        
        
    