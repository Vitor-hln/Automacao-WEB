# Importação de dados de arquivos
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from pathlib import Path

class Importador_de_arquivos:
    def __init__(self):
        self.root = tk.Tk() 
        self.root.withdraw()
    
    def selecionar_arquivo(self):
        return filedialog.askopenfilename(
            title= "Selecione o arquivo Excel",
            filetypes=[("Planilhas Excel", "*.xlsx, *.xls, *.csv")]
        )
    
    def importar(self):
        arquivo = self.selecionar_arquivo()
        
        if not arquivo:     # Caso o usúario cancele a operação
            return None
        
        arquivo_final = Path(arquivo).suffix.lower()
                
        def verifica_extensao(extensao):
            
            match extensao:
                
                case  ".xlsx" | ".xls":
                    return pd.read_excel(arquivo)
                
                case ".csv":
                    return pd.read_csv(arquivo)
                
                case _:
                    messagebox.showerror("Erro", "Arquivo não suportado!")
                    return None
        
        return verifica_extensao(arquivo_final)   

