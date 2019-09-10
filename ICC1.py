n = int(input("Digite o valor de n: "))
x = 1
i = 2

while i <= n:
  x = x*i
  i += 1
  
print("O valor de {}! é = {}".format(n, x))