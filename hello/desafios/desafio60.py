num = int(input('Digite um número para calcular o fatorial: '))
fat = 1
while num >= 1:
   fat = fat * num
   num -= 1
print(f'o fatorial será: {fat} ')
