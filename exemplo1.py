# --------------------------TIPOS DE DADOS

# int
idade = 21
# float
nota = 8.25
# str
nome = 'Paulo'
# bool
valor = True
valor = False

# --------------------------função type (verifica o tipo de dado de uma variável)

print(type(nota))
print(type(nome))
if type(nota) == float:
    print('Tipo de dados correto')
else:
    print('Tipo de dados errado')

# ---------------------------casting (conversão de tipo de dados)

valor = 40.79                               # converte para int
valor = int(valor)

valor = 30                                  # converte para float
valor = float(valor)
print(valor)

valor = 30                                  # coverte para str
valor = str(valor)
print(valor)
print(type(valor))

idade = int(input('Digite a idade: '))

# -------------------------Operadores Aritméticos

# Potência            **          (Prioridade 1)

# Multiplicação       *           (Prioridade 2)
# Divisão             /
# Divisão Inteira     //
# Resto de Divisão    %

# Adição              +           (Prioridade 3)
# Subtração           -

# -------------------------Operadores Relacionais

# Maior               >
# Menor               -
# Maior ou igual      >=
# Menor ou igual      <=
# Igual               ==
# Diferente           !=

# -----------------------------Operadores Lógicos

# not             (Prioridade 1)
# and             (Prioridade 2)
# or              (Prioridade 3)

# ------------------------------------------------------------------------------------------------------------

# ----------------------------Estrutura Condicional Simples (if)
if idade >= 18:
    print('Maior de idade')

# ----------------------------Estrutura Condicional Composta (if-else)
if idade >= 18:
    print('Maior de idade')
else
    print('Menor de idade')

# -----------------------------Estrutura Condicional Encadeada (if-elif-else)
if idade >= 40:
    print('Idade maior que 40')
if idade >= 30:
    print('Idade maior que 30')
if idade >= 20:
    print('Idade maior que 20')
else
    print('Outra idade')

# -----------------------------Estrutura de Seleção Múltipla (match-case)
match idade:
    case 17 | 18 | 19:
        print('Idade igual a 17, 18 ou 19')
    case 20:
        print('Idade igual a 20')
    case 30:
        print('Idade igual a 30')
    case _:
        print('Outra idade')

# ----------------------------------------------------------------------------------------------------------

# ------------------------------Estrutura de repetição while
# ------------------------------Solicitar a idade de 5 pessoas
cont = 1
while cont <= 5:
    idade = int(input('Digite uma idade: '))
    cont += 1

# ------------------------------Exibir os números de 1 a 10
cont = 1
while cont <= 10:
    print(cont)
    cont += 1

# Estrutura de repetição for
# -----------------------------Exibir os números de 1 a 10
for cont in range(1, 11):
    print(cont)

# -----------------------------Exibir os números de 1 a 10
for cont in range(1,11,2):                  # range (inicio, fim, incremento)
    print(cont)

# -----------------------------Exibir os números de 1 a 10
for cont in range(2,11,2):                  # range (inicio, fim, incremento)
    print(cont)

# -----------------------------Solicitar a idade de várias pessoas até que seja digitada uma negativa
idade = 0
while idade >= 0:
    idade = int(input('Idade: '))

# -----------------------------Solicitar a idade de várias pessoas até que seja digitada uma negativa
while True:
    idade = int(input('Idade: '))
    if idade < 0:
        break

# -----------------------------Calcular a média da idade
soma = 0                 # somadora
cont = 0                 # contagem

while True:
    idade = int(input('Idade: '))
    if idade < 0:
        break
    soma += idade
    cont += 1
media = soma / cont
print(f'Média da idade: {idade:.2f}')