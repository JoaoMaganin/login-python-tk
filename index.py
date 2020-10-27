from tkinter import *
from tkinter import ttk

# Iniciando e configurando a tela
screen = Tk()
screen.geometry("500x600")
screen.title("Login com Python")
screen.configure(bg="white")
screen.resizable(0, 0)
screen.attributes("-alpha", 0.9)

# Criando o frame superior e inferior
top_frame = Frame(screen, width=493, height=250, bg="#005000", relief="raised")
top_frame.pack(side=TOP)

bot_frame = Frame(screen, width=493, height=345, bg="#005000", relief="raised")
bot_frame.pack(side=BOTTOM)

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

pass_entry = ttk.Entry(bot_frame)
pass_entry.place(x=150, y=117, width=300, height=25)

login_button = Button(bot_frame, text="Logar", font=("Segoe UI", 10), command="#")
login_button.place(x=150, y=200, width=200, height=40)

register_button = Button(bot_frame, text="Registrar", font=("Segoe UI", 10), command="#")
register_button.place(x=150, y=250, width=200, height=40)

screen.mainloop()
