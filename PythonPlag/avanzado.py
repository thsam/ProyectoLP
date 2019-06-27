#funcion avanzada
def encriptar(cadena):
  r=''
  n=len(cadena)
  for i in range(0,n-1,2):
    a=cadena[i]
    b=cadena[i+1]
    r=r+b+a
  if(n%2!=0):
    r=r+cadena[n-1]
  return r
print(encriptar("programas"))