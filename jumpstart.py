import pandas as pd

# assim se cria uma tabela
tabela = pd.DataFrame({
    'Nome': ['Renata', 'Anderson', 'Paulo'],
    'Nota1': [10, 5, 9],
    'Nota2': [7, 3, 9]
})

#selecionar as colunas ou mudar a tsbela
#utiliza dois cochetes para retornar a tabela, e não um vetor que é com um conlchete
tabela[['Nota2', 'Nome', 'Nota1']]

#filtrando as tabelas
tabela.query('Nota1 > 7')
#só pega a linha de renata
tabela.query('Nome == "Renata"')
tabela.query('Nome in ("Renata", "Paulo")')

#quebrando o código para ficar mas legivel
#1
tabela \
    .query('Nota1 > 7')

#2
(
    tabela
        .query('Nota1 > 7')
)

#criando colunas
tabela \
    .assign(
        media = lambda x: (x['Nota1'] + x['Nota2'])/2

#não mostra a tabela, apenas o resultado da média    
)
(tabela['Nota1'] + tabela['Nota2'])/2