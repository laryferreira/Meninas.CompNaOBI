'''Oi meninas, tudo bem? 
Nesse problema temos que fazer um sisteminha simples de classificação com condicionais,
comparando notas e suas respectivas letras. A tabela já deixa bem claro o que devemos fazer.''''

n = int(input()) #entrada
if n == 0: #primeiro caso
    print("E")
elif n >= 1 and n <= 35: #segundo caso
    print("D")
elif n >= 36 and n <= 60: #terceiro caso
    print("C")
elif n >= 61 and n <= 85: #quarto caso
    print("B")
elif n >= 86 and n <= 100: #quinto caso
    print("A")
