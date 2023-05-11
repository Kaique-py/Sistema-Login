import PySimpleGUI as sg

#Primeiro, vamos criar o layout da janela que queremos exibir.
#Uma dica aqui é, antes de tudo, desenhar essa janela para ver como queremos que ela se pareça para, a 
#partir daí, implementá-la.

layout = [
    #Para cada 'linha' da minha janela, vamos ter uma lista (que seria, em pcp, cada frame ou campo)
    [sg.Text('Usuário:')],
    [sg.Input(key='user')],
    [sg.Text('Senha:')],
    [sg.Input(key='password')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')],
]

#Após criado o layout, vamos criar a janela propriamente dita:

janela = sg.Window('Acesso ao Sistema', layout=layout)

#Agora vamos criar o loop para manter a janela aberta e lendo os valores inseridos pelo usuário:
while True:
    try:
        event, values = janela.read()
        if event == sg.WIN_CLOSED: #Se o usuário clicar no X para fechar a janela o programa tem que parar.
            break
        elif event == 'Login':
            usuario_cadastrado = 'Kaique-Py'
            senha_cadastrada = '12345'
            usuario = values['user']
            senha = values['password']
            if usuario == usuario_cadastrado and senha == senha_cadastrada:
                janela['mensagem'].update('Login realizado com sucesso!')
                sg.popup('Bem vindo ao Sistema!')
            else:
                janela['mensagem'].update('Usuário ou senha incorretos. Favor tente novamente.')
                sg.popup_error('Não foi possível acessar o Sistema. Usuário ou senha incorretos. Favor tente novamente.')
    except:
        sg.popup_error('Falha no Sistema. Favor tente novamente mais tarde.')