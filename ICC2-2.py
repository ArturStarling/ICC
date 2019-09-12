arquivo = open("arquivo2.txt", 'r')
x,e = arquivo.read().split()
w = int(x[0])
y = int(e[0])

def seno2(w,y):
  lista = [w]
  t = w
  s = 0
  i = 0
  while (math.fabs(t) > y):
    i = i + 1
    t = -((w*w)/((2*i)*(2*i+1)))*t
    lista.append(t)
  for i in reversed(lista):
    s = s + i
  return s
  
import numpy
print ("seno de x (com numpy)= ",numpy.sin(w))