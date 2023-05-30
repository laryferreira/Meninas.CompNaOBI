entrada = list(map(int, input().split()))
p1 = entrada[0]
c1 = entrada[1]
p2 = entrada[2]
c2 = entrada[3]

esquerda = p1*c1
direita = p2*c2

if esquerda == direita:
    print(0)
elif esquerda > direita:
    print(-1)
else:
    print(1)