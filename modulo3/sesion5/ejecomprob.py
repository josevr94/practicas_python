num = int(input("ingresa un numero: "))
facotiral = 1
while num > 0:
    facotiral *= num * (num - 1)
    num = num - 2 
    print(facotiral)
    print(num)
print(facotiral)    
    
     