# Exercício 05 
# Implemente  a  função  calcular_salario,  que  recebe  o  salário  atual  de  um  funcionário  e  retorna  o 
# salário com um reajuste de aumento, sendo que: 
# - Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento. 
# - Caso contrário, o funcionário receberá 15% de aumento.

def calcular_salario(salario: float) -> float:
    """Calcula os ajustes salariais"""
    if salario >= 2000:
        return (salario * 7/100) + salario
    else:
        return (salario * 15/100) + salario

salario = float(input('Insira o Salário: '))
print(f'O salário com o reajuste será de {calcular_salario(salario)}')
