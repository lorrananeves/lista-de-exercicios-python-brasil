"""
Exercício 13 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
Mostrar a área com 1 casa decimal.

    >>> from secao_01_estrutura_sequencial import ex_13_peso_ideal_mulher_e_homem
    >>> ex_13_peso_ideal_mulher_e_homem.input = lambda k: '1.62'
    >>> ex_13_peso_ideal_mulher_e_homem.calcular_peso_ideal()
    Seu peso ideal é 55.9 kg, se você for mulher
    Seu peso ideal é 59.8 kg, se você for homem
    >>> ex_13_peso_ideal_mulher_e_homem.input = lambda k: '1.80'
    >>> ex_13_peso_ideal_mulher_e_homem.calcular_peso_ideal()
    Seu peso ideal é 67.1 kg, se você for mulher
    Seu peso ideal é 72.9 kg, se você for homem

"""


def calcular_peso_ideal():
    """Escreva aqui em baixo a sua solução"""
    n1=float(input('Digite aqui a sua altura: '))
    n2=((72.7*n1)-58)
    n3=((62.1*n1)-44.7)
    print(f'Seu peso ideal é {"%.1f" %n3} kg, se você for mulher')
    print(f'Seu peso ideal é {"%.1f" %n2} kg, se você for homem')