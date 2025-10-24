from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Navegador:
    def __init__(self):
        pass
    
    def abrir(self):
        try:
            # Configurações do navegador (opcional)
            options = webdriver.ChromeOptions()
            # options.add_argument("--comando opcional")
            # Exemplo: rodar em modo anônimo | options.add_argument("--incognito") 
            # Rodar sem abrir a janela (headless)| options.add_argument("--headless")
            # Rodar a janela em tela cheia | options.add_argument("--start-maximized") 
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()),
                options=options
            )


            self.driver.implicitly_wait(10) # Regra geral - Procura o elemente por até 10 segundos

        except Exception as e:
            print("Falha ao iniciar o navegador!")

        return None

    def abrir_url(self, url):
        if self.driver:
            self.driver.get(url)
        else:
            print("⚠️ O navegador ainda não foi iniciado!")

    def fechar_navegador(self):

        if self.driver:
            self.driver.quit()
            print("🧹 Navegador fechado.")
        else:
            print("⚠️ Nenhum navegador para fechar.")