import os
from dotenv import load_dotenv
from apps.driver.browser import Navegador
from apps.pages import login_page, notas_page, principal_page
from apps.loop.loop import looper
from data.importacao import Importador_de_arquivos
from utils.utils import msg_erro



def main():
   
    # Carrega variaveis do ambiente
    load_dotenv()
    # Variaveis de ambiente
    login = os.getenv("login")
    senha = os.getenv("senha")
    url = os.getenv("URL")    
    
    
    # Usuario seleciona arquivo com informações
    imp = Importador_de_arquivos()
    df = None 
    # loop de 3 tentativas para upar arquivo valido
    for i in range(3):
        try:
            df = imp.transformar_df() # retorna os dados do excel como Data frame
            if df is not None:
                break # sai do loop se upar arquivo correto
            else:
                print(f"Arquivo invalido tente novamente.\n Tentativa{i+1}")
        except Exception as e:
            print(f"Tentativa {i+3}:\n Erro ao importar arquivo - {e} ")
    if df is None:
        msg_erro("Falha após 3 tentativas.\n Encerrando")
    else:
        pass
        
    
    # Iniciar navegador
    nav = Navegador()
    nav.abrir()
    nav.abrir_url(url)
    driver = nav.driver
    
    # Login
    user = login_page.LogarUsuario(driver)
    user.logar(login, senha)
    
    # Pagina Princcipal
    pp = principal_page.pagina_principal(driver)
    pp.acessar_disciplinas()
    pp.selecionar_filtros() 
        
    for index, row in df.iterrows():
        disciplina = row['Nome']
        nav.focar_na_aba_atual() 
        l = looper(driver)
        
        l.acessar_disciplinas(disciplina)
        l.adicionar_notas()
        l.abrir_menu_formula_nota_final()
        l.inserir_formula()
        l.validar_formula()
        
        driver.close()    
        

    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        msg_erro(f"Não foi possivel iniciar a automação:  {e}")
    
    