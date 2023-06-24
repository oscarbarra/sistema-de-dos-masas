#abrir como carpeta
#definicion de las constantes 
#modificar este codigo y no el MAIN
P1 = 0; P2 = 0; M1 = 0; M2 = 0; T = 0; A = 0 ; F = 0 ; g = -9.8; aceleracionPI= 0
tensionPI= 0; aceleracionPI2 =0; angulo_inclinacion_1= 0;angulo_inclinacion_2= 0; complemento = ''; repeticion = ''

#---------------------------------------------------------------------------
# Sistema de dos masas superficie horizontal con una fuerza externa aplicada
#---------------------------------------------------------------------------
 # Calcula la aceleración 
def aceleracion(F,M1,M2):
    global A
    A = (F/(M1+M2))
    return A

# Calcula la tensión en la cuerda que conecta las masas
def tension(A,M1,M2):
    global T
    T = M1 * A
    return T
#--------------------------------------------------
# Sistema de dos masas superficie inclinada
#CASO 1 (UN SOLO ANGULO)
#--------------------------------------------------
# Cálculo de la aceleración en la superficie inclinada
import math
def aceleracion_1Angulo(g,M1,M2,angulo_inclinacion):
    global aceleracionPI
    aceleracionPI = (abs((M2 * g) - (M1 * g * math.sin(math.radians(angulo_inclinacion)))) / (M1 + M2 ))
    return aceleracionPI

# Cálculo de la tensión en la cuerda o superficie inclinada
def tension_1Angulo(g,M1,aceleracionPI):
    global tensionPI
    tensionPI = abs(M2 * g - M1 * aceleracionPI)
    return tensionPI

#--------------------------------------------------
# Sistema de dos masas superficie inclinada
#CASO 2 (DOS ANGULOS)
#--------------------------------------------------
# Cálculo de la aceleración en la superficie inclinada con dos angulos
def aceleracion_2Angulos(g,M1, M2, angulo_inclinacion_1, angulo_inclinacion_2):
    global aceleracionPI2
    aceleracionPI2 = (abs(M2 * g * math.sin(math.radians(angulo_inclinacion_2)) - M1 * g * math.sin(math.radians(angulo_inclinacion_1)) ) / (M1 + M2))
    return aceleracionPI2

# Cálculo de la tensión en la superficie inclinada con dos angulos
def tension_2Angulos(M1, aceleracionPI2):
    global tensionPI2
    tensionPI2 = (abs(M1 * aceleracionPI2 + M1* g * math.sin(math.radians(angulo_inclinacion_1))))
    return tensionPI2
#--------------------------------------------------
#
#--------------------------------------------------
#complemento
def complemento_0():
    global complemento
    complemento = input("otra cosita?: ")
    return

#repeticion
def repeticion_0():
    global repeticion
    repeticion = input("quieres otros valores?: ")
    return

#historial

def relleno():
    with open('historial.txt','r+') as h:
        h.readlines()
        h.write(("M1 = ")+str(M1)+("\n")+("M2 = ")+str(M2)+("\n"))
        h.write(("fuerza aplicada = ")+(str(F))+("\n"))
        h.write(("A = ")+str(A)+'\n'+("T = ")+str(T)+("\n"))
        h.write("------------------------------------------------"+("\n"))


#INGRESO DE LOS DATOS
def datos():
    global P1,P2,M1,M2,F,g,angulo_inclinacion_1,angulo_inclinacion_2
    angulo_inclinacion_1 = float(input("Ingrese el ángulo de inclinación 1 (en grados): "))
    angulo_inclinacion_2 = float(input("Ingrese el ángulo de inclinación 2 (en grados): "))
    P1 = float(input("peso objeto 1: "))
    P2 = float(input("peso objeto 2: "))
    F = float(input("fuerza aplicada: "))
    if P1 != 0:
        M1 = P1/9.8
    else:
        M1 = float(input("masa objeto 1: "))
    if P2 != 0:
        M2 = P2/9.8
    else:
        M2 = float(input("masa objeto 2: "))
    return

#progrma principal
datos()
h = open("historial.txt","w")
h.close
while True:
    encontrar = input("que deseas conocer?: ")
    if encontrar == 'aceleracion':
        print("a = ",aceleracion(F,M1,M2))
    elif encontrar == 'tension':
        print("t = ",tension(F,M1,M2))
    elif encontrar == 'tension caso 1':
        print("tension de la superficie inclinada =",tension_1Angulo(g,M1,aceleracionPI))
    elif encontrar == 'aceleracion caso 1':
        print("aceleracion de la  superficie inclinada =",aceleracion_1Angulo(g,M1,M2,angulo_inclinacion_1))
    elif encontrar == 'tension caso 2':
        print("tension de la superficie inclinada dos angulos =",tension_2Angulos(M1, aceleracionPI2))
    elif encontrar == 'aceleracion caso 2':
        print("tension de la superficie inclinada 2 angulos =",aceleracion_2Angulos(g,M1, M2, angulo_inclinacion_1, angulo_inclinacion_2))
        complemento_0()
        if complemento == 'si':
            if encontrar == 'aceleracion':
                print("t = ",tension(F,M1,M2))
            elif encontrar == 'tension':
                print("a = ",aceleracion(F,M1,M2))
        elif complemento == 'no':
            break
        relleno()
    repeticion_0()
    if repeticion == 'si':
        datos()
    elif repeticion == 'no':
        break