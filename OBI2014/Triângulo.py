'''Olá meninas! Tudo bem?

Nessa questão, antes de começar o código, é importante analisar se você sabe a condição para um triângulo ser formado

Essa condição é : a soma da medida de dois segmentos precisa ser maior q a medida do terceiro segmento
'''

n = list(map(int, input().split()))  # a entrada será composta por 4 números separados por espaço. O "split" mostra como os elementos da lisita estão separados no "input" então, a cada espaço, um novo elemento é criado na lista. 

n = sorted(n)   # a função "sorted" vai ordenar a lista em ordem crescente

if (n[0] + n[1] > n[2] or n[1] + n[2] > n[3]):  
    print('S')
else:
    print('N')