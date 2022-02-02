import random #Biblioteca com ferramentas de sorteio
import os #Permite manipular arquivos externos
import PySimpleGUI as sg #Cria interfaces gráficas
from playsound import playsound

class PassGen: #Criando Esqueleto da classe
    def __init__(self):
        sg.theme('Black')
        playsound('sickLove.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), default_value=1, size=(3, 1), key='total_chars')],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        self.janela = sg.Window('Password generator', layout)

    def Iniciar(self):
        while True:
            event, valores = self.janela.Read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$&%*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    def salvar_senha(self, nova_senha, valores):
        with open('senhas2.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuário: {valores['usuario']}, senha: {nova_senha}\n")
        print('Arquivo Gerado')

gen = PassGen() #Instanciando a classe
gen.Iniciar() #Chamando o método inicar