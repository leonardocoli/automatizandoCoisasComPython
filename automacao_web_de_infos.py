#passo1: abrir o navegador
#passo2: importar base de dados
#passo3: para cada produto da base de dados
#passo4: pegar preco atual do produto
#passo5: atualizar o preco na base de dados
#passo6: decidir quais produtos comprar
#passo7: exportar base de dados atualizada

#baixar WEBDRIVER do microsoft edge
#passo1
from selenium import webdriver
#passo2
import pandas as pd

tabela = pd.read_excel('C:/Users/Leonardo Coli/Documents/arquivos_p_projetos_python/automacao_web_de_infos/commodities.xlsx')
print(tabela)

navegador = webdriver.Chrome(executable_path="C:/Users/Leonardo Coli/AppData/Local/Programs/Python/Python311/chromedriver.exe")

#entrar no site melhor cambio

navegador.get("https://www.melhorcambio.com/milho-hoje")

#pegar cotacao do item que quero (milho) e tratar o dado

cotacao_milho = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_milho = cotacao_milho.replace(".","").replace(",",".")
cotacao_milho = float(cotacao_milho)
print(cotacao_milho)
                                                            #.send_keys("bla bla") -> escrever nele
                                                            #.click() -> clicar nele
                                                                #.get_atribute() -> pegar info
# #dar um insert da cotacao atual na tabela

tabela.loc[0,'Preço Atual'] = cotacao_milho

##tabela.loc["linha,coluna"] = cotacao_milho

if 'Preço Atual' <= 'Preço ideal':
    tabela.loc[0, 'Comprar'] = str("SIM")
else:
    tabela.loc[0, 'Comprar'] = str("NAO")

print(tabela)

#falta generalizar codigo!!