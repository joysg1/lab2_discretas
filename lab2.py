import itertools as it
import pprint
from itertools import combinations
from itertools import permutations
from math import factorial
import math


pp = pprint.PrettyPrinter(indent=4)

## Problema 1
def fibloop(n):
    lista =[0,1] ## Creacion de la lista
    while len(lista)<n: ##ciclo while mientras la longtud de lista sea menor a n
      lista.append(lista[-1]+ lista[-2]) ## se anexa a la lista los dos elementos anteriores
      print(lista[:10]) ## se imprime la lista
    return lista[:n]  ## retorno de la lista

assert fibloop(1) == [0]
assert fibloop(2) == [0,1]
assert fibloop(3) == [0,1,1]
assert fibloop(5) == [0,1,1,2,3]
assert fibloop(7) == [0,1,1,2,3,5,8]


## Problema 2
def calc_fibrec(n):
    if n <=1: # Si n es menor o igual a 1 retornar 1
     return 1
    
    else:
      return((calc_fibrec(n-1) + calc_fibrec(n-2))) 
  # En caso contrario retornar la suma de los dos numeros anteriores a n

## Problema 3
def fibrec(n):
    lista_f = [] ## Creacion de la lista
    for i in range(10): ## Ciclo for hasta 10 
        lista_f.append(calc_fibrec(i)) 
        ## Se anexan a la lista los resultados de calc_fibrec
      
    return lista_f ## Se retorna la lista

assert fibrec(1) == [0]
assert fibrec(2) == [0,1]
assert fibrec(3) == [0,1,1]
assert fibrec(5) == [0,1,1,2,3]
assert fibrec(7) == [0,1,1,2,3,5,8]
print()

## Problema 4
def euler_totient(n):
    r = n 
    p = 2 
    
    while p * p <=n:   #Ciclos repetitivos para iterar entre numeros primos p
        if n%p ==0:
            while n % p == 0:
                n //= p
            r *= 1 - (1/p)
        p = p + 1
        
    if n > 1:
        r *= 1 - (1/n)
                  
    return r   #Retorno de los numeros coprimos a n 

## Problema 5
def sec_euler_totient(n):
    listc = []       # Creacion de la lista
    for i in range (1, n+1): # Recorrido de las posiciones
        if euler_totient(i) == i-1: # Comparacion entre posiciones
            listc.append(i) # Se agrega el coprimo a la lista
            
    return listc     # Se retorna la lista 

assert sec_euler_totient(10) == [1,1,2,2,4,2,6,4,6,4]
print()


## Problema 7

def num_perm(n,r): 
    
    tam = len(n)
    P = factorial(tam) / factorial(tam -r)
    
    return int(P)    


lista = [1,2,3,4,5,6,7]

## print("Numero de permutaciones tomando 3 elementos ")
## print(num_perm(lista,3))

## print("Numero de permutaciones tomando 4 elementos ")
## print(num_perm(lista,4))

## print("Numero de permutaciones tomando 5 elementos ")
## print(num_perm(lista,5))

## print("Numero de permutaciones tomando todos los elementos ")
## print(num_perm(lista,len(lista)))


## Problema 8
def lanzamiento_dado(num_lanz):
    
    n = 8
    S = pow(8,num_lanz)
    
    return S



# print(lanzamiento_dado(4))

assert lanzamiento_dado(4) == 4096


## Problema 9
def ordenar_libros(num_libros):
    tot_lib= 8
    
    P = factorial(tot_lib) / factorial(tot_lib - num_libros)
    
    return P

assert ordenar_libros(4) == 1680
print()


## Problema 10


def calc_combinations(n,r):
    
    tam = len (n)
    C = factorial (tam) / ( factorial(r) * factorial (tam - r))
    
    return int(C)

lst2 = [1,2,3,4,5,6,7]

## print(calc_combinations(lst2,2))

## print(calc_combinations(lst2,3))

## print(calc_combinations(lst2,4))

## print(calc_combinations(lst2,5))


## Problema 11
def imprimir_manos(num_cartas):
    palos = ['♠', '♥', '♦', '♣']
    rango = [str(n) for n in range(2,11)] + ['J','Q','K','A']
    
    cartas = list(it.product(rango, palos))
    
    manos = list(it.combinations(cartas, num_cartas)) # Combinaciones posibles
    
    return len(manos) #longitud de la variable manos
    
    pass

assert imprimir_manos(6) == 20358520


## Problema 12
def lanzamiento_moneda(num_lanz):
    caras = 2 * num_lanz # Total de caras en num_lanz
    k = num_lanz
    C = math.factorial(caras) / (math.factorial(k) * math.factorial(caras-k))
    return int(C)

assert lanzamiento_moneda(5) == 252
