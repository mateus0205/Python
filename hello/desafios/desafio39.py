# Faça um progrma que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar no serviço militar.
# Se é a hora de se alistar
# Se passou do tempo de alistamento
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
alistamento = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = alistamento - ano
if idade > 18:
    print(f'Você perdeu o tempo de alistamento em {idade-18} anos!')
elif idade == 18:
    print(f'Está no seu ano de alistar!')
elif idade < 18:
    print(f'Você ainda não esta na hora de se alistar, faltam {18-idade} anos')