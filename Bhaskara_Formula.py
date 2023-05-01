# Apenas números inteiros
print("\nDigite os coeficientes de uma equação de segundo grau, de acordo com a fórmula 'ax² + bx + c = 0' :")
a = int(input("\na: "))
b = int(input("b: "))
c = int(input("c: "))
if a == 0:
    print("Sua equação não é de segundo grau, pois o valor 'a' é igual a 0.")
elif b == 0:
    if c > 0 and a > 0:
        print("No caso 'a² + c = 0', o valor 'c' é positivo, logo os valores de x não são reais.")
    elif c > 0 > a or a > 0 > c:
        x1 = (-c/a) ** 0.5
        x2 = -1 * ((-c/a) ** 0.5)
        print("\nOs valores de x são: \nx1 = {}\nx2 = {}".format(x1, x2))
    else:
        print("No caso 'a² + c = 0', ambos os valores 'a' e 'c' são negativos, logo os valores de x não são reais.")
elif c == 0:
    x1 = 0
    x2 = -b/a
    print("\nOs valores de x são: \nx1 = {}\nx2 = {}".format(x1, x2))
else:
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / 2 * a
    x2 = (-b - delta ** 0.5) / 2 * a
    print("\nOs valores de x são: \nx1 = {}\nx2 = {}\nO valor de delta é {}".format(x1, x2, delta))
