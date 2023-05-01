''''Olá meninas, tudo bem?
Nesse problema, temos três entradas e devemos descobrir a idade do outro filho de dona Mônica (que deverá ser o mais velho).
''''

M = int(input()) #idade de dona mônica
A = int(input()) #idade de um filho (a)
B = int(input()) #idade de um filho (b)

C = M - (A + B) #idade de dona mônica - soma da idade dos outros filhos

idades = [A,B,C] #organizando em uma lista os valores
print(max(idades)) #selecionando o maior valor (max) entre os filhos
