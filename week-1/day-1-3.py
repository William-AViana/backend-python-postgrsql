numbers_user = input('Digite dois números separados por (, ): ').split(', ')

operator = input('Qual operação você quer fazer? '
                '(1) Soma \n (2) Subtração \n ' 
                '(3) Divisão \n (4) Multiplicação \n '
                'Opção: ')

        
if(operator == '1'):
    def soma(numbers):
        result = sum(int(num) for num in numbers)
        print(result)

    soma(numbers_user)
