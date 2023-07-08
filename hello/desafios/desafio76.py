# CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM OS NOMES DOS PRODUTOS E SUE RESPECTIVOS PREÇOS NA SEQUENCIA
# NO FINAL, MOSTR UMA LISTAGEM DE PREÇOS ORGANIZADOS DE FORMA TABULAR
from tabulate import tabulate 
tupla = [('banana', 'R$ 5'), ('mamao', 'R$ 10'),('limao','R$ 3'),('maça','R$ 13'),('pera','R$ 15')]
print('-'*18)
print(tabulate(tupla, headers=["Produto", "Preço"]))
print('-'*18)
