import PySimpleGUI as sg
import datetime

ANO_ATUAL = datetime.datetime.now().year

JANELA_TEMA = sg.theme("DarkGreen")

JANELA_RODAPE = sg.Text(f"Desenvolvido por Michael JM Cardoso. © {ANO_ATUAL}\n             Todos os direitos reservados.", text_color='blue', font='Helvetica 8 bold')

FONTE = font='Any 10 bold'

FAIXA_DE_COMPLEXIDADE = ['1', '2', '4', '8', '12', '16', '20', '24', '40']

REGIME_DE_EXECUCAO = ['Parcial', 'Presencial', 'Integral']

AVALIACAO_NOTA = ['10']

HORAS_EXECUTADAS = ['1', '2', '4', '8', '12', '16', '20', '24', '40']

MACRO_ATIVIDADES = [
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

ATIVIDADES_DETALHADAS = [
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

