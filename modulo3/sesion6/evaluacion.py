num1 = float(input("ingresa un numero: "))
num2 = float(input("ingresa un numero: "))
num3 = float(input("ingresa un numero: "))


if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1    
if num2 < num3:
    num2, num3 = num3, num2
print(f"El orden de los numero es: {num1} {num2} {num3}")               