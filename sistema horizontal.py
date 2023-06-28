#abrir como carpeta
#definicion de las constantes 
#modificar este codigo y no el MAIN
#python 3.11.4

import math

P1 = 0; P2 = 0; M1 = 0; M2 = 0; F = 0 ; g = 9.8; 
A = 0; T = 0; aceleracionPI = 0; tensionPI = 0; aceleracionPI2 = 0
angulo_inclinacion_1 = 0;angulo_inclinacion_2 = 0
complemento = ''

#---------------------------------------------------------------------------
#---------------------------ingtreso de datos-------------------------------
#---------------------------------------------------------------------------
def peso_1():
    global P1
    P1 = float(input("valor del peso 1: "))
    return

def peso_2():
    global P2
    P2 = float(input("valor del peso 2: "))
    return

def masa_1():
    global M1
    if P1 != 0:
        M1 = P1 / g
    else:
        M1 = float(input("valor de la masa 1: "))
    return

def masa_2():
    global M2
    if P2 != 0:
        M2 = P1 / g
    else:
        M2 = float(input("valor de la masa 2: "))

def fuerza_aplicada():
    global F
    F = float(input("valor de la fueraz aplicada: "))

def anglulo_inclinacion_A():
    global angulo_inclinacion_1
    angulo_inclinacion_1 = float(input("Ingrese el ángulo de inclinación 1 (en grados): "))
    return

def angulo_inclinacion_B():
    global angulo_inclinacion_2
    angulo_inclinacion_2 = float(input("Ingrese el ángulo de inclinación 2 (en grados): "))
#---------------------------------------------------------------------------
# Sistema de dos masas superficie horizontal con una fuerza externa aplicada
#---------------------------------------------------------------------------
 # Calcula la aceleración 
def aceleracion():
    global A
    A = (F/(M1+M2))
    return
# Calcula la tensión en la cuerda que conecta las masas
def tension():
    global T
    T = M1 * A
    return 
#--------------------------------------------------
# Sistema de dos masas superficie inclinada
# CASO 1 (UN SOLO ANGULO)
#--------------------------------------------------
# Cálculo de la aceleración en la superficie inclinada
def aceleracion_1Angulo():
    global aceleracionPI
    aceleracionPI = ((M2 * g) - ((M1 * g * math.sin(math.radians(angulo_inclinacion_1))) / (M1 + M2 )))
    return

# Cálculo de la tensión en la cuerda o superficie inclinada
def tension_1Angulo():
    global tensionPI
    tensionPI = ((M2 * g) - (M1 * aceleracionPI))
    return 

#--------------------------------------------------
# Sistema de dos masas superficie inclinada
#CASO 2 (DOS ANGULOS)
#--------------------------------------------------
# Cálculo de la aceleración en la superficie inclinada con dos angulos
def aceleracion_2Angulos():
    global aceleracionPI2
    aceleracionPI2 = (M2 * g * math.sin(math.radians(angulo_inclinacion_2))) - ((M1 * g * math.sin(math.radians(angulo_inclinacion_1)) ) / (M1 + M2))
    return 

# Cálculo de la tensión en la superficie inclinada con dos angulos
def tension_2Angulos():
    global tensionPI2
    tensionPI2 = ((M1 * aceleracionPI2) + (M1* g * math.sin(math.radians(angulo_inclinacion_1))))
    return 
#----------------------------------------------------------------------------

#---------complemento----------------------
def complemento_0():
    global complemento
    complemento = input("otra cosita?: ")
    return

#progrma principal
while True:
    encontrar = input("que deseas conocer?: ")
    #-----------------------sitema horizontal--------------------------------
    if encontrar == 'aceleracion':
        peso_1(); peso_2(); masa_1(); masa_2(); fuerza_aplicada() #datos
        aceleracion()
        print("aceleracion = ",A)
    elif encontrar == 'tension': 
        peso_1(); peso_2(); masa_1(); masa_2(); fuerza_aplicada() #datos
        aceleracion(); tension()
        print("tension = ",T)
    #-------------------------plano inclinado con 1 angulo----------------------------
    elif encontrar == 'tension caso 1':
        peso_1(); peso_2(); masa_1(); masa_2(); anglulo_inclinacion_A() #datos
        aceleracion_1Angulo()
        tension_1Angulo()
        print("tension de la superficie inclinada = ",tensionPI)
    elif encontrar == 'aceleracion caso 1':
        peso_1(); peso_2(); masa_1(); masa_2(); anglulo_inclinacion_A() #datos
        aceleracion_1Angulo()
        print("aceleracion de la superficie inclinada = ",aceleracionPI)
    #-----------------plano inclinado con 2 angulos-----------------------------------
    elif encontrar == 'tension caso 2':
        peso_1(); peso_2(); masa_1(); masa_2(); anglulo_inclinacion_A(); angulo_inclinacion_B() #datos
        aceleracion_2Angulos()
        tension_2Angulos()
        print("tension de la superficie inclinada dos angulos = ",tensionPI2)
    elif encontrar == 'aceleracion caso 2':
        peso_1(); peso_2(); masa_1(); masa_2(); anglulo_inclinacion_A(); angulo_inclinacion_B() #datos
        aceleracion_2Angulos()
        print("aceleracion de la superficie inclinada 2 angulos = ",aceleracionPI2)
        #-------------------------------------------------------------------------------
        #complemento_0()
        if complemento == 'si':
            if encontrar == 'aceleracion':
                print("t = ",tension())
            elif encontrar == 'tension':
                print("a = ",aceleracion())
        elif complemento == 'no':
            break