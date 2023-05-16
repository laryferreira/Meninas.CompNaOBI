'''Olá, meninas! Tudo bem?
Sabendo que o vice-campeão é a pessoa com a segunda maior pontuação, basta ordenar a lista em ordem crescente e imprimir o segundo valor da lista!'''

p = list(map(int, input().split()))
p = sorted(p)   # a função sorted organiza a lista em ordem crescente
print(p[1])     # ATENÇÃO! Lembrem que a contagem em python começa em 0, então o segundo elemento da lista está na posição 1