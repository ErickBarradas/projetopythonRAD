import tkinter as tk
from tkinter import messagebox
import sqlite3
import re


# Conecta ao banco de dados SQLite
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# Cria a tabela de usuários se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS bancodeusuarios (
    nomedeusuario TEXT PRIMARY KEY,
    senha TEXT NOT NULL);
''')

def register():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute('SELECT * FROM bancodeusuarios WHERE nomedeusuario = ?', (username,))

#regex de regra na criação do email
    if not re.match(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,7}\b' , username):
        
        messagebox.showinfo("Erro!", "Necessário ser um email válido!")
        #print('E-mail inválido!')
        return
    
    if cursor.fetchone() is not None:
        messagebox.showinfo("Erro", "Nome de usuário já existe")
    else:
        cursor.execute('INSERT INTO bancodeusuarios VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute('SELECT * FROM bancodeusuarios WHERE nomedeusuario = ? AND senha = ?', (username, password))
    if cursor.fetchone() is not None:
        #login.py.open()
        #messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        janeladelogin.destroy()
        #LINK PARA A CONTINUACAO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        messagebox.showinfo("Erro", "Nome de usuário ou senha incorretos")

janeladelogin = tk.Tk()
janeladelogin.title('Cadastro de Jogos')

width = 250
height = 250
# colectando informacoes do monitor
sc_width = janeladelogin.winfo_screenwidth()
sc_height = janeladelogin.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
# tamanho da janela principal
janeladelogin.geometry("%dx%d+%d+%d" % (width, height, x, y))
janeladelogin.resizable(0, 0)


label_username = tk.Label(janeladelogin, text="Endereço de e-mail:")
label_username.pack()

entry_username = tk.Entry(janeladelogin)
entry_username.pack(padx=10, pady=10)

label_password = tk.Label(janeladelogin, text="Senha:")
label_password.pack()

entry_password = tk.Entry(janeladelogin, show="*")
entry_password.pack(padx=10, pady=10)

button_register = tk.Button(janeladelogin, text="Cadastrar", command=register)
button_register.pack(padx=30, pady=30)

button_login = tk.Button(janeladelogin, text="Entrar", command=login)
button_login.pack()

janeladelogin.mainloop()