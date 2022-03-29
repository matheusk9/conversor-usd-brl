from tkinter import *
from tkinter import ttk
from tkinter.font import Font


def screen():
    screen = Tk()
    screen.title("USD -> BRL")
    screen.geometry("400x400")
    screen.configure(background="black")
    screen.resizable(width=False, height=False)
    screen.attributes("-alpha",0.9)
    return screen
    

def label_place(janela, nome= str, fonte_leg="Times New Roman",tam_fonte=15, cor_bg="black", cor_fg="white", place_x=100, place_y=100):
    legenda = Label(janela, text= nome, font=(fonte_leg,tam_fonte),bg=cor_bg, fg=cor_fg)
    legenda.place(x= place_x ,y= place_y)
    return legenda


def label_in_screen(main_screen):     
    texto1='Cotação atual: $1 = R$'
    label_brl='BRL'
    label_usd='USD'
    label_place(main_screen,texto1,place_x=100,place_y=350)
    label_place(main_screen,label_usd,place_x=130,place_y=223)
    label_place(main_screen,label_brl,place_x=130,place_y=260)


def text_box(main_screen):
    box_usd=ttk.Entry(main_screen, width=20)
    box_usd.place(x=190, y=228)
    return box_usd


def editing(main_screen):
    leg = label_place(main_screen,"0,00",place_x=190,place_y=260, cor_fg='green')
    return leg


def button_conversao(main_screen,funcao):
    ttk.Button(main_screen, text="OK", width=15, command=funcao).place(x=200, y=300)
