# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
numeros = []  # lista vazia para armazenar os números digitados

while True:
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)  # adiciona o número digitado à lista

    continuar = input("Deseja continuar digitando valores? (s/n) ")
    if continuar.lower() != "s":
        break

media = sum(numeros) / len(numeros)  # calcula a média dos valores
maior = max(numeros)  # encontra o maior valor na lista
menor = min(numeros)  # encontra o menor valor na lista

print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")


#REFAZER