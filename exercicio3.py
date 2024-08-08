# Exercício 03 
# Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus quadrados. 
# Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação. 

def soma_dos_quadrados(numero1: float, numero2: float) -> float:
    """A função recebe dois numeros e devolve a soma dos seus quadrados"""
    a = numero1 ** 2
    b = numero2 ** 2
    return a + b

numero1 = float(input('Primeiro Número: '))
numero2 = float(input('Segundo Número: '))
print(f'Soma de {numero1} ao quadrado e {numero2} ao quadrado é {soma_dos_quadrados(numero1, numero2)}')