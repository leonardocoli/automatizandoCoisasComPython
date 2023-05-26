#passo1: importas a base de dados

#passo2: visualizar a base de dados
    #entender as informa'coes disponiveis
    #procurar os erros da base de dados

#passo3: tratamento de dados
    #valores no formato errado
    #valores vazios

#passo4: analise inicial; ex: entender como estao as notas dos clientes

#passo5: analise completa; ex: tracar o perfil ideal de clientes, entender como cada caracteristica do cliente impacta na nota

#SOL:
#passo1:

import pandas as pd


tabela = pd.read_csv("nome do arquivo", encoding="latin", sep=";") #encoding="latin" pra ler com termos latinos

#passo2:

tabela = tabela.drop("nome de quem vc quer deletar", axis="numero da linha")
display(tabela)

#passo3:
tabela["titulo de uma coluna"] = pd.to_numeric((tabela["titulo de uma coluna"], errors='coerce'))

tabela = tabela.dropna()
print(tabela.info())


#passo4:
tabela.describe()

display(tabela.describe)


#passo5:
import plotly.espress as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="parametro", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()