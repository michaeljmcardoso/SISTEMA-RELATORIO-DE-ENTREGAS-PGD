import PySimpleGUI as sg
import pandas as pd
import tkinter as tk
import funcoes_registro
import constantes
from tkinter import filedialog

def planilha(registros):
    conn = funcoes_registro.conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()

    cursor.execute("SELECT * FROM RELATORIO")
    registros = cursor.fetchall()
    if registros:
        df = pd.DataFrame(
            registros,     
            columns=[
                'ID',
                'Macro atividades',
                'Atividades detalhadas',
                'Faixa de complexidade (horas)',
                'Regime de execução',
                'Entregas',
                'Avaliação (nota de 0 a 10)',
                'Horas executadas'
                ]
            )
        
        # Abre uma janela para selecionar o local e o nome do arquivo
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        root.destroy()  # Fecha a janela de seleção de arquivo

        if file_path:
            df.to_excel(file_path, index=False)
            sg.popup('Relatório extraído com sucesso!', title='Sucesso', font=constantes.FONTE)
        else:
            sg.popup('Nenhum arquivo selecionado. O relatório não foi salvo.', title='Aviso', font=constantes.FONTE)
    else:
        sg.popup('Não há registros para extrair.', title='Erro', font=constantes.FONTE)