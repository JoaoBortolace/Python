from time import perf_counter_ns


def factorial(n=1):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Digite um número: '))
tempo_inicial = perf_counter_ns()
print(f'{num}! = {factorial(num)} ')
tempo_final = perf_counter_ns()
print(f"{(tempo_final - tempo_inicial)} nanosegundos gastos para calcular")

tempo_inicial = perf_counter_ns()
print(f'{num}! = {fatorial(num)}')
tempo_final = perf_counter_ns()
print(f"{(tempo_final - tempo_inicial)} nanosegundos gastos para calcular")
