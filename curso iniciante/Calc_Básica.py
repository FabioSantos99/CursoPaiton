print('Calculadora')

print("-" * 10)

print("Escolha a operação: \n"
      "1 - Adição \n"
      "2 - Subtração \n"
      "3 - Multiplicação \n"
      "4 - Divisão")

num1 = int(input("Digite num1:"))
num2 = int(input("Digite num2: "))
op = input("operador: ")
resultado = 0
if op == '1':
    resultado = num1 + num2
elif op == '2':
    resultado = num1 - num2
elif op == '3':
    resultado = num1 * num2
elif op == '4':
    resultado = num1 / num2
else:
    print('Caractere não permitido')


print('Resultado é: ', resultado)