conjunto1 =  {1 , 2 , 2 , 3 , 4 , 5 , 4 , 8 , 45 , 54 , 87 , 99 , 5 }
conjunto2 = { 1 , 2 , 4 , 6 , 2 , 4 , 5 , 2 , 45 , 22 , 55 , 77 , 88 , 99 }
A = conjunto1
B = conjunto2
union = A  |  B
diferenciaAmenosB =  A  -  B
diferenciaBmenosA =  B  -  A
interseccion = A  &  B
print ( "Elementos que aparecen en las dos listas (Union)." , union )
print ( "Elementos que aparecen en la primera lista pero no en la segunda (Diferencia)." , diferenciaAmenosB )
print ( "Elementos que aparecen en la segunda lista pero no en la primera (Diferencia)." , diferenciaBmenosA )
print ( "Elementos que aparecen en ambas listas (interseccion)." , interseccion )