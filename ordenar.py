print("------------------------------")
print("-----------Ordenar------------")
print("------------------------------")

# input
a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercero número: "))

# processing and output
if a > b and a > c:
    if b > c:
        print("El número mayor es "+str(a)+", el número de la mitad es "+str(b)+" y el número menor es "+str(c))
    else:
        print("El número mayor es "+str(a)+", el número de la mitad es "+str(c)+" y el número menor es "+str(b))
elif c > a and c > b:
    if a > b:
        print("El número mayor es "+str(c)+", el número de la mitad es "+str(a)+" y el número menor es "+str(b))
    else:
        print("El número mayor es "+str(c)+", el número de la mitad es "+str(b)+" y el número menor es "+str(a))

else:
    if b > a and b > c:
        if a > c:
            print("El número mayor es "+str(b)+", el número de la mitad es "+str(a)+" y el número menor es "+str(c))
        else:
            print("El número mayor es "+str(a)+", el número de la mitad es "+str(c)+" y el número menor es "+str(a))
