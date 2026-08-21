print("Calculadora simples")
numero1=float(input("Digite o primeiro número:"))
numero2=float(input("Digite o segundo número:"))
print("soma:", numero1+numero2)
print("subtração:", numero1-numero2)
print("multiplicação:", numero1 * numero2)
if numero2 != 0:
     print("divisão:", numero1/numero2)
else:
     print("Não é possível dividir por zero.")