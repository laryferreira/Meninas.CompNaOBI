'''Olá, meninas! Tudo bem?
Esse problema pode parecer confuso mas, usando a imagem para compreender a lógica dele, facilita muito!

Vamos fazer algumas análises sobre a imagem e o problema (tente compreender cada tópico antes de passar para o próximo)!
- As lajotas do tipo 1 possuem 1 metro na vertical e 1 metro na horizontal;
- As lajotas do tipo 2 possuem 1 metro na vertical e 1/2 metro na horizontal;
- As latojas do tipo 3 possuem 1/2 metro na vertical e 1/2 metro na horizontal;
- Como diz o problema, sempre serão usadas 4 lajotas do tipo 3 que ficarão nos cantos do piso (note que, realmente, na imagem só são usadas 4 desse tipo!);
- As lajotas do tipo 2 só são usadas nos lados do piso, nunca no meio dele!

ANALISANDO A QUANTIDADE DE LAJOTAS DO TIPO 2 (lembre de ver a imagem para entender melhor):
- Como estamos contabilizando a quantidade de lajotas do tipo 2, vamos analisar só os lados do piso;
- A largura do piso é 3m então somando a medida vertical das lajotas do tipo 2 e 3, o resultado deve ser 3;
- Como sabemos que foram usadas 2 do tipo 3, elas ocuparam 1 metro na vertical (2 * 1/2 = 1), então sobram 2m para serem preenchidos pelas do tipo 2;
- Sabendo que as do tipo 2 têm 1 metro na vertical, para preencherem os dois metros, serão usadas 2 lajotas;
- Fizemos essa análise apenas para um lado, como temos dois lados, multiplicamos esse valor por 2 (então foram usadas 4 lajotas);
- A expressão que representaria o que calculamos até agora é: (L - 1) * 2;
- O mesmo raciocínio pode ser usado analisando o comprimento, com a expressão sendo: (C - 1) * 2;
- Somando a quantidade de lajotas de todos os lados, temos: (L - 1) * 2 + (C - 1) * 2;

ANALISANDO A QUANTIDADE DE LAJOTAS DO TIPO 1 (lembre de ver a imagem para entender melhor);
- Podemos ver pela imagem que temos três fileiras de lajotas (tipo 1) que vão de uma ponta do piso até a outra (encostam nas duas extremidades);
- Cada uma dessas 3 fileiras possui 5 lajotas, então, para calcular elas, basta multiplicar 3 com 5 (L * C), totalizando 15;
- Além dessas fileiras, temos 2 fileiras (repare que 2 = 3-1) com 4 lajotas em cada (4 = 5-1), multiplicando 4 com 2 ((L - 1)*(C - 1)),
temos a quantidade de lajotas nessas fileiras (8 lajotas);
- Agora basta somar: 15 + 8 = 23;
- A expressão que representaria isso é: (L * C) + (L - 1) * (C - 1);
'''

l = int(input())
c = int(input())
print((l*c) + (l - 1)*(c - 1))
print((l - 1)*2 + (c - 1)* 2)