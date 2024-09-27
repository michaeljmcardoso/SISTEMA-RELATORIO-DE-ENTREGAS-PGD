import PySimpleGUI as sg
import sqlite3
import constantes


def conectar_banco_de_dados():
    try:
        conn = sqlite3.connect('relatorio.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}", font=constantes.FONTE)
        return None


def criar_tabela_se_nao_existir(conn):
    cursor = conn.cursor()
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
    

def inserir_dados(values, janela):
    macroAtividades = values['-MACRO-']
    atividadesDetalhadas = values['-DETALHADA-']
    faixaComplexidadeHoras = str(values['-HORAS-'])
    regimeExecucao = values['-REGIME-']
    entregas = values['-ENTREGAS-']
    avaliacao = values['-NOTAS-']
    horasExecutadas = values['-EXECUTADAS-']

    conn = conectar_banco_de_dados()
    
    if conn is not None:
        cursor = conn.cursor()
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
    
    sg.popup('Dados inseridos com sucesso!', title='Sucesso', font=constantes.FONTE)

    janela['-MACRO-'].update('')
    janela['-DETALHADA-'].update('')
    janela['-HORAS-'].update('')
    janela['-REGIME-'].update('Presencial')
    janela['-ENTREGAS-'].update('')
    janela['-NOTAS-'].update('10')
    janela['-EXECUTADAS-'].update('')
    
    cursor.close()
    conn.close()


def consultar_registros(janela):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM RELATORIO")
        registros = cursor.fetchall()
        
        if registros:
            janela['-TABLE-'].update(registros)
        else:
            janela['-TABLE-'].update(registros)
            sg.popup('Não há registros cadastrados.', title='Registros', font=constantes.FONTE)

        cursor.close()
        conn.close()


def alterar_registro(janela):
    conn = conectar_banco_de_dados()
    if conn is not None:
        cursor = conn.cursor()

    selected_rows = janela['-TABLE-'].SelectedRows
    if len(selected_rows) != 1:
        sg.popup('Selecione um único registro para alterar.', title='Erro', font=constantes.FONTE)
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
            [sg.Combo(constantes.MACRO_ATIVIDADES, size=(45, 1), key='-MACRO-', default_value=macroAtividades)],
            [sg.Text('Atividades Detalhadas:')],
            [sg.Combo(constantes.ATIVIDADES_DETALHADAS, size=(45, 1), key='-DETALHADA-', default_value=atividadesDetalhadas)],
            [sg.Text('Faixa de Complexidade:')],
            [sg.Combo(constantes.FAIXA_DE_COMPLEXIDADE, size=(10, 1), key='-HORAS-', default_value=faixaComplexidadeHoras)],
            [sg.Text('Regime de Execução:')],
            [sg.Combo(constantes.REGIME_DE_EXECUCAO, size=(10, 1), key='-REGIME-', default_value=regimeExecucao)],
            [sg.Text('Entregas:')],
            [sg.Input(size=(35, 2), key='-ENTREGAS-', default_text=entregas)],
            [sg.Text('Avaliação Nota:')],
            [sg.Combo(constantes.AVALIACAO_NOTA, size=(10, 1), key='-NOTAS-', default_value=avaliacao)],
            [sg.Text('Horas Executadas:')],
            [sg.Combo(constantes.HORAS_EXECUTADAS, size=(10, 1), key='-EXECUTADAS-', default_value=horasExecutadas)],
            [sg.Text('')],
            [sg.Button('Salvar Alterações', button_color='#ac4e04')],
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

            sg.popup('Registro alterado com sucesso!', title='Sucesso', font=constantes.FONTE)
            
            janelaAlterarDados.close()
            
            consultar_registros(janela)


def excluir_registro(janela):
    selected_rows = janela['-TABLE-'].SelectedRows
    if len(selected_rows) != 1:
        sg.popup('Selecione um único registro para excluir.', title='Erro', font=constantes.FONTE)
        return

    confirmar_exclusao = sg.popup_yes_no('Tem certeza que deseja excluir o registro selecionado?\nEsta ação não poderá ser desfeita.', title='Confirmação', font=constantes.FONTE)
    if confirmar_exclusao == 'Yes':
        try:
            selected_row_values = janela['-TABLE-'].get()[selected_rows[0]] # Obter o ID do registro selecionado na tabela
            registro_id = selected_row_values[0]  # O ID está na primeira coluna da tabela
            
            conn = conectar_banco_de_dados()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM RELATORIO WHERE ID = ?", (registro_id,)) # Query para excluir o registro com base no ID
            conn.commit()

            sg.popup('Registro excluído com sucesso.', title='Sucesso', font=constantes.FONTE)

            consultar_registros(janela)

        except Exception as e:
            sg.popup_error(f'Erro ao excluir registro: {e}', title='Erro', font=constantes.FONTE)