from flask import Flask, request

app = Flask(__name__)

lista_operacoes = ['+ 1', '- 2', 'x 3', '÷ 4']

@app.route('/')
def homepage():
    # Monta a lista de operações em texto
    texto = 'Bem-Vindo\n\nOperações disponíveis:\n'
    for i in lista_operacoes:
        texto += f'{i}\n'
    texto += '\nUse /calc?op=+&n1=10&n2=5 para calcular'
    return texto

@app.route('/calc')
def calc():
    op = request.args.get('op', '').strip()
    n1_str = request.args.get('n1', '')
    n2_str = request.args.get('n2', '')
    
    if not op or not n1_str or not n2_str:
        return 'Erro: Faltam parâmetros. Use /calc?op=+&n1=10&n2=5', 400
    
    try:
        num1 = float(n1_str)
        num2 = float(n2_str)
    except ValueError:
        return 'Erro: n1 e n2 precisam ser números', 400
    
    if op == '+' or op == '1':
        return f'{num1} + {num2} = {num1 + num2}'
    
    elif op == '-' or op == '2':
        return f'{num1} - {num2} = {num1 - num2}'
    
    elif op == 'x' or op == '3':
        return f'{num1} x {num2} = {num1 * num2}'
    
    elif op == '÷' or op == '4':
        if num2 == 0:
            return 'Erro: Divisão por zero', 400
        return f'{num1} ÷ {num2} = {num1 / num2}'
    
    else:
        return f'Erro: Operação inválida\nOperações válidas:\n' + '\n'.join(lista_operacoes), 400

if __name__ == '__main__':
    app.run(debug=True)
