# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade
# ate 9 anos: mirim, 14 infantil, 19 junior, 20 senior, acima: master
from datetime import date
hoje = date.today().year
idade = int(input('Digite a sua data de nascimento: '))
if (hoje - idade) <= 9:
    print(f'A pessoa nascida no ano {idade} tem {hoje-idade} anos, é da Categoria Mirim.')
elif (hoje - idade) > 9 and (hoje - idade)<= 14:
    print(f'A pessoa nascida no ano {idade} tem {hoje-idade} anos, é da Categoria Infantil.')
elif(hoje - idade)> 14 and (hoje - idade) <=19: 
    print(f'A pessoa nascida no ano {idade} tem {hoje-idade} anos, é da Categoria Junior.')
else: 
   print(f'A pessoa nascida no ano {idade} tem {hoje-idade} anos, é da Categoria Senior.')
    