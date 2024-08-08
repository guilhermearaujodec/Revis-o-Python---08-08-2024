# Exercício 02 
# Implemente  a  função  quadrado  que  recebe  um  número  e  retorna  o  resultado  desse  número  ao quadrado.

def funcao_quadrado(numero):
    """Calcula o valor ao quadrado do número"""
    return numero ** 2

numero = float(input('Insira o Número: '))
print(f'O quadrado de {numero} é {funcao_quadrado(numero)}')
