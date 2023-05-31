frase = input().split()
frase_decodificada = list()

for palavra in frase:
    palavra_decodificada = ''
    for index in range(1, len(palavra), 2):
        palavra_decodificada = palavra_decodificada + palavra[index]
    frase_decodificada.append(palavra_decodificada)
    
print(' '.join(frase_decodificada))