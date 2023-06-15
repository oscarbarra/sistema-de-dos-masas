#abrir como carpeta
#definicion de las constantes 
#probando el commit
P1 = 0; P2 = 0; M1 = 0; M2 = 0; T = 0; A = 0 ; F = 0; complemento = ''; repeticion = ''

#creacion de los modelos
def aceleracion(F,M1,M2):
    global A
    A = (F/(M1+M2))
    return A

def tension(F,M1,M2):
    global T
    T = (M2*(F/(M1+M2)))
    return T

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
    global P1,P2,M1,M2,F
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
    encontrar = input("que desas conocer?: ")
    if encontrar == 'aceleracion':
        print("a = ",aceleracion(F,M1,M2))
    elif encontrar == 'tension':
        print("t = ",tension(F,M1,M2))
    while True:
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