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

def procurar_elemento(driver, by, value, action, timeout=10, **kwargs):
    """
    Função central (Dispatcher) que decide qual ação executar.
    """
    match str(action).lower():
        
        case "clicar":
            clicar(driver, by, value, timeout)

        case "digitar":
            if 'text' in kwargs:
                texto_a_digitar = kwargs['text']
                # --- CORREÇÃO: Passa a variável 'timeout', não o valor fixo 10 ---
                digitar(driver, by, value, texto_a_digitar, timeout=timeout) 
            else:
                # --- CORREÇÃO: Mensagem de erro mais clara ---
                print(f"❌ Erro de Lógica: Ação 'digitar' foi chamada, mas o argumento 'text' não foi fornecido. ❌")
                
        case _:
            print(f"❌ Erro: Ação '{action}' desconhecida. Use 'clicar' ou 'digitar'. ❌")
            
    return None

        