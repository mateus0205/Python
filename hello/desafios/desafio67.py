# faça um program que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
n = 1
while n>=1:
    n = int (input('\nQual valor você deseja que seja mostrada a tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        multi = n * c
        print(f'{n} x {c} =  {multi}')
    