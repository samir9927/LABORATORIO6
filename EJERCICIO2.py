listaNumeros1=set()
listaNumeros2=set()
conjunto1 = int(input("Cuantos datos tiene el conjunto1: "))

for i in range (conjunto1):
    A=int(input("Ingrese numero: "))
    listaNumeros1.add(A)
print("El conjunto 1 es: ", listaNumeros1)

print("---------------------------------")

conjunto2 = int(input("Cuantos datos tiene el conjunto2: "))
for i in range (conjunto2):
    B=int(input("Ingrese numero: "))
    listaNumeros2.add(B)

print("El conjunto 2 es: ", listaNumeros2)

diferencia1menos2 =  listaNumeros1  -  listaNumeros2
diferencia2menos1 =  listaNumeros2  -  listaNumeros1

print("La diferencia del primer y segundo conjunto es: ",diferencia1menos2)
print("La diferencia del segundo y primer conjunto es: ",diferencia2menos1)