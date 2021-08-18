print('CALCULADORA!')
print('+ adição')
print('- subtração')
print('/ divisão')
print('* multiplicação')
print('Pressione outra tecla para sair...')

op = input('Qual operação deseja realizar?:')
if op == '+' or op == '-' or op == '/' or op == '*':
    X = int(input('Digite o primeiro valor:'))
    Y = int(input('Digite o segundo valor:'))

if (op == '+'):
    res =  X + Y
    print('O resultado de {} + {} = {}' .format(X, Y, res))
elif (op == '-'):
    res = X - Y
    print('O resultado de {} - {} = {}' .format(X, Y, res))
elif (op == '/'):
    res = X / Y
    print('O resultado de {} / {} = {}' .format(X, Y, res))
elif (op == '*'):
    res = X * Y
    print('O resultado de {} * {} = {}'.format(X, Y, res))
else:
    print('operação inválida')

print('Encerrando o programa...')