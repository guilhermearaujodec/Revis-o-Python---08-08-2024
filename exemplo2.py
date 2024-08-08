"""
DOCSTRING
- Uma docstring tem como objetivo explicar o funcionamento de uma função.
- Uma docstring é um comentário sempre localizado na primeira linha da função.
- Uma docstring deve estar sempre entre 3 aspas duplas.
- Uma docstring contribui para a documentação de um código fonte e para seu entendimento.

ANOTAÇÃO DE TIPO
- Anotação de tipo (type hint) são usadas para indicar os tipos de dados das variáveis e
  dos parâmetros de funções.
- O objetivo é tornar o código mais legível e organizado.
"""

def calcular_media(quantidade: int) -> float:
    """
    Calcula a média de idade de pessoas.
    """
    if type(quantidade) != int:
        print('Erro. o parametro deve ser do tipo int')
    else:
        soma = 0
        for a in range(quantidade):
            idade = int(input('Idade: '))
            soma += idade
        media = soma / quantidade
        return media


m = calcular_media("ereererer")
print(f'Média das idade: {m}')

media = calcular_media(5)
print(f'Media: {media}')

calcular_media()

nome: str = 'Paulo'
altura: float = 1.70