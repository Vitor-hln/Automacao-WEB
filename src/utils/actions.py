from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# ✅ Clicar com fallback via JavaScript
def clicar(driver, by, value, timeout=10):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        elemento.click()
    except Exception as e:
        print(f"❌ Erro ao clicar normalmente: {e}")
        try:
            elemento = driver.find_element(by, value)
            driver.execute_script("arguments[0].click();", elemento)
            print("⚠️ Clique via JavaScript executado como fallback.")
        except Exception as js_error:
            print(f"❌ Falha também no clique via JavaScript: {js_error}")

# ✅ Digitar com limpeza e validação
def digitar(driver, by, value, text, timeout=10):
    try:
        campo = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        campo.clear()
        campo.send_keys(text)
    except Exception as e:
        print(f"❌ Erro ao digitar: {e}")

# ✅ Clicar por texto visível no botão
def clicar_por_texto(driver, texto, timeout=10):
    try:
        botao = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[.//span[contains(., '{texto}')]]")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
        driver.execute_script("arguments[0].click();", botao)
        print(f"✅ Botão '{texto}' clicado com sucesso!")
    except Exception as e:
        print(f"❌ Falha ao clicar no botão '{texto}': {e}")

# ✅ Localizar e retornar o elemento (sem clicar)
def localizar(driver, by, value, timeout=10):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return elemento
    except Exception as e:
        print(f"❌ Erro ao localizar elemento: {e}")
        return None
