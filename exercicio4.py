# Exercício 04 
# Implemente  a  função  media,  que  recebe  três  valores  numéricos  e  retorna  a  média  aritmética  dos 
# valores.

def media(numero1: float, numero2: float, numero3: float) -> float:
    """A função recebe 3 números e calcula a média deles"""
    
    return (numero1 + numero2 + numero3) / 3

numero1 = float(input('Primeiro Número: '))
numero2 = float(input('Segundo Número: '))
numero3 = float(input('Terceiro Número: '))
print(f'A média aritmética dos números {numero1}, {numero2} e {numero3} é {media(numero1, numero2, numero3)}')