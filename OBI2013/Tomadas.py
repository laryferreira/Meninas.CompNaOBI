'''Olá, meninas! Tudo bem?
Para esse problema, é importante perceber que a quantidade de aparelhos que podem ser conectados vai ser a quantidade de tomadas - 3;
Mas por que isso?
Bom, a segunda régua estará conectada em uma tomada da primeira, a terceira estará conectada em uma tomada da segunda, e a quarta estará conectada em uma da terceira
'''

r = list(map(int, input().split()))
print(sum(r)-3)