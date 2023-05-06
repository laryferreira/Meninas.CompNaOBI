# função para calcular o n-ésimo termo da sequência de Fibonacci
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# número de casos de teste
t = int(input())

# processamento dos casos de teste
for i in range(t):
    n = int(input())
    # cálculo do n-ésimo termo da sequência de Fibonacci
    resultado = fib(n)
    # impressão do resultado
    print("Fib({}) = {}".format(n, resultado))
