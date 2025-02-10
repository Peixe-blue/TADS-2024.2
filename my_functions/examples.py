import pandas as pd

#a seta é para mostrar que vai retornar uma tabela
def create_example() -> pd.DataFrame:
    """ Create a dataframe exemple. 

    Returns:
        pd.DataFrame: Name and scores.
        #Sempre escrever tudo em inglês
    """
    tabela = pd.DataFrame({
        'Nome': ['Renata', 'Anderson', 'Paulo'],
        'Nota1': [10, 5, 9],
        'Nota2': [7, 3, 9]
    })

    return tabela