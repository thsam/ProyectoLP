#funcion avanzada

def multilista(lista,factor,factor2=2):
  for i in range (0, len(lista)):
    lista.append(lista[i]*factor-factor2)
    #comentario
    return lista
print(multilista([10,20,30],1))



