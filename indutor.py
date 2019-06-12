import sys
import numpy as np
import math


def erro(lista_valores, atributo, arq2, arq3):
  atributo_teste = 0
  for i in  range(len(lista_valores[0])):    
    if lista_valores[0][i] == atributo:
      atributo_teste = i

  f = open(arq2, 'w')
  f2 = open(arq3, 'w')
  X_raiz = 0 
  y0_raiz = 0  
  y1_raiz = 0
  
  y0_no6 = 0
  y1_no6 = 0
  X_no6 = 0

  y0_no7 = 0
  y1_no7 = 0
  X_no7 = 0

  for i in  lista_valores:
    if i[atributo_teste] == '0':
      f.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no6 = y0_no6 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no6 = y1_no6 + 1
      X_no6 = X_no6 + 1

    if i[atributo_teste] == '1':
      f2.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no7 = y0_no7 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no7 = y1_no7 + 1
      X_no7 = X_no7 + 1

  f.close()
  f2.close()

  for i in  lista_valores:
    if i[len(lista_valores[0])-1] == '0':
      y0_raiz = y0_raiz + 1
    if i[len(lista_valores[0])-1] == '1':
      y1_raiz = y1_raiz + 1
    X_raiz = X_raiz + 1
  
  X_raiz = X_raiz - 1
  erroClass_raiz = 1 -  max([y0_raiz/X_raiz , y1_raiz/X_raiz])
  erroClass_no6 = 1 -  max([y0_no6/X_no6 , y1_no6/X_no6])
  erroClass_no7 = 1 -  max([y0_no7/X_raiz , y1_no7/X_no7])
  ganho = erroClass_raiz - X_no6/X_raiz * erroClass_no6 + X_no7/X_raiz * erroClass_no7 
  print('1 - Erro de Classificação')
  print('Impureza em no3.txt: {0}'.format(erroClass_raiz))
  print('Impureza em no6.txt: {0}'.format(erroClass_no6))
  print('Impureza em no7.txt: {0}'.format(erroClass_no7))
  print('Ganho: {0}'.format(ganho))

def gini(lista_valores, atributo, arq2, arq3):
  atributo_teste = 0
  for i in  range(len(lista_valores[0])):    
    if lista_valores[0][i] == atributo:
      atributo_teste = i

  f = open(arq2, 'w')
  f2 = open(arq3, 'w')
  X_raiz = 0
  y0_raiz = 0
  y1_raiz = 0

  y0_no6 = 0
  y1_no6 = 0
  X_no6 = 0

  y0_no7 = 0
  y1_no7 = 0
  X_no7 = 0

  for i in  lista_valores:
    if i[atributo_teste] == '0':
      f.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no6 = y0_no6 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no6 = y1_no6 + 1
      X_no6 = X_no6 + 1

    if i[atributo_teste] == '1':
      f2.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no7 = y0_no7 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no7 = y1_no7 + 1
      X_no7 = X_no7 + 1

  f.close()
  f2.close()

  for i in  lista_valores:
    if i[len(lista_valores[0])-1] == '0':
      y0_raiz = y0_raiz + 1
    if i[len(lista_valores[0])-1] == '1':
      y1_raiz = y1_raiz + 1
    X_raiz = X_raiz + 1
  
  X_raiz = X_raiz - 1
  gini_raiz = 1 - (y0_raiz/X_raiz)**2 - (y1_raiz/X_raiz)**2
  gini_no6 = 1 - (y0_no6/X_no6)**2 - (y1_no6/X_no6)**2
  gini_no7 = 1 - (y0_no7/X_no7)**2 - (y1_no7/X_no7)**2
  ganho = gini_raiz - X_no6/X_raiz * gini_no6 + X_no7/X_raiz * gini_no7 
  print('2 - Gini')
  print('Impureza em no3.txt: {0}'.format(gini_raiz))
  print('Impureza em no6.txt: {0}'.format(gini_no6))
  print('Impureza em no7.txt: {0}'.format(gini_no7))
  print('Ganho: {0}'.format(ganho))

