# Crie uma tabela preenchida com os 20 primeiros colocados da tabela do campeonato brasilerio
# apenas os 5 primeiros colocados
# os ultimos 4 colocados da tabela
# uma lista de times em ordem alfabetica 
# em que posicao esta o time do cuiaba 
brasileirao = ('botafogo', 'gremio' , 'flamengo', 'palmeiras', 'fluminense', 'inter', 'bragantino', 
              'fortaleza', 'atletico-pr', 'atletico-mg', 'sao paulo', 'cruzeiro', 'santos', 
              'bahia', 'corintians', 'cuiaba', 'goias', 'vasco', 'america', 'coritiba')
print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
print()
print(f'Os 4 ultimos colocados são {brasileirao[16:20]} ')
print()
print(f'O brasileirão em ordem alfabetica fica {sorted(brasileirao)}')
print()
print(f'A cuiaba esta na posição {brasileirao.index("cuiaba")+1}')
print()