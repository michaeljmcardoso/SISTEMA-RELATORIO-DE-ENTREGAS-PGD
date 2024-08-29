import PySimpleGUI as sg
import funcoes_registro
import constantes

def horas_executadas():
    conn = funcoes_registro.conectar_banco_de_dados()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(Horas_executadas) FROM RELATORIO")
    totalHorasExecutadas = cursor.fetchone()[0]

    if totalHorasExecutadas is not None:
        totalHorasFormatado = "{:.2f}".format(totalHorasExecutadas)

        sg.popup(f'Horas Executadas: {totalHorasExecutadas} horas', title='Total de Horas', font=constantes.FONTE)
    else:
        sg.popup('Não há registros para exibir.', title='Erro', font=constantes.FONTE)