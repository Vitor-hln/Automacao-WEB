# Ações genéricas (clicar, digitar, etc.)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def clicar(driver, by, value, timeout=10):
        
    try:
    
        elemento_clicavel = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
            )
            
        elemento_clicavel.click()
        
    except Exception as e:
        print("❌ Elemento nao encontrado ❌")

    return None

def digitar(driver, by, value, text, timeout=10):
    
    try:

        campo_digitavel = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
            )
        campo_digitavel.send_keys(text)
        
    except Exception as e:
        print("❌ Campo digitavel não encontrado ou não pode ser digitado ❌")

    return None

def procurar_elemento(driver, by, value, timeout=10):
    
    try:

        procura = WebDriverWait(driver, timeout).ultil(
            EC.presence_of_element_located((by,value))
        )
        procura.click()

    except Exception as e:
        print("❌ A procura Falhou ❌\n ❌ Elemento não encontrado! ❌")
        
    return None

        