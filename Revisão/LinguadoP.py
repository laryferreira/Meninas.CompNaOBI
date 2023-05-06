mensagem_codificada = input()

mensagem_decodificada = ""
i = 0
while i < len(mensagem_codificada):
    if mensagem_codificada[i] == "p":
        mensagem_decodificada += mensagem_codificada[i+1]
        i += 2
    else:
        mensagem_decodificada += mensagem_codificada[i]
        i += 1

print(mensagem_decodificada)
''''A ideia é percorrer a mensagem codificada caractere por caractere e, sempre que encontrar a letra "p", 
adicionar à mensagem decodificada o próximo caractere (que corresponde à letra original). 
Caso contrário, adiciona o caractere original à mensagem decodificada.
A variável i é usada para controlar a posição atual na mensagem codificada enquanto percorre os caracteres.''''
