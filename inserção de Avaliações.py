import pandas as pd

import dotenv

import time

import os

import pyautogui as pa

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains







dotenv.load_dotenv(r"C:\Users\vitor\Documents\UNIG\Automação\.env")

login = os.getenv("login")

senha = os.getenv("senha")





df = pd.read_excel(r"C:\Users\vitor\Documents\UNIG\Automação\Inserção de Avaliações.xlsx")

index_inicial = 288





# Inicialização

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



# Maximiza a janela

driver.maximize_window()



# Abre o site

driver.get("https://avauni.grupoa.education/plataforma/auth/signin/")





# Função para dimimnuir escrita do código

web = WebDriverWait(driver, 20)





def clicar_quando_pronto(driver, locator):

    wait = WebDriverWait(driver, 20)

    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading-page")))

    element = wait.until(EC.element_to_be_clickable(locator))

    driver.execute_script("arguments[0].click();", element)







#----------------------------------------------------------------------#



# Mapeia a pagína de login



#Login

web.until(

 EC.presence_of_element_located((By.NAME, "field-username"))

).send_keys(login)



# Senha                                            

web.until(

 EC.presence_of_element_located((By.NAME, "field-password"))

).send_keys(senha)



# Entrar

web.until(

    EC.element_to_be_clickable((By.NAME, "btn-login"))

).click()







#Mapeia a pagina principal

# Clica em academico

web.until(

    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Acadêmico')]"))

).click()



# Clica em Disciplinas

web.until(

    EC.element_to_be_clickable((By.XPATH, "//a//div[contains(text(), 'Disciplinas')]"))

).click()





# Espera a pagina carregar

# Clica em Filtros