def entropia(lista_valores, atributo, arq2, arq3):
  atributo_teste = 0
  for i in range(len(lista_valores[0])):    
    if lista_valores[0][i] == atributo:
      atributo_teste = i

  f = open(arq2, 'w')
  f2 = open(arq3, 'w')
  X_raiz = 0
  y0_raiz = 0
  y1_raiz = 0

  y0_no6 = 0
  y1_no6 = 0
  X_no6 = 0

  y0_no7 = 0
  y1_no7 = 0
  X_no7 = 0

  for i in  lista_valores:
    if i[atributo_teste] == '0':
      f.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no6 = y0_no6 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no6 = y1_no6 + 1
      X_no6 = X_no6 + 1

    if i[atributo_teste] == '1':
      f2.write(' '.join(i)+'\n')
      if i[len(lista_valores[0])-1] == '0':
        y0_no7 = y0_no7 + 1
      if i[len(lista_valores[0])-1] == '1':
        y1_no7 = y1_no7 + 1
      X_no7 = X_no7 + 1

  f.close()
  f2.close()

  for i in  lista_valores:
    if i[len(lista_valores[0])-1] == '0':
      y0_raiz = y0_raiz + 1
    if i[len(lista_valores[0])-1] == '1':
      y1_raiz = y1_raiz + 1
    X_raiz = X_raiz + 1
  
  X_raiz = X_raiz - 1
  entropia_raiz = -(y0_raiz/X_raiz * math.log((y0_raiz/X_raiz),2) + y1_raiz/X_raiz * math.log((y1_raiz/X_raiz),2)) 

  if (y0_no6/X_no6) == 0:
    if (y1_no6/X_no6) == 0:
      entropia_no6 = 0.0
    else:
      entropia_no6 = -(y1_no6/X_no6 * math.log((y1_no6/X_no6),2))
  else:
    if (y1_no6/X_no6) == 0:
      entropia_no6 = -(y0_no6/X_no6 * math.log((y0_no6/X_no6),2))
    else:
      entropia_no6 = -(y0_no6/X_no6 * math.log((y0_no6/X_no6),2) + y1_no6/X_no6 * math.log((y1_no6/X_no6),2))

  if (y0_no7/X_no7) == 0: 
    if (y1_no7/X_no7) == 0:  
      entropia_no7 = 0.0
    else:
      entropia_no7 = -(y1_no7/X_no7 * math.log((y1_no7/X_no7),2))
  else:
    if (y1_no7/X_no7) == 0:
      entropia_no7 = -(y0_no7/X_no7 * math.log((y0_no7/X_no7),2))
    else:
      entropia_no7 = -(y0_no7/X_no7 * math.log((y0_no7/X_no7),2) + y1_no7/X_no7 * math.log((y1_no7/X_no7),2))
  
  ganho = entropia_raiz - X_no6/X_raiz * entropia_no6 + X_no7/X_raiz * entropia_no7 
  print('3 - Entropia')
  print('Impureza em no3.txt: {0}'.format(entropia_raiz))
  print('Impureza em no6.txt: {0}'.format(entropia_no6))
  print('Impureza em no7.txt: {0}'.format(entropia_no7))
  print('Ganho: {0}'.format(ganho))
  
def impureza(txt, atributo, tipo, arq2, arq3):
  f = open(txt, 'r')  
  linhas = f.readlines()
  linha_array = []
  for i in linhas:
    linha_array.append(i.replace('\n','').split())    
    
  lista_valores = np.array(linha_array)
  
  if tipo == '1':
    erro(lista_valores, atributo, arq2, arq3)

  if tipo == '2':
    gini(lista_valores, atributo, arq2, arq3)

  if tipo == '3':
    entropia(lista_valores, atributo, arq2, arq3)
  

def main(argv):
  arq1 = sys.argv[1]
  arq2 = sys.argv[2]
  arq3 = sys.argv[3]
  atrib = sys.argv[4]
  tipo = sys.argv[5]
  impureza(arq1, atrib, tipo, arq2, arq3)

if __name__ == "__main__":
  main(sys.argv)