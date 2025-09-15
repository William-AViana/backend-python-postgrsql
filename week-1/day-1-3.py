numbers_user = input('Digite dois números separados por (, ): ').split(', ')

operator = input('Qual operação você quer fazer? '
                '(1) Soma \n (2) Subtração \n ' 
                '(3) Divisão \n (4) Multiplicação \n '
                'Opção: ')

if(operator == '1'):
    result_sum = sum(int(num) for num in numbers_user)
print(result_sum)

