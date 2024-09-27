import PySimpleGUI as sg
from funcoes_registro import conectar_banco_de_dados
from constantes import FONTE

def somar_horas_executadas():
    conn = conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(Horas_executadas) FROM RELATORIO")
    totalHorasExecutadas = cursor.fetchone()[0]

    if totalHorasExecutadas is not None:
        totalHorasFormatado = "{:.2f}".format(totalHorasExecutadas)

        sg.popup(f'Horas Executadas: {totalHorasExecutadas} horas', title='Total de Horas', font=FONTE)
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=FONTE)