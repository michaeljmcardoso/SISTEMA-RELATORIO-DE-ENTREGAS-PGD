# Sistema de Relatório de Entregas PGD

import sqlite3
import PySimpleGUI as sg
import pandas as pd
import datetime

# Criar o banco de dados
conn = sqlite3.connect('relatorio.db')

# Conectar a um banco existente
cursor = conn.cursor()

# Criar a tabela RELATORIO se ela não existir
cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS RELATORIO ( 
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Macro_atividades TEXT,
        Atividades_detalhadas TEXT,
        Faixa_de_complexidade_horas TEXT,
        Regime_de_execução TEXT,
        Entregas TEXT,
        Avaliação_nota_de_0_a_10 TEXT,
        Horas_executadas NUMERIC
        )'''
    )

conn.commit()

# CONSTANTES
macro_atividades = [
    'Análise',
    'Planejamento', 
    'Reuniões_e_Similares', 
    'Verificação_de_Documentos', 
    'Elaboração_de_documentos_diversos', 
    'Estudos_e_Pesquisa_Institucionais', 
    'Levantamento_de_necessidades_e_subsídios',
    'Ação_de_Desenvolvimento_em_Serviço',
    'Direção/Gestão/Assessoria_e_Atendimento' 
]

atividades_detalhadas = [
    'Abertura_de_Processo',
    'Análise_de_Processo_Levantamento_de_Informações',
    'Análise_de_Processo_Administrativo',
    'Análise_de_Sobreposições',
    'Análise_de_Contestação',
    'Atendimento_ao_Público',
    'Contato_com_Comunidade',
    'Envio_de_E-mail',
    'Reunião_de_Equipe',
    'Reunião_Mesa_Quilombola',
    'Reunião_Mesa_Quilombola_Extra',
    'Instrução_Kit_Portaria',
    'Instrução_Kit_Decreto',
    'Revisão_Análise_Técnica_RTID',
    'Sistematização_de_Dados',
    'Elaboração_Minuta_de_Ofício_aos_Órgãos',
    'Elaboração_Minuta_Notificação_Prazo_Contestação',
    'Elaboração_Minuta_Notificação_Julgamento_CDR',
    'Elaboração_Minuta_de_Ofício',
    'Elaboração_Minuta_Edital',
    'Elaboração_de_Minuta_de_Declaração',
    'Elaboração_Nota_Informativa',
    'Elaboração_de_Nota_Técnica',
    'Elaboração_de_Despacho',
    'Elaboração_de_Parecer',
    'Elaboração_de_Plano_de_Ação',
    'Elaboração_de_Ficha_do_RTID',
    'Elaboração_Minuta_Certidão_Tramitação_Processo',
    'Elaboração_Relatório_PGD',
    'Elaboração_Plano_de_Trabalho_PGD',
    'Elaboração_Introdução_Relatório_Antropológico',
    'Elaboração_Capítulo_Dados_Gerais',
    'Elaboração_Conclusão_do_RA',
    'Elaboração_de_Briefing',
    'Estudo_de_Literatura_e_Legislação',
    'GE_Temática_Quilombola',
    'Levantamento_de_Referencial_Teórico',
    'Levantamento_de_Informações_Dados_Gerais',
    'Participação_em_Cursos_e_Palestras',
    'Participação_Audiência_Judicial',
    'Relatório',
    'Redação_Capítulo_Histórico_Ocupacional',
    'Redação_Capítulo_Organização_Social',
    'Redação_Capítulo_Ambiente_e_Produção',
    'Revisão_Formatação_do_Relatório_Antropológico',
    'Solicitação_de_Diárias',
    'Solicitação_de_Viaturas',
    'Transcrição_de_Entrevistas',
]

faixa_de_complexidade = [
    '1',
    '2',
    '4',
    '8',
    '12',
    '16',
    '20',
    '24',
    '40'
]

regime_de_execucao = ['Presencial']

avaliacao_nota = ['10']

horas_executadas = [
    '1',
    '2',
    '4',
    '8',
    '12',
    '16',
    '20',
    '24',
    '40'
]

anoAtual = datetime.datetime.now().year

sg.theme('DarkGreen')

layout = [
    [
        sg.Column([
            [sg.Text('Macro Atividades:')],
            [sg.Combo(macro_atividades, key='-MACRO-', size=(45, 1))],
            [sg.Text('Atividades Detalhadas:')],
            [sg.Combo(atividades_detalhadas, key='-DETALHADA-', size=(45, 1))],
            [sg.Text('Faixa de Complexidade:')],
            [sg.Combo(faixa_de_complexidade, key='-HORAS-', size=(10, 1))],
            [sg.Text('Regime de Execução:')],
            [sg.Combo(regime_de_execucao, key='-REGIME-', size=(10, 1))],
            [sg.Text('Entregas:')],
            [sg.Input(key='-ENTREGAS-', size=(45, 1))],
            [sg.Text('Avaliação Nota:')],
            [sg.Combo(avaliacao_nota, key='-NOTAS-', size=(10, 1))],
            [sg.Text('Horas Executadas:')],
            [sg.Combo(horas_executadas, key='-EXECUTADAS-', size=(10, 1))],
            [sg.Text('')],
            [
                sg.Button('INSERIR', button_color='#ac4e04'), 
                sg.Button('CONSULTAR', button_color='#ac4e04'), 
                sg.Button('ALTERAR', button_color='#ac4e04'), 
                sg.Button('EXCLUIR', button_color='#ac4e04')
            ],
            [sg.Text('')],
            [
                sg.Button('BAIXAR RELATÓRIO', button_color='green'), 
                sg.Button('HORAS EXECUTADAS', button_color='green')
            ]
        ], vertical_alignment='top', element_justification='left', size=(338, 600)),
        sg.Column([
            [sg.Table(
                values=[],
                headings=[
                    'ID',
                    '  Macro_atividades  ',
                    'Atividades_detalhadas',
                    'Horas',
                    'Regime ',
                    '  Entregas  ',
                    'Nota',
                    'Horas_executadas'
                ], 
                num_rows=38,
                key='-TABLE-',
                hide_vertical_scroll=False,
                vertical_scroll_only=False,
                justification='left',
                auto_size_columns=True,
            )]
        ], vertical_alignment='left', element_justification='left', size=(1150, 650))
    ],
    [
        sg.Text('', size=(75, 1)),
        sg.Text(f"Desenvolvido por Michael JM Cardoso © {anoAtual}\n             Todos os direitos reservados.", text_color='black', font='Helvetica 8 bold'), 
        sg.Text('', size=(40, 1))
    ]
]

janela = sg.Window('SISPGD - Sistema de Relatório de Entregas/PGD/F-4/MICHAEL JM CARDOSO', layout, resizable=True)

def inserirDados(values):
    macroAtividades = values['-MACRO-']
    atividadesDetalhadas = values['-DETALHADA-']
    faixaComplexidadeHoras = str(values['-HORAS-'])
    regimeExecucao = values['-REGIME-']
    entregas = values['-ENTREGAS-']
    avaliacao = values['-NOTAS-']
    horasExecutadas = values['-EXECUTADAS-']
    
    cursor.execute("""
        INSERT INTO RELATORIO (
                   'Macro_atividades',
                   'Atividades_detalhadas',
                   'Faixa_de_complexidade_horas',
                   'Regime_de_execução',
                   'Entregas',
                   'Avaliação_nota_de_0_a_10',
                   'Horas_executadas')
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """,
        (
            macroAtividades,
            atividadesDetalhadas,
            faixaComplexidadeHoras,
            regimeExecucao,
            entregas,
            avaliacao,
            horasExecutadas,

        )
    )

    conn.commit()
    sg.popup('Dados inseridos com sucesso!', title='Sucesso')

     # limpar os campos do formulário
    janela['-MACRO-'].update('')
    janela['-DETALHADA-'].update('')
    janela['-HORAS-'].update('')
    janela['-REGIME-'].update(regime_de_execucao)
    janela['-ENTREGAS-'].update('')
    janela['-NOTAS-'].update(avaliacao_nota)
    janela['-EXECUTADAS-'].update('')
    
    consultarRegistros()


# Função para consultar todos os registros do banco de dados
def consultarRegistros():
    cursor.execute("SELECT * FROM RELATORIO")
    registros = cursor.fetchall()
    if registros:
        janela['-TABLE-'].update(registros)
    else:
        sg.popup('Não há registros cadastrados.', title='Registros')


# Função para alterar um registro do banco de dados
def alterarRegistro():
    selected_rows = janela['-TABLE-'].SelectedRows
    if len(selected_rows) != 1:
        sg.popup('Selecione um único registro para alterar.', title='Erro')
        return

    selected_row_values = janela['-TABLE-'].get()[selected_rows[0]]
    macroAtividades = selected_row_values[1]
    atividadesDetalhadas = selected_row_values[2]
    faixaComplexidadeHoras = selected_row_values[3]
    regimeExecucao = selected_row_values[4]
    entregas = selected_row_values[5]
    avaliacao = selected_row_values[6]
    horasExecutadas = selected_row_values[7]

    layoutAlterarDados = [
    [
        sg.Column([
            [sg.Text('Macro Atividades:')],
            [sg.Combo(macro_atividades, size=(45, 1), key='-MACRO-', default_value=macroAtividades)],
            [sg.Text('Atividades Detalhadas:')],
            [sg.Combo(atividades_detalhadas, size=(45, 1), key='-DETALHADA-', default_value=atividadesDetalhadas)],
            [sg.Text('Faixa de Complexidade:')],
            [sg.Combo(faixa_de_complexidade, size=(10, 1), key='-HORAS-', default_value=faixaComplexidadeHoras)],
            [sg.Text('Regime de Execução:')],
            [sg.Combo(regime_de_execucao, size=(10, 1), key='-REGIME-', default_value=regimeExecucao)],
            [sg.Text('Entregas:')],
            [sg.Input(size=(35, 2), key='-ENTREGAS-', default_text=entregas)],
            [sg.Text('Avaliação Nota:')],
            [sg.Combo(avaliacao_nota, size=(10, 1), key='-NOTAS-', default_value=avaliacao)],
            [sg.Text('Horas Executadas:')],
            [sg.Combo(horas_executadas, size=(10, 1), key='-EXECUTADAS-', default_value=horasExecutadas)],
            [sg.Text('')],
            [sg.Button('Salvar Alterações', button_color='#ac4e04')],
            [sg.Text('')],
            [sg.Text('')],
            [
                sg.Text('', size=(35, 1)),
                sg.Text(f"Desenvolvido por Michael JM Cardoso © {anoAtual}\n             Todos os direitos reservados.", text_color='black', font='Helvetica 8 bold'), 
                sg.Text('', size=(40, 1)),
                
            ]
        ]),
    ]
]

    janelaAlterarDados = sg.Window('Alterar Registro', layoutAlterarDados, size=(800, 500), resizable=False)

    while True:
        event_alterar, values_alterar = janelaAlterarDados.read()

        if event_alterar == sg.WINDOW_CLOSED:
            break
        elif event_alterar == 'Salvar Alterações':
            new_macroAtividades = values_alterar['-MACRO-']
            new_atividadesDetalhadas = values_alterar['-DETALHADA-']
            new_faixaComplexidadeHoras = values_alterar['-HORAS-']
            new_regimeExecucao = values_alterar['-REGIME-']
            new_entregas = values_alterar['-ENTREGAS-']
            new_avaliacao = values_alterar['-NOTAS-']
            new_horasExecutadas = values_alterar['-EXECUTADAS-']
            

            cursor.execute(
                """ 
                UPDATE RELATORIO SET 
                Macro_atividades=?, 
                Atividades_detalhadas=?, 
                Faixa_de_complexidade_horas=?, 
                Regime_de_execução=?, 
                Entregas=?, 
                Avaliação_nota_de_0_a_10=?,
                Horas_executadas=?
                WHERE ID=?
                """,

            (
                new_macroAtividades,
                new_atividadesDetalhadas,
                new_faixaComplexidadeHoras,
                new_regimeExecucao,
                new_entregas,
                new_avaliacao,
                new_horasExecutadas,
                selected_row_values[0]
            )
            
            )

            conn.commit()
            sg.popup('Registro alterado com sucesso!', title='Sucesso')
            janelaAlterarDados.close()
            consultarRegistros()


# Função para excluir um registro do banco de dados
def excluirRegistro():
    selected_rows = janela['-TABLE-'].SelectedRows
    if len(selected_rows) != 1:
        sg.popup('Selecione um único registro para excluir.', title='Erro')
        return

    confirmar_exclusao = sg.popup_yes_no('Tem certeza que deseja excluir o registro selecionado?\nEsta ação não poderá ser desfeita.', title='Confirmação')
    if confirmar_exclusao == 'Yes':
        try:
             # Obter o ID do registro selecionado na tabela
            selected_row_values = janela['-TABLE-'].get()[selected_rows[0]]
            registro_id = selected_row_values[0]  # O ID está na primeira coluna da tabela
            # Query para excluir o registro com base no ID
            cursor.execute("DELETE FROM RELATORIO WHERE ID = ?", (registro_id,))
            
            conn.commit()

            sg.popup('Registro excluído com sucesso.', title='Sucesso')
            # Atualizar a exibição da tabela após a exclusão do registro
            consultarRegistros()

        except Exception as e:
            sg.popup_error(f'Erro ao excluir registro: {e}', title='Erro')


# Função para extrair a planilha
def extrairPlanilha():
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
        
        df.to_excel('Relatorio_PGD.xlsx', index=False)
        sg.popup('Relatório extraído com sucesso!', title='Sucesso')
    else:
        sg.popup('Não há registros para extrair.', title='Erro')

def somarHorasExecutadas():
    cursor.execute("SELECT SUM(Horas_executadas) FROM RELATORIO")
    
    totalHorasExecutadas = cursor.fetchone()[0]

    if totalHorasExecutadas is not None:
        totalHorasFormatado = "{:.2f}".format(totalHorasExecutadas)

        sg.popup(f'Horas Executadas: {totalHorasExecutadas} horas', title='Total de Horas')
    else:
        sg.popup('Não há registros para exibir.', title='Erro')

 # Loop principal para capturar eventos da janela
while True:
    event, values = janela.read()

    if event == sg.WINDOW_CLOSED or event == 'Fechar':
        break
    elif event == 'INSERIR':
        inserirDados(values)
    elif event == 'ALTERAR':
        alterarRegistro()
    elif event == 'CONSULTAR':
        consultarRegistros()
    elif event == 'EXCLUIR':
        excluirRegistro()
    elif event == 'BAIXAR RELATÓRIO':
        extrairPlanilha()
    elif event == 'HORAS EXECUTADAS':
        somarHorasExecutadas()

# Fechando a conexão com o banco de dados e encerrando o programa
conn.close()
janela.close()

'''
Desenvolvido por Michael JM Cardoso
@ 2024 Ararajuba Software House.
Todos os direitos reservados
'''      
