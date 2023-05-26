import time
import unicodedata2
from selenium import webdriver
import pandas as pd
from time import *



tabela = pd.read_excel("C:/Users/Leonardo Coli/Documents/arquivos_p_projetos_python/automacao_web_de_infos/commodities.xlsx")

navegador = webdriver.Chrome(executable_path="C:/Users/Leonardo Coli/AppData/Local/Programs/Python/Python311/chromedriver.exe")

print(tabela)
for i in range(len(tabela.Produto)):

    produto = produto = unicodedata2.normalize('NFD', tabela.Produto[i]).encode('ascii', 'ignore').decode('utf8')
    print(produto)

    site = "https://www.melhorcambio.com/{}-hoje".format(produto)
    navegador.get(site)

    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace(".", "").replace(",", ".")
    cotacao = float(cotacao)
    print(cotacao)

    tabela.loc[i, 'Preço Atual'] = cotacao


    #refazer essa estrutura que nao esta funcionando:::::::::
#    if ('Preço Atual' <= 'Preço Ideal'):
#        tabela.loc[i, 'Comprar'] = str("SIM")
#    else:
#       tabela.loc[i, 'Comprar'] = str("NAO")



print(tabela)
