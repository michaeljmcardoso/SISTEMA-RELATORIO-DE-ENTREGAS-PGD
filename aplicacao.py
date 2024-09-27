import PySimpleGUI as sg
from funcoes_registro import inserir_dados, consultar_registros, alterar_registro, excluir_registro
import constantes
from salvar import salvar_planilha
from somar import somar_horas_executadas

class Aplicacao:
    def __init__(self):
        self.janela = self.criar_janela()

    def iniciar(self):
        while True:
            event, values = self.janela.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 'INSERIR':
                inserir_dados(values, self.janela)
                consultar_registros(self.janela)

            elif event == 'CONSULTAR':
                consultar_registros(self.janela)

            elif event == 'ALTERAR':
                alterar_registro(self.janela)

            elif event == 'BAIXAR RELATÓRIO':
                salvar_planilha(self.janela)

            elif event == 'EXCLUIR':
                excluir_registro(self.janela)

            elif event == 'HORAS EXECUTADAS':
                somar_horas_executadas()


    def criar_janela(self):
            sg.theme(constantes.JANELA_TEMA)

            layout = [
                [
                    sg.Column([
                        [sg.Text('Macro Atividades:')],
                        [sg.Combo(constantes.MACRO_ATIVIDADES, key='-MACRO-', size=(45, 1))],
                        [sg.Text('Atividades Detalhadas:')],
                        [sg.Combo(constantes.ATIVIDADES_DETALHADAS, key='-DETALHADA-', size=(45, 1))],
                        [sg.Text('Faixa de Complexidade:')],
                        [sg.Combo(constantes.FAIXA_DE_COMPLEXIDADE, key='-HORAS-', size=(10, 1))],
                        [sg.Text('Regime de Execução:')],
                        [sg.Combo(constantes.REGIME_DE_EXECUCAO, key='-REGIME-', size=(10, 1))],
                        [sg.Text('Entregas:')],
                        [sg.Input(key='-ENTREGAS-', size=(45, 1))],
                        [sg.Text('Avaliação Nota:')],
                        [sg.Combo(constantes.AVALIACAO_NOTA, key='-NOTAS-', size=(10, 1))],
                        [sg.Text('Horas Executadas:')],
                        [sg.Combo(constantes.HORAS_EXECUTADAS, key='-EXECUTADAS-', size=(10, 1))],
                        [sg.Text('')],

                        [
                            sg.Button('INSERIR', button_color='#ac4e04'),
                            sg.Button('CONSULTAR', button_color='#ac4e04'),
                            sg.Button('ALTERAR', button_color='#ac4e04')
                        ],

                        [sg.Button('EXCLUIR', button_color='#ac4e04')],

                        [sg.Text('')],

                        [
                            sg.Button('BAIXAR RELATÓRIO', button_color='green'),
                            sg.Button('HORAS EXECUTADAS', button_color='green')
                        ],
                    ], 
                    
                    vertical_alignment='top', element_justification='left', size=(340, 620)),
                    
                    sg.Column([
                        [sg.Table(
                            values=[],
                            headings=[
                                'ID ',
                                '   Macro_atividades   ',
                                'Atividades_detalhadas',
                                'Horas',
                                'Regime ',
                                '   Entregas   ',
                                'Nota',
                                'H_Executadas'
                            ], 
                            num_rows=40,
                            key='-TABLE-',
                            hide_vertical_scroll=False,
                            vertical_scroll_only=False,
                            justification='left',
                            auto_size_columns=True,
                        )]
                    ], 
                    
                    vertical_alignment='left', element_justification='left', size=(1150, 630))
                ],

                [sg.Text('', size=(75, 1)), constantes.JANELA_RODAPE]
            ]

            janela = sg.Window('SISPGD - Sistema de Relatório de Entregas PGD', layout, resizable=True)
            return janela