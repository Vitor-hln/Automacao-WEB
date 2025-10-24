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
    
    def transformar_df(self):
        dados = self.selecionar_arquivo()
        
        if not dados:     # Caso o usúario cancele a operação
            return None
        
        extensao = Path(dados).suffix.lower() # extensao retorna apenas o sufixo ".csv" ou ".xlsx"
                    
        match extensao: # match compara o sufixo de extensao com o sufixo do arquivo passado
            case  ".xlsx" | ".xls":
                df = pd.read_excel(dados)
            case ".csv":
                df = pd.read_csv(dados, sep=";")
            case _:
                messagebox.showerror("Erro", "Arquivo não suportado!")
                return None
        
        return df 



