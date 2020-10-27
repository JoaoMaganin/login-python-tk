from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco_de_dados

# Iniciando e configurando a tela
screen = Tk()
screen.geometry("500x600+450+20")
screen.title("Login com Python")
screen.configure(bg="white")
screen.resizable(0, 0)
screen.attributes("-alpha", 0.9)
screen.iconbitmap(default="images/python_ico.ico")

# Criando o frame superior e inferior
top_frame = Frame(screen, width=493, height=250, bg="#005000", relief="raised")
top_frame.pack(side=TOP)

bot_frame = Frame(screen, width=493, height=345, bg="#005000", relief="raised")
bot_frame.pack(side=BOTTOM)

# Funções


def registrar():
    # removendo widgets
    login_button.place(x=5000)
    register_button.place(x=5000)

    # Inserindo widgets
    nome_label = Label(bot_frame, text="Nome:", font=("Segoe UI", 25), bg="#005000", fg="#fff")
    nome_label.place(x=10, y=10)
    nome_entry = ttk.Entry(bot_frame)
    nome_entry.place(x=150, y=27, width=300, height=25)

    email_label = Label(bot_frame, text="Email:", font=("Segoe UI", 25), bg="#005000", fg="#fff")
    email_label.place(x=10, y=60)
    email_entry = ttk.Entry(bot_frame)
    email_entry.place(x=150, y=77, width=300, height=25)

    user_label.place(x=10, y=110)
    user_entry.place(x=150, y=127)
    pass_label.place(x=10, y=160)
    pass_entry.place(x=150, y=177)

    def registrar_no_banco():
        nome = nome_entry.get()
        email = email_entry.get()
        usuario = user_entry.get()
        senha = pass_entry.get()

        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro no registo",
                                 message="Algum dos campos está vazio, preencha todos os campos.")
        else:
            banco_de_dados.cursor.execute("""
            INSERT INTO usuarios(nome, email, usuario, senha) VALUES (?, ?, ?, ?)
            """, (nome, email, usuario, senha))
            banco_de_dados.conn.commit()

            nome_entry.delete(0, END)
            email_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo(title="Informação de registro", message="Registrado com sucesso!")

    register_bt2 = ttk.Button(bot_frame, text="Registrar", command=registrar_no_banco)
    register_bt2.place(x=125, y=250, width=250, height=30)

    def voltar_menu():
        # Removendo widgets
        nome_label.place(x=5000)
        nome_entry.place(x=5000)
        email_label.place(x=5000)
        email_entry.place(x=5000)
        register_bt2.place(x=5000)
        voltar_bt.place(x=5000)

        # Puxando widgets de volta
        user_label.place(x=10, y=40)
        user_entry.place(x=150, y=57, width=300, height=25)
        pass_label.place(x=10, y=100)
        pass_entry.place(x=150, y=117, width=300, height=25)
        login_button.place(x=125, y=200, width=250, height=40)
        register_button.place(x=150, y=250, width=200, height=40)

    voltar_bt = ttk.Button(bot_frame, text="Voltar", command=voltar_menu)
    voltar_bt.place(x=150, y=290, width=200, height=30)


def login():
    usuario = user_entry.get()
    senha = pass_entry.get()

    banco_de_dados.cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = ? AND senha = ?
    """, (usuario, senha))

    verifica_login = banco_de_dados.cursor.fetchone()
    try:
        if usuario in verifica_login and senha in verifica_login:
            messagebox.showinfo(title="Informação de login", message="Logado com sucesso. Seja bem-vindo!")
    except:
        messagebox.showerror(title="Informação de login",
                             message="Acesso negado. Verifique se está cadastrado no sistema.")


# Colocando os widgets
logo = PhotoImage(file="images/python_modificado.png")

logo_label = Label(top_frame, image=logo, bg="#005000")
logo_label.place(width=200, height=200, x=150, y=20)

user_label = Label(bot_frame, text="Usuário:", font=("Segoe UI", 25), bg="#005000", fg="#fff")
user_label.place(x=10, y=40)

user_entry = ttk.Entry(bot_frame)
user_entry.place(x=150, y=57, width=300, height=25)

pass_label = Label(bot_frame, text="Senha:", font=("Segoe UI", 25), bg="#005000", fg="#fff")
pass_label.place(x=10, y=100)

pass_entry = ttk.Entry(bot_frame, show="●")
pass_entry.place(x=150, y=117, width=300, height=25)

login_button = ttk.Button(bot_frame, text="Logar", command=login)
login_button.place(x=125, y=200, width=250, height=40)

register_button = ttk.Button(bot_frame, text="Registrar", command=registrar)
register_button.place(x=150, y=250, width=200, height=40)

screen.mainloop()
