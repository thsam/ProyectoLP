def numerospares(n):
    #creamos lista
    lista=[]
    for i in range(n):
        valor=int(input("ingrese numero: "))
        if(valor%2==0):
            lista.append(valor)
            lista.hola(4)
    return lista

print(numerospares(7))