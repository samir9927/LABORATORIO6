def conjuntos(x):
    listaNumeros=set()
    for i in range (x):
        num=int(input("Ingrese numero: "))
        listaNumeros.add(num)
    
    print("El conjunto es: ", listaNumeros)
    print("------------------------------------------")

    return listaNumeros

conj1=int(input("Cuantos datos tiene el primer conjunto: "))
A=conjuntos(conj1)

conj2=int(input("Cuantos datos tiene el segundo conjunto: "))
B=conjuntos(conj2)

conj3=int(input("Cuantos datos tiene el tercer conjunto: "))
C=conjuntos(conj3)

difSimetrica = (A^B)^C
print("La diferencia simetrica de los conjuntos es: ", difSimetrica)