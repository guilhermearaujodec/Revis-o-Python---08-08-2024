# Exercício 01
# Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois números.
# Lembre-se que para retornar um resultado a função deve utilizar a instrução return.


def somar(numero1: float, numero2: float) -> float:
    """retorna o numero ao quadrado"""
    return numero1 + numero2
a = float(input('Primeiro Número: '))
b = float(input('Segundo Número: '))
print(f'Soma de {a} e {b} é {somar(a, b)}')
