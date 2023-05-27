notas = []

for i in range(1, 5):
    nota = float(input(f"Nota{i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print(f"A média final é {media:.2f}. A sua maior nota foi {maior_nota:.2f} e a menor foi {menor_nota:.2f}.")
