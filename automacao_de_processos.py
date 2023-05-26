#PASSO A PASSO
import pyautogui

# pyperclip copia texto e formata com os acentos
import pyperclip
import time
#acessar sistema da empresa
#fazer login no sistema
#baixar base de dados
#calcular os indicadores
#enviar o email


from pyautogui import *
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever texto
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar combinacao de teclas

pyautogui.PAUSE = 0.2
# passo1: acessar sistema da empresa

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(2)

pyautogui.hotkey("ctrl"+"t")
pyautogui.write("LINK DO SITE")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=983 ,y=441)
pyautogui.write("MEU LOGIN")

time.sleep(2)
pyautogui.press("tab")
pyautogui.write("MINHA SENHA")

time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

#download and rename

#base de dados
import pandas as pd

#importar base

tabela = pd.read_csv("C:\Users\Leonardo Coli\Downloads\{}".format(NOME DO ARQUIVO EM RENAME), sep=";")

print(tabela)

#calcular indicadores

tot_gastos = tabela["tot_gastos_do_arq_csv"].sum()
print("total gastos:", tot_gastos)
#elemento por elemento da tabela

quantidade = tabela["quantidade_do_arq_csv"].sum()
print("quantidade:", quantidade)

preco_medio =  tot_gastos / quantidade
print("preco medio:", preco_medio)


#usar pygui pra enviar email/whatsapp
#FAZER DE TAREFA!!


#""" para excrever texto aberto, email """

#esse F antes do TEXTO : f""" """ serve para formatar o texto
TEXTO: f"""
    BLA BLA BLA
BLA.
BLA BLA BLA BLA
    ATENCIOSAMENTE, EU
"""

pyperclip(TEXTO)
pyautogui.hotckey("ctrl","v") #colar no corpo do email


#ENVIAR EMAIL COM pyautogui
