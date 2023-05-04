'''Olá meninas, tudo bem?
Nesse problema, devemos printar quantos pontos o robô fez sabendo a distância dele para o início da quadra sabendo que:
- Se a distância for menor ou igual a 800, a cesta vale 1 ponto
- Se a distância for entre 800 e 1400, a cesta vale 2 pontos
- Se a distância for entre 1400 e 2000, a cesta vale 3 pontos
'''

d = int(input())    # aqui a variável n recebe um inteiro
if d <= 800 :
    print(1)
elif d <= 1400 :  
    print(2)
else:
    print(3)

''' percebam que na linha 11 eu não coloquei a condição de D ser maior que 800 (d > 800) porque se o número for menor ou igual a 800, a linha 10 será executada e o programa será
 interrompido, sem passar pelas outras condições'''