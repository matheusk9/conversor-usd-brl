import requests
from front_end import *

def buscar_dados():
    request  = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    address_data = request.json()
    brl = address_data['USDBRL']['high']   
    return round(float(brl),2)


def conversao_BRL_USD(valor):
    price = valor/buscar_dados()
    modificacao = str(price)
    return modificacao.replace('.',',')


def conversao_USD_BRL(valor_func, legenda,legenda2):
    valor = valor_func
    valor = float(valor)
    price = round(valor*buscar_dados(),2)
    modificacao = str(price)
    legenda['text']=modificacao.replace('.',',')
    legenda2['text']=buscar_dados()


main_screen = screen()
cotacao_atual=label_place(main_screen,buscar_dados(),place_x=290,place_y=350, cor_fg='green')
topFrame = Frame(main_screen, width = 400, height= 150, bg="MIDNIGHTBLUE",relief="raise")
topFrame.pack(side=TOP)
logo = PhotoImage(file=r"files\imag.png")
LogoLabel = Label(topFrame, image=logo, bg="black").place(x=-120, y=-250)
legenda=editing(main_screen)
retorno = text_box(main_screen)
label_in_screen(main_screen)
button_conversao(main_screen, lambda:(conversao_USD_BRL(retorno.get(),legenda,cotacao_atual)))

main_screen.mainloop()

