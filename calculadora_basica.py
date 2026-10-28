# ========================================================
# Calculadora Simples em Python
# Operadores básicos: Soma (+), Subtração (-),
# Multiplicação (*) e Divisão (/)
# ========================================================

print("==========================================")
print("      CALCULADORA BÁSICA EM PYTHON        ")
print("==========================================")
print("Operações disponíveis:")
print("  +  : Adição (Soma)")
print("  -  : Subtração")
print("  *  : Multiplicação")
print("  /  : Divisão")
print("==========================================")

# 1. Leitura dos números e do operador
num1 = float(input("Digite o primeiro número: "))
operador = input("Escolha a operação (+, -, *, /): ").strip()
num2 = float(input("Digite o segundo número: "))

# 2. Execução da operação escolhida
if operador == "+":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")

elif operador == "-":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")

elif operador == "*":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")

elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\n[ERRO] Não é possível dividir por zero (ZeroDivisionError)!")

else:
    print(f"\n[ERRO] Operador '{operador}' é inválido! Escolha +, -, * ou /.")
