x = float(input("Digite um valor para o angulo (em radianos): "))
e = float(input("Digite um valor para o epsilon: "))

def seno(x,e):
  t = x
  s = t
  i = 0
  while (math.fabs(t) > e):
    i = i + 1
    t = -(x*x)/((2.*i)*(2.*i+1))*t
    s += t
  return s
  
import numpy
print ("seno de x (com numpy)= ",numpy.sin(x))