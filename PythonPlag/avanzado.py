#funcion avanzada
'''def encriptar(cadena):
  r=''
  n=len(cadena)
  for i in range(0,n-1,2):
    a=cadena[i]
    b=cadena[i+1]
    r=r+b+a
  if(n%2!=0):
    r=r+cadena[n-1]
  return r
print(encriptar("programas"))'''
def multilista(lista,factor,factor2=2):
  for i in range (0, len(lista)):
    lista.append(lista[i]*factor-factor2)
    #comentario
    return lista
print(multilista([10,20,30],1))



