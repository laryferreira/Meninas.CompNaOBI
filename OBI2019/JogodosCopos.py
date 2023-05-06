n = int(input())  # número de movimentos
pos = input()     # posição inicial da moeda

for i in range(n):
    move = int(input())  # tipo de movimento efetuado pela banca
    if move == 1:
        if pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'
    elif move == 2:
        if pos == 'B':
            pos = 'C'
        elif pos == 'C':
            pos = 'B'
    elif move == 3:
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'

print(pos)  # posição final da moeda após os movimentos