clicar_quando_pronto(driver, (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[3]/button"))





# Status

web.until(

    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[3]/asIDe/div[1]/div/div[2]/label[2]/div/div/div/div[1]/div[1]/div[3]"))

).click()





# Clica 2 vezes para selecionar "Ativo"

for i in range(2):

    try:

        web.until(

            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[1]/div[2]/div/div"))

        ).click()

    except:

        pass

print()

   

# Aplicar filtros

web.until(

    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aplicar filtros')]"))

).click()





for index in df.loc[317:423:1].index:

   

    codigo = df.loc[index, "Nome"]

    print(f"Processando disciplina: {codigo}")

   

    aba_principal = driver.current_window_handle



    # buscar a disciplina e clicar para abrir a nova aba...

    placeholder_locator = (By.CSS_SELECTOR, "input[placeholder='Buscar por código ou nome']")

    disciplina = web.until(EC.element_to_be_clickable(placeholder_locator))

    disciplina.send_keys(Keys.CONTROL, "a")

    disciplina.send_keys(Keys.BACKSPACE)

    disciplina.send_keys(codigo)



    web.until( # 3 pontos

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/table/tbody/tr[1]/td[9]/div/button/span/i"))

    ).click()



   

    web.until( # Grade de notas

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[2]"))

    ).click()

   

    # Troca o foco para a nova aba

    nova_aba = driver.window_handles[-1]

    driver.switch_to.window(nova_aba)

   

    #Adicionar novo bloco - AD

    web.until(

    EC.element_to_be_clickable((By.CSS_SELECTOR, "button i.mdi-plus"))

    ).click()

   

    #TITULO

    web.until(

        EC.element_to_be_clickable((By.ID, "input-73"))

    ).send_keys("AD")

   

    #Codigo Externo

    web.until(

        EC.element_to_be_clickable((By.ID, "input-77"))

    ).send_keys("AD")

   

    #SALVAR

    web.until(

        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Salvar')]]"))

    ).click()

   

    time.sleep(2)

   

   

   

    #Adicionar novo bloco - AI

    web.until(

    EC.element_to_be_clickable((By.CSS_SELECTOR, "button i.mdi-plus"))

    ).click()

   

    #TITULO

    web.until(

        EC.element_to_be_clickable((By.ID, "input-73"))

    ).send_keys("AI")

   

    #Codigo Externo

    web.until(

        EC.element_to_be_clickable((By.ID, "input-77"))

    ).send_keys("AI")

   

    #SALVAR

    web.until(

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[3]/button[2]"))

    ).click()

   

   

    # Fecha primeira pagina de nota

    # Define o localizador específico

    fechar_button_locator = (By.XPATH, "//div[contains(@class,  'v-toolbar__title') and contains(., 'Fechar')]/  preceding-sibling::button")  



    time.sleep(1)

    web.until(

        EC.element_to_be_clickable(fechar_button_locator)

        ).click()

   

# Abre Opções de Nota final





    # 1. Localizador preciso para o CABEÇALHO da coluna que contém o texto "3ª Nota"

    nota_header_locator = (By.XPATH, "//th[.//span[contains(text(), '3ª Nota')]]")

   

    # Encontra o elemento do cabeçalho

    nota_header = web.until(EC.presence_of_element_located(nota_header_locator))



    # 2. Move o mouse para cima do cabeçalho da nota para revelar o menu

    ActionChains(driver).move_to_element(nota_header_element).perform()



    # 3. Localizador para o botão DENTRO do cabeçalho que acabamos de focalizar

    # O ponto no início (.//) garante que ele procure apenas DENTRO do nota_header_element

    three_dots_in_header_locator = (By.XPATH, ".//button[contains(@class, 'mdi-dots-vertical')]")

   

    # Espera o botão ficar visível e clicável DEPOIS de passar o mouse

    three_dots_button = web.until(

        EC.element_to_be_clickable(three_dots_in_header_locator)

    )

   

    # Clica no botão de três pontos correto

    three_dots_button.click()

   

    # 4. Agora que o menu está aberto, clica na opção desejada (ex: "Fórmula nota final")

    # Use um localizador baseado no texto da opção, é mais seguro.

    formula_option_locator = (By.XPATH, "//*[contains(@class, 'v-list-item__title') and contains(text(), 'Fórmula nota final')]")



    web.until(

        EC.element_to_be_clickable(formula_option_locator)

    ).click()

   

    time.sleep(2)

# FORMULA



    # Abre parenteses

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--abrir-parênteses"))

    ).click()



    # AD

    web.until(

        EC.element_to_be_clickable((By.ID, "variable--1ª-ad"))

    ).click()

   

    # +

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--adição"))

    ).click()

   

    # Abre parenteses

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--abrir-parênteses"))

    ).click()

   

    # AI

    web.until(

        EC.element_to_be_clickable((By.ID, "variable--2ª-ai"))

    ).click()

   

    # *

    web.until(

        EC.element_to_be_clickable((By.ID, 'arithmetic--multiplicação'))

    ).click()    

   

    # valor

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--valor"))

    ).click()    

   

    # 2

    web.until(

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[7]/div/div/div/div/div/div/input"))

    ).send_keys("2")

   

    # Fecha Parênteses 2 vezes

    for i in range(2):

        try:

            web.until(

                EC.element_to_be_clickable((By.ID, "arithmetic--fechar-parênteses"))

            ).click()

           

        except:

            pass



    # Divisão  

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--divisão"))

    ).click()

   

    # Valor

    web.until(

        EC.element_to_be_clickable((By.ID, "arithmetic--valor"))

    ).click()

   

    # 3

    web.until(

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[11]/div/div/div/div/div/div/input"))

    ).send_keys("3")

   

    #ValIDar Formula

    time.sleep(1.5)

    web.until(

        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[1]/div[2]/div/div[1]/div/div[3]/button[1]"))

    ).click()

   

    time.sleep(1.5)

    # valIDa e salva

    web.until(

        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space() = 'Validar e salvar fórmula']"))

    ).click()

   

    time.sleep(1.5)

    # Fecha pagina

    # Define o localizador específico

    fechar_button_locator = (By.XPATH, "//div[contains(@class,  'v-toolbar__title') and contains(., 'Fechar')]/  preceding-sibling::button")  



    time.sleep(1.5)

    web.until(

        EC.element_to_be_clickable(fechar_button_locator)

        ).click()

   

    time.sleep(10)

   

    driver.close()

   

    driver.switch_to.window(aba_principal)

   

    # --- FIM DA CORREÇÃO PARTE 3 ---



    # Agora o loop pode recomeçar com segurança, pois o foco está na página correta.

    print(f"Disciplina '{codigo}' processada com sucesso. Voltando para a lista.")