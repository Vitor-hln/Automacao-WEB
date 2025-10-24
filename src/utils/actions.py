# Ações genéricas (clicar, digitar, etc.)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def clicar(driver, by, value, timeout=10):
        
    try:
    
        elemento_clicavel = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
            )
            
        elemento_clicavel.click()
        
    except Exception as e:
        print(f"❌ {e} ❌")

    return None

def digitar(driver, by, value, text, timeout=10):
    
    try:

        campo_digitavel = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
            )
        campo_digitavel.send_keys(text)
        
    except Exception as e:
        print(f"❌{e}❌")

    return None

def clicar_por_texto(driver, texto, timeout=10):
    wait = WebDriverWait(driver, timeout)
    try:
        botao = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[.//span[contains(., '{texto}')]]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
        driver.execute_script("arguments[0].click();", botao)
        print(f"✅ Botão '{texto}' clicado com sucesso!")
    except Exception as e:
        print(f"❌ Falha ao clicar no botão '{texto}': {e}")