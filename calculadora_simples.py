# Calculadora simples

lista_operacoes = ['+ 1', '- 2', 'x 3', '÷ 4']
print('Bem-Vindo')
input('Pressione Enter para começar')
while True:
    print('Operações')
    for i in lista_operacoes:
        print(i)
    operacao = str(input('digite a operação: '))
    num1 = float(input('digite o 1° número: '))
    num2 = float(input('digite o 2° número: '))

    if operacao == '+' or operacao == '1':
        print(f'{num1} + {num2} = {num1 + num2}')

    elif operacao == '-' or operacao == '2':
        print(f'{num1} - {num2} = {num1 - num2}')

    elif operacao == 'x' or operacao == '3':
        print(f'{num1} x {num2} = {num1 * num2}')

    elif operacao == '÷' or operacao == '4':
        print(f'{num1} ÷ {num2} = {num1 / num2}')
    
