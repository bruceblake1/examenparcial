#BUCLE DE UNA TABLA DE MULTIPLICAR
resp = "Si"
while (resp!="no"):
    num = int(input("Digitar un número: "))
    for i in range (1,21):
        mult = num * i
        print(num,"x", i , "es igual a", mult)
    print("Desea multiplicar otro número (si/no) ? :")
    resp= input()