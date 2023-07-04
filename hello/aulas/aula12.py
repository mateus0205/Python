nome = str(input('Qual o seu nome? ')).capitalize()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana cláudia':
    print('Nome feminimo')
else: 
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')