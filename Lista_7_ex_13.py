Times = {'SP': 'Sao Paulo' , 'PL': 'Palmeiras' , 'ST': 'Santos', 'VC': 'Vasco'}
for x , y in Times.items():
    print ('{} = {}'.format(x,y))
print('\n')     
   
inf = float('inf')
A = [['#', 'PG', 'GM', 'GS', 'S', 'V', 'GA'],
     ['SP', '2', '4', '4', '0', '1', '1'],
     ['PL', '0', '1', '2', '-1', '0', '0.5'],
     ['ST', '0', '1', '3', '-2', '0', '3.33'],
     ['VC', '4', '6', '3', '3', '2', '2']]

print('\n'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in A]))
t = []
g = []
u = []
for i in A:
  t.append(i[0])
  g.append(i[2])
  u.append(i[4])

print('\n Primeiro jogo =','({},{},{},{})'.format(t[1],t[2],'2','1'))
print('Segundo jogo =','({},{},{},{})'.format(t[3],t[4],'1','3'))
print('Terceiro jogo =','({},{},{},{})'.format(t[4],t[1],'3','2'))
print('Quarto jogo =','({},{},{},{})'.format(t[3],t[2],'0','0'))

print('\n Classificação por PG:', '\n Primeiro: {}'.format(t[1]),'\n Segundo: {}'.format(t[4]),'\n Terceiro: {}'.format(t[2]), '\n Último: {}'.format(t[3]))

print('\n Classificação por S:', '\n Primeiro: {}'.format(t[4]),'\n Segundo: {}'.format(t[1]),'\n Terceiro: {}'.format(t[2]), '\n Último: {}'.format(t[3]))

print('\n Pelas regras do campeonato paulista de 1975, a classificação final é:', '\n Primeiro: {}'.format(t[4]),'\n Segundo: {}'.format(t[1]),'\n Terceiro: {}'.format(t[3]), '\n Último: {}'.format(t[2]))

c,v,b,n,m = (0,0,0,0,0)
apostas = {'Joao' : [3,2,1,3,1,4,1,1], 'Pedro' : [1,2,4,2,2,3,0,1] , 'Roberto' : [3,2,1,4,3,2,2,2], 'Tauane' : [2,1,3,1,2,3,0,4], 'Borracha' : [4,5,5,2,2,4,1,3]}
for z,x in apostas.items():
  print('\n {} apostou nos seguintes placares: ({},{});({},{});({},{});({},{})'.format(z,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
  
  if z == 'Joao':
    if x[0] > x[1]:
      c += 3 
    if x[0] == 2 and x[1] == 1:
      c += 2
    if x[2] < x[3]:
      c += 3 
    if x[2] == 1 and x[3] == 3:
      c += 2
    if x[4] > x[5]:
      c += 3 
    if x[4] == 3 and x[5] == 2:
      c += 2  
    if x[6] == x[7]:
      c += 3 
    if x[6] == 0 and x[7] == 0:
      c += 2     

  elif z == 'Pedro':    
    if x[0] > x[1]:
      v += 3 
    if x[0] == 2 and x[1] == 1:
      v += 2
    if x[2] < x[3]:
      v += 3 
    if x[2] == 1 and x[3] == 3:
      v += 2
    if x[4] > x[5]:
      v += 3 
    if x[4] == 3 and x[5] == 2:
      v += 2  
    if x[6] == x[7]:
      v += 3 
    if x[6] == 0 and x[7] == 0:
      v += 2      
     
  elif z == 'Roberto':    
    if x[0] > x[1]:
      b += 3 
    if x[0] == 2 and x[1] == 1:
      b += 2
    if x[2] < x[3]:
      b += 3 
    if x[2] == 1 and x[3] == 3:
      b += 2
    if x[4] > x[5]:
      b += 3 
    if x[4] == 3 and x[5] == 2:
      b += 2  
    if x[6] == x[7]:
      b += 3 
    if x[6] == 0 and x[7] == 0:
      b += 2     

  elif z == 'Tauane':    
    if x[0] > x[1]:
      n += 3 
    if x[0] == 2 and x[1] == 1:
      n += 2
    if x[2] < x[3]:
      n += 3 
    if x[2] == 1 and x[3] == 3:
      n += 2
    if x[4] > x[5]:
      n += 3 
    if x[4] == 3 and x[5] == 2:
      n += 2  
    if x[6] == x[7]:
      n += 3 
    if x[6] == 0 and x[7] == 0:
      n += 2       

  elif z == 'Borracha':
    if x[0] > x[1]:
      m += 3 
    if x[0] == 2 and x[1] == 1:
      m += 2
    if x[2] < x[3]:
      m += 3 
    if x[2] == 1 and x[3] == 3:
      m += 2
    if x[4] > x[5]:
      m += 3 
    if x[4] == 3 and x[5] == 2:
      m += 2  
    if x[6] == x[7]:
      m += 3 
    if x[6] == 0 and x[7] == 0:
      m += 2

somatorio = [c,v,b,n,m]

print('\n O vencedor foi: Roberto, com {} pontos'.format((max(somatorio))))
