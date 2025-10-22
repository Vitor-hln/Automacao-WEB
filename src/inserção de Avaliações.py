import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import dotenv


dotenv.load_dotenv(r"C:\Users\vitor\Documents\UNIG\Automação\.env")
login = os.getenv("login")
senha = os.getenv("senha")


df = pd.read_excel(r"C:\Users\vitor\Documents\UNIG\Automação\Automacao-WEB\src\data\Inserção de Avaliações.xlsx")
index_inicial = 288


# Inicialização 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abre o site
driver.get("https://avauni.grupoa.education/plataforma/auth/signin/")


web = WebDriverWait(driver, 10)

#Mapeia a pagína de login


#Login
web.until(
 EC.presence_of_element_located((By.NAME, "field-username"))
).send_keys("vitor.nascimento")

# Senha                                             
web.until(
 EC.presence_of_element_located((By.NAME, "field-password"))
).send_keys("@VEaa19102024")

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

# Clica em Filtros
web.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[3]/button"))
).click()

# Status
web.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[3]/aside/div[1]/div/div[2]/label[2]/div/div/div/div[1]/div[1]/div[3]"))
).click()


# Clica 2 vezes para selecionar "Ativo"
for i in range(2):
    try:
        web.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[1]/div[2]/div/div"))
        ).click()
    except:
        pass
print("Ta ok")
    
# Aplicar filtros
web.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aplicar filtros')]"))
).click()


for index in df.loc[index_inicial:288].index:

    codigo = df.loc[index, "Nome"]

    busca_field = web.until( # Campo do nome da disciplina
        EC.element_to_be_clickable((By.ID, "291"))
    )
    
    busca_field.send_keys(codigo)
    
    web.until( # 3 pontos
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/main/div/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/table/tbody/tr[1]/td[9]/div/button/span/i"))
    ).click()

    web.until( # Grade de notas
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/div/div[2]"))
    ).click()