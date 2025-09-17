from functools import reduce

numbers_user = list(input('Digite dois números separados por (, ): ').split(', '))

operator = input('Qual operação você quer fazer? '
                '(1) Soma \n (2) Subtração \n ' 
                '(3) Divisão \n (4) Multiplicação \n '
                'Opção: ')

numbers_user_int = [int(num) for num in numbers_user]

def soma(numbers_user_int):
    result = sum(int(num) for num in numbers_user_int)
    print(result)

def subtracao(numbers_user_int):
    result = reduce(lambda acumulador, elemento_atual: acumulador - elemento_atual, numbers_user_int)
    print(result)

def divisao(numbers_user_int):
    result = reduce(lambda acumulador, elemento_atual: acumulador / elemento_atual, numbers_user_int)
    print(result)

def multiplicacao(numbers_user_int):
    result = reduce(lambda acumulador, elemento_atual: acumulador * elemento_atual, numbers_user_int)
    print(result)

match operator:
    case "1":
        soma(numbers_user_int)
    case "2":
        subtracao(numbers_user_int)
    case "3":
        divisao(numbers_user_int)
    case "4":
        multiplicacao(numbers_user_int)
