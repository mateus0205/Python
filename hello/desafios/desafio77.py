# crie um programa que tenha uma tupla com varias palavras,
# depois disso, voce deve mostrar, para cada palavras, quais são suas vogais
tupla = ('arroz', 'banana', 'carne', 'drive', 'escola', 'frango')
vogais_por_palavra = {}
# perccore cada palavra da tupla
for palavra in tupla:
    vogais = []
    # perccore cada caractere da palavra
    for caractere in palavra:
        # verifica se o caractere é vogal
        if caractere.lower() in "aeiou":
            # adiciona a vogal a lista de vogais
            vogais.append(caractere)
    # adiciona a lista de vogais da palavra ao dicionario        
    vogais_por_palavra[palavra] = vogais
    
# exibe as vogais encontradas em cada palavra    
for palavra, vogais in vogais_por_palavra.items():
    print(f'Vogais da palavra: {palavra} {vogais}')