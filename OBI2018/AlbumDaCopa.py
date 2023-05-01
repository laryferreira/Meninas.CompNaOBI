''''Olá meninas, tudo bem?
Percebam que o nosso papel nesse problema é contar quantas figurinhas faltam para completar o álbum. 
Mas cuidado! Devemos considerar que há figurinhas repetidas.
Vamos definir nossas variáveis:
N = espaços e figurinhas totais
M = número de figurinhas compradas
x = cada figurinha repetida''''

N = int(input())
M = int(input())
figurinhas_compradas = set() 
for i in range(M):
    x = int(input())
    figurinhas_compradas.add(x)

faltam = n - len(figurinhas_compradas)

print(faltam)

''''
set() é um tipo de estrutura de dados em Python que armazena um conjunto de elementos únicos e não ordenados.

Em outras palavras, um conjunto é uma coleção de itens que não pode conter elementos repetidos.
Você pode criar um conjunto vazio usando set() ou pode inicializá-lo com valores, como set([1,2,3]) ou simplesmente {1,2,3}. 
É importante notar que os elementos em um conjunto podem ser de qualquer tipo imutável, incluindo números, strings e tuplas.
No código que apresentei anteriormente, usamos set() para criar um conjunto vazio que será preenchido com as figurinhas já compradas. 
Usamos o método add() para adicionar cada figurinha já comprada ao conjunto figurinhas_compradas.
''''
