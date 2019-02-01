def add(num1,num2):
  """
  Agregar dos numeros Reales
  Por ejemplo:
  >>> add(1,3)
  4
  >>> add(3,-4)
  -1
  """
  return num2 + num1

def task_051():
  """
  Calcula los minutos en una semana
  Por ejemplo:
  >>> task_051()
  10080
  """
  return 7*24*60

def task_052(num):
  """
  Calcula el residuo de 2304811/ 47
  sin usar operador %
  ejemplo:
  >>> task_052(2304811)
  25
  """
  return num-((num//47)*47)

  def task_053(num1,num2):
    """
    Ingresar una expresion booleana y probar si la suma de 673 y 909 es divisible entre 3
    ejemplo:
    >>> task_053(673,909)
    False
    """
    return (num1+num2)%3==0

def task_054(x,y):
    """
    Asignar el valor de -9 a X y 1/2 a y, predecir el valor de la siguiente expresion
    2**3(y+1/2) if x+10<0 else 2**(y-1/2)
    ejemplo:
    >>> task_054(-9,1/2)
    1
    """
    return int(2**3(y+1/2) if x+10<0 else 2**(y-1/2))

def task_055():
    """
    Escribe una comprension entre {1,2,3,4,5} y eleva los valores al cuadrado

    ejemplo:
    >>> task_055()
    {16, 1, 9, 25, 4}
    """
    return {x**2 for x in {1,2,3,4,5}}

def task_056():
    """
    Escribe una comprension entre {0,1,2,3,4} y eleva el valor de dos a cada potencia o elemento
    del conjunto

    ejemplo:
    >>> task_056()
    {8, 1, 2, 16, 4}
    """
    return {2**x for x in {0,1,2,3,4}}

def task_057():
    """
    producir un conjunto de 9 elementos
    ejemplo:
    >>> task_057()
    {5, 6, 7, 10, 12, 14, 15, 18, 21}
    """
    return {x*y for x in {1,2,3} for y in {5,6,7}}


def task_058():
    """
    Reemplazar los dos conjuntos anteriores para producir un
    resultado de 5 elementos
    ejemplo:
    >>> task_058()
    {1, 2, 3, 4, 6}
    """
    return {x*y for x in {1,2,3} for y in {1,2,2}}


def task_059():
    """
    producir una interseccion de dos conjuntos sin usar el
    operador &
    ejemplo:
    >>> task_059()
    {3, 4}
    """
    return {x for x in {1,2,3,4} for y in {3,4,5,6} if x == y}


def task_0510():
    """
    Escribe una expresion cuyo valor es el promedio de los
    elementos de una lista [20, 10, 15, 75]
    ejemplo:
    >>> task_0510()
    30
    """
    return sum([20, 10, 15, 75])/len([20, 10, 15, 75])

def task_0511():
    """
    Escribe una lista doble ['A','B','C'] y [1,2,3]
    ejemplo:
    >>> task_0511()
    [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
    """
    return [[x,y] for x in ['A','B','C'] for y in [1,2,3] ]

def task_0512():
    """
    Escribe una lista que evalue la suma de los numeros de la lista

    ejemplo:

    >>> task_0512()
    16.1
    """
    return sum([sum([.25, .75, .1] + [-1,0] + [4,4,4,4])])

def hola():
  a = 23
  return a

def task_0514():
    """
    Produce una triple comprension cuyo resultado sean tuplas que sumados sus elementosden 0
    ejemplo:
    >>> task_0514()
    {(0, 2, -2), (0, -2, 2), (1, 1, -2), (2, 2, -4), (2, 0, -2), (2, -4, 2), (-2, 0, 2), (-2, 1, 1), (2, -2, 0), (-4, 2, 2), (-2, 2, 0), (0, 0, 0), (1, -2, 1)}
    """
    a = 23
    return a
    #return {(x,y,z) for x in {-4,-2,1,2,5,0} for y in {-4,-2,1,2,5,0} for z in {-4,-2,1,2,5,0} if x+y+z==0}

def task_0515():
    """
    Produce una triple comprension cuyo resultado sean tuplas que sumados sus elementosden 0
    ejemplo:
    >>> task_0515()
    {(0, 2, -2), (0, -2, 2), (1, 1, -2), (2, 2, -4), (2, -4, 2), (2, 0, -2), (-2, 0, 2), (-2, 1, 1), (2, -2, 0), (-4, 2, 2), (-2, 2, 0), (1, -2, 1)}
    """
    s = {(x,y,z) for x in {-4,-2,1,2,5,0} for y in {-4,-2,1,2,5,0} for z in {-4,-2,1,2,5,0} if x+y+z==0 }
    return { x for x in s  if x!=(0,0,0) }


def task_0516():
    """
    Modifica la expresion de la task_05_14 para producir una tripla = {(0, 0, 0)}
    ejemplo:
    >>> task_0516()
    {(0, 0, 0)}
    """
    s = task_0514()
    return { x for x in s  if x==(0,0,0) }

def task_0517():
    """
    Encuentra un ejemplo de una lista cuya longitudes sean diferntes
    ejemplo:
    >>> task_0517()
    4
    """
    L = [1,2,2,3,4]
    return len(list(set(L)))

def task_0518():
    """
    escribe comprension sobre un rango que el valor de la comprension sean los numeros del 1 - 99
    ejemplo:
    >>> task_0518()
    {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99}
    """
    return {x for x in range(100) if x % 2 != 0}

def task_0519():
    """
    Asigna a la lista L las 5 primeras letras del alfabeto y utiliza una expresion para relacionarlas
    con los numeros del 0 al 4
    ejemplo:
    >>> task_0519()
    [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
    """
    letters = ['A', 'B', 'C', 'D', 'E']

    return list(zip(range(5), letters))

def task_0520():
    """
    basado en 2 listas, escribe una tercera lista cuyos elementos sean las sumas de los elementos de las 2 listas
    ejemplo:
    >>> task_0520()
    {40, 11, 60}
    """
    L1= [10, 25, 40]
    L2= [1, 15, 20]
    return {x+y for (x,y) in zip(L1,L2)}

def task_0521(k):
  """
  Encuentra un valor en un diccionario a partir de su clave, dentro de una lista
  >>> task_0521('James')
  Sean
  Royer
  Pearse
  """
  dlist = [{'James':'Sean', 'directos':'Terence'}, {'James':'Royer', 'Director': 'Lewis'}, {'James':'Pearse', 'Director':'Royer'}]

  for i in dlist:
    if(k in i.keys()):
      print( i[k] )



def task_0522(k):
  """
  Realiza una comprension que evalue de una lista cuyos elementos son diccionarios la llave
  y compare si esta presente en los dos diccionarios
  >>> task_0522('Bilbo')
  True
  >>> task_0522('Frodo')
  False
  """
  dlist=[{'Bilbo':'Ian', 'Frodo':'Elijah'}, {'Bilbo':'Martin', 'Thorin': 'Richard'}];
  cont = 0
  for i in dlist:
    if(k in i.keys()):
      cont = cont+1

  if cont == len(dlist):
    return True
  else:
    return False

def task_0523():
    """
    Escribe una expresion cuyo resultado sea un diccionario donde las llaves son enteros del 0 al 99 y los valores corresponden a los cuadrados de las claves
    ejemplo:
    >>> task_0523()
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 27: 729, 28: 784, 29: 841, 30: 900, 31: 961, 32: 1024, 33: 1089, 34: 1156, 35: 1225, 36: 1296, 37: 1369, 38: 1444, 39: 1521, 40: 1600, 41: 1681, 42: 1764, 43: 1849, 44: 1936, 45: 2025, 46: 2116, 47: 2209, 48: 2304, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 54: 2916, 55: 3025, 56: 3136, 57: 3249, 58: 3364, 59: 3481, 60: 3600, 61: 3721, 62: 3844, 63: 3969, 64: 4096, 65: 4225, 66: 4356, 67: 4489, 68: 4624, 69: 4761, 70: 4900, 71: 5041, 72: 5184, 73: 5329, 74: 5476, 75: 5625, 76: 5776, 77: 5929, 78: 6084, 79: 6241, 80: 6400, 81: 6561, 82: 6724, 83: 6889, 84: 7056, 85: 7225, 86: 7396, 87: 7569, 88: 7744, 89: 7921, 90: 8100, 91: 8281, 92: 8464, 93: 8649, 94: 8836, 95: 9025, 96: 9216, 97: 9409, 98: 9604, 99: 9801}
    """
    return {k:k*k for k in range(100)}

def task_0524():
    """
    Escribe una comprension en un diccionario que represente la identidad en el diccionario D
    {'red','white','blue'}
    ejemplo:
    >>> task_0524()
    {0: 'white', 1: 'white', 2: 'white'}
    """
    D = {'red','white','blue'}
    return {k:v for k in range(3) for v in D}
#Pelucas, este no jala

