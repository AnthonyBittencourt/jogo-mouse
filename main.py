
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
from pygame.locals import *
import pyautogui
import time
import threading
# Cores
coRpreto = "#000000"
coRbranco = "#feffff"
coRcinza = "#353535"
coRazul = "#38576b"
coRcinza2 = "#403d3d"
coRvermelho = "#ff0000"

# Variável para guardar credenciais (apenas exemplo, não persistente)
credenciais = ['1', '1']

# Criando janela principal
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(bg=coRbranco)



# Frames
frame_cima = Frame(janela, width=310, height=50, bg=coRbranco, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=coRbranco, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame_cima
l_nome = Label(frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy 25'), bg=coRbranco, fg=coRcinza2)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 25'), bg=coRcinza)
l_linha.place(x=10, y=45)

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!!!')

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])

        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome do usuário ou a palavra passe')

def nova_janela():
    jogos_text = Label(frame_cima, text='JOGOS:', bg=coRbranco, fg=coRpreto, font=('Ivy 25 bold'))
    jogos_text.place(x=95, y=10)
    linha = Label(frame_cima, text='', width=30, bg=coRcinza)
    linha.place(x=49, y=48)

    jogoMouse_b = Button(frame_baixo, text='Mouse Track Game', width=15, height=1, bg=coRazul, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=janela_jogo)
    jogoMouse_b.place(x=95,y=10)
def abrir_janela_cadastro():
    def salvar_cadastro():
        novo_nome = entry_nome.get()
        nova_senha = entry_Novasenha.get()
        senhaantiga = entry_senha.get()

        senhaINC_l = Label(janela_cadastro, text="Senha incorreta. Tente novamente", bg=coRbranco, fg=coRbranco, font=("Ivy", 7))
        senhaINC_l.place(x=90, y=90)
        
        while senhaantiga == credenciais[1]:
            senhaINC_l.config(fg = coRbranco)
            break

        if senhaantiga != credenciais[1]:
            senhaINC_l.config(fg = coRvermelho)

        elif len(nova_senha) < 8:
            Label(janela_cadastro, text="senha inválida. necessário no mínimo 8 caracteres.", bg=coRbranco, fg=coRvermelho, font=("Ivy", 7)).place(x=90, y=130)
        
        elif nova_senha == credenciais[1]:
            Label(janela_cadastro, text="a senha deve ser diferente da atual", bg=coRbranco, fg=coRvermelho, font=("Ivy", 6)).place(x=90, y=130)

        elif novo_nome and nova_senha:
            credenciais[0] = novo_nome
            credenciais[1] = nova_senha
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            janela_cadastro.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    janela_cadastro = Toplevel(janela)
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("350x300")
    janela_cadastro.configure(bg=coRbranco)
    janela_cadastro.resizable(False, False)

    Label(janela_cadastro, text="    Nome:", bg=coRbranco, fg=coRcinza2, justify='right', font=("Ivy", 10)).place(x=10, y=30)
    entry_nome = Entry(janela_cadastro, width=40)
    entry_nome.place(x=90, y=30)

    Label(janela_cadastro, text="Senha atual:", bg=coRbranco, fg=coRcinza2, font=("Ivy", 10)).place(x=10, y=70)
    entry_senha = Entry(janela_cadastro, width=40, show="*")
    entry_senha.place(x=90, y=70)

    Label(janela_cadastro, text="Nova senha:", bg=coRbranco, fg=coRcinza2, font=("Ivy", 10)).place(x=10, y=110)
    entry_Novasenha = Entry(janela_cadastro, width=40, show="*")
    entry_Novasenha.place(x=90, y=110)

    Button(janela_cadastro, text="Atualizar", bg=coRcinza, fg=coRbranco, font=("Ivy", 10), command=salvar_cadastro).place(x=70, y=170)

# Campos do login
l_nome = Label(frame_baixo, text="Name *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
e_nome.place(x=14, y=40)

l_pass = Label(frame_baixo, text="Password *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
l_pass.place(x=10, y=90)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
e_pass.place(x=14, y=110)

# Botões
botao_confirmar = Button(frame_baixo, text="Entrar", width=39, height=2, bg=coRcinza, fg=coRbranco, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=150)

botao_cadastrar = Button(frame_baixo, text="Atualizar", width=39, height=2, bg=coRazul, fg=coRbranco, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_janela_cadastro)
botao_cadastrar.place(x=15, y=200)

###########jogo do mouse#########################
def janela_jogo():
    click = 0
    tempo = 60

    janela_mini = Toplevel(janela)
    janela_mini.title("Mouse Track Game")
    janela_mini.geometry("500x500")
    janela_mini.configure(bg=coRcinza2)

    # Labels de contagem
    cont_l = Label(janela_mini, width=20, text=f"Tempo restante: {tempo}", bg=coRcinza2, fg=coRbranco, font=("Ivy", 10))
    cont_l.place(x=10, y=10)

    cont_click_l = Label(janela_mini, width=15, text=f"Cliques: {click}", bg=coRcinza2, fg=coRbranco, font=("Ivy", 10))
    cont_click_l.place(x=370, y=10)

    # Botão móvel
    button = Button(janela_mini, text="Click", bg=coRazul, fg=coRbranco, font=("Ivy", 10, "bold"))
    button.place(x=200, y=200)

    def move_button():
        x = random.randint(36, janela_mini.winfo_width() - button.winfo_reqwidth())
        y = random.randint(36, janela_mini.winfo_height() - button.winfo_reqheight())
        button.place(x=x, y=y)

    def detectar_click(event):
        nonlocal click, tempo
        if button.winfo_containing(event.x_root, event.y_root) == button:
            click += 1
            cont_click_l.config(text=f"Cliques: {click}")
            tempo += 1
            move_button()
        else:
            tempo -= 2

    def contador_tempo():
        nonlocal tempo
        if tempo > 0:
            cont_l.config(text=f"Tempo restante: {tempo}")
            janela_mini.after(1000, contador_tempo)
            tempo -= 1
        else:
            messagebox.showinfo("Fim de jogo", f"O tempo acabou! Sua pontuação: {click}")
            janela_mini.destroy()

    # Inicia o jogo
    button.config(command=move_button)
    janela_mini.bind("<Button-1>", detectar_click)
    contador_tempo()
janela.mainloop()
