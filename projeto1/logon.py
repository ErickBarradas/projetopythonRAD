from tkinter import *
import re
import sqlite3


def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Verifica se o e-mail é válido
    if not re.match(r"[^@]+@[^@]+\.[^@]+", usuario):
        print('E-mail inválido!')
        return

    # Verifica se o usuário e a senha estão corretos
    if usuario == 'erick@gmail.com' and senha == 'vasco':
        # Abre uma nova janela
        nova_janela = Toplevel(janela)
        nova_janela.title('Bem-vindo')
        
        width = 350
        height = 250
        nova_janela.geometry("%dx%d+%d+%d" % (width, height, x, y))
        nova_janela.resizable(0, 0)        
        

        Label(nova_janela, text='Login bem-sucedido!').pack()
    else:
        print('Usuário ou senha incorretos!')



def novo_cadastro():
    cadastro_janela = Toplevel(janela)
    cadastro_janela.title('Janela de Cadastro')

    entrada_usuario = Entry(cadastro_janela)
    entrada_usuario.pack()
    entrada_senha = Entry(cadastro_janela, show='*')
    entrada_senha.pack()
    
    width = 350
    height = 250
    cadastro_janela.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cadastro_janela.resizable(0, 0)
    
    botao_cadastrar = Button(cadastro_janela, text='Cadastrar', command=novo_cadastro)
    botao_cadastrar.pack()

      



# Janela e atributos
janela = Tk()
janela.title('Tela de Login')

width = 450
height = 250
# colectando informacoes do monitor
sc_width = janela.winfo_screenwidth()
sc_height = janela.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

# tamanho da janela principal
janela.geometry("%dx%d+%d+%d" % (width, height, x, y))
janela.resizable(0, 0)


# Cria os campos de entrada
entrada_usuario = Entry(janela)
entrada_usuario.pack()
entrada_senha = Entry(janela, show='*')
entrada_senha.pack()

#botoes
botao_login = Button(janela, text='Login', command=verificar_login)
botao_login.pack()

botao_cadastro = Button(janela, text='Cadastro', command=novo_cadastro)
botao_cadastro.pack()


# Inicia o loop principal
janela.mainloop()

