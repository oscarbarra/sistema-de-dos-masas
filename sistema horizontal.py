#abrir como carpeta
#definicion de las constantes 
#modificar este codigo y no el MAIN
#python 3.11.4

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import math

#--creacion de la ventana pricipal--
ventana = Tk()
ventana.title("sistemas con dos masas")
ventana.geometry("350x350")
ventana.config(bg="pink")

#---punto de control entre sistemas---
def encontrar():
    global combo_2, combo_3, combo_4#combo_2 = 'datos_horizontal'
    seleccion_1 = combo_1.get() #recupera la primera eleccion
    opciones_2 = ["aceleracion", "tension"] #lista con nuevas opciones
    if seleccion_1 == "horizontal":
        combo_2 = ttk.Combobox(ventana, state="readonly", values=opciones_2) #nueva ventana de eleccion
        combo_2.place(x=0, y=25)

        boton_alfa = Button(ventana, text="aceptar", command=datos_horizontal)
        boton_alfa.place(x=150, y=25)
    if seleccion_1 == "inclinado(1 angulo)":
        combo_3 = ttk.Combobox(ventana, state="readonly", values=opciones_2)
        combo_3.place(x=0, y=25)

        boton_beta = Button(ventana, text="aceptar", command=inclinado_A1)
        boton_beta.place(x=150, y=25)
    if seleccion_1 == "inclinado(2 angulos)":
        combo_4 = ttk.Combobox(ventana, state="readonly", values=opciones_2)
        combo_4.place(x=0, y=25)

        boton_gama = Button(ventana, text="aceptar", command=inclinado_A2)
        boton_gama.place(x=150, y=25) 

#-----todo lo relacionado al plano horizontal-----
def datos_horizontal():
    global x, y, z, seleccion_2, btn_misterioso #lo subimos para usarlos en 'confirmacion_1 y 2'
    seleccion_2 = combo_2.get() #recupera el valor de la eleccion 2
    if seleccion_2 == "aceleracion":
        x= DoubleVar() #dato clave 1
        masa_1 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada1_1 = Entry(ventana, textvariable=x).place(x=55, y=52) # entrada 1
        #btn_1 = Button(ventana, text="aceptar",).place(x=195, y=30) #no se esta usando

        y= DoubleVar() #dato clave 2
        masa_2 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada2_1 = Entry(ventana, textvariable=y).place(x=55, y=82) # entrada 2
        #btn_2 = Button(ventana, text="aceptar").place(x=195, y=60) # no se esta usando
    
        z= DoubleVar() # dato clave 3
        fuerza_A = Label(ventana, text="fuerza", bg="cyan").place(x=0, y=110)
        entrada3_1 = Entry(ventana, textvariable=z).place(x=55, y=112) # entrada 3
        #btn_3 = Button(ventana, text="aceptar").place(x=230, y=90) # no se esta usando

        btn_misterioso = Button(ventana, text="aceptar todo", command=confirmacion_1)
        btn_misterioso.place(x=250, y=75)

    if seleccion_2 == "tension": #la tension depende de la aceleracion
        x= DoubleVar() #dato clave 1
        masa_1 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada4_1 = Entry(ventana, textvariable=x).place(x=55, y=52) # entrada 1

        y= DoubleVar() #dato clave 2
        masa_2 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada5_1 = Entry(ventana, textvariable=y).place(x=55, y=82) # entrada 2
        #btn_2 = Button(ventana, text="aceptar").place(x=195, y=60) # no se esta usando

        z=DoubleVar() # dato clave 3
        fuerza_A = Label(ventana, text="fuerza", bg="cyan").place(x=0, y=110)
        entrada6_1 = Entry(ventana, textvariable=z).place(x=55, y=112) # entrada 3
        #btn_3 = Button(ventana, text="aceptar").place(x=230, y=90) # no se esta usando

        btn_misterioso = Button(ventana, text="aceptar todo", command=confirmacion_1)
        btn_misterioso.place(x=250, y=75)
        
def confirmacion_1():
    global a, b, masa1, masa2, fuerza #a,b se van a 'confirmacion_2' # fuerza esta lista
    masa1 = x.get()
    masa2 = y.get()
    fuerza = z.get()
    if fuerza != 0:
        if masa1 != 0:
            if masa2 != 0:
                respuesta = askyesno(title="ultima pregunta",
                                     message="listo para conocer las respuestas")
                if respuesta:
                    if seleccion_2 == "aceleracion":
                        solu1 = (fuerza/(masa1+masa2))
                        etiq1 = Label(ventana, text="la aceleracion es: "+str(solu1), bg="white")
                        etiq1.place(x=10, y=202)
                    elif seleccion_2 == "tension":
                        solu2 = (masa1*(fuerza/(masa1+masa2)))
                        etiq2 = Label(ventana, text="la tension es: "+str(solu2), bg="white")
                        etiq2.place(x=10, y=232)
    if fuerza != 0:
        if masa1 == 0:
            a = DoubleVar()
            peso1_1 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=140)
            entrada7_1 = Entry(ventana, textvariable=a).place(x=55, y=142)
            if masa2 == 0:
                b = DoubleVar()
                peso2_1 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=170)
                entrada8_1 = Entry(ventana, textvariable=b).place(x=55, y=172)
                btn1_1= Button(ventana, text="resultado", command=confirmacion_2).place(x=250, y=150)
    if fuerza != 0:
        if masa1 != 0:
            if masa2 == 0:
                b = DoubleVar()
                peso2_1 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=140)
                entrada9_1 = Entry(ventana, textvariable=b).place(x=55, y=142)
                btn2_1= Button(ventana, text="resultado", command=confirmacion_3).place(x=250, y=150)
    if fuerza != 0:
        if masa2 != 0:
            if masa1 == 0:
                a = DoubleVar()
                peso2_1 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=140)
                entrada10_1 = Entry(ventana, textvariable=a).place(x=55, y=142)
                btn3_1= Button(ventana, text="resultado", command=confirmacion_4).place(x=250, y=150)


def confirmacion_2():
    peso1 = a.get(); peso2 = b.get()
    masa1 = peso1 / 9.8; masa2 = peso2 / 9.8
    respuesta = askyesno(title="ultima confirmacion", 
                        message="¡listo para conocer la respuesta!")
    if respuesta: #revision de los datos
        if seleccion_2 == "aceleracion":
            solu3 = (fuerza/(masa1+masa2))
            etiq3 = Label(ventana, text="la aceleracion es: "+str(solu3), bg="white")
            etiq3.place(x=10, y=202)
        elif seleccion_2 == "tension":
            solu4 = (masa1*(fuerza/(masa1+masa2)))
            etiq4 = Label(ventana, text="la tension es: "+str(solu4), bg="white")
            etiq4.place(x=10, y=232)

def confirmacion_3():
    peso2 = b.get()
    masa2 = peso2 / 9.8
    respuesta = askyesno(title="ultima confirmacion", 
                        message="¡listo para conocer la respuesta!")
    if respuesta: #revision de los datos
        if seleccion_2 == "aceleracion":
            solu5 = (fuerza/(masa1+masa2))
            etiq5 = Label(ventana, text="la aceleracion es: "+str(solu5), bg="white")
            etiq5.place(x=10, y=202)
        elif seleccion_2 == "tension":
            solu6 = (masa1*(fuerza/(masa1+masa2)))
            etiq6 = Label(ventana, text="la tension es: "+str(solu6), bg="white")
            etiq6.place(x=10, y=232)

def confirmacion_4():
    peso1 = a.get()
    masa1 = peso1 / 9.8
    respuesta = askyesno(title="ultima confirmacion", 
                        message="¡listo para conocer la respuesta!")
    if respuesta: #revision de los datos
        if seleccion_2 == "aceleracion":
            solu7 = (fuerza/(masa1+masa2))
            etiq7 = Label(ventana, text="la aceleracion es: "+str(solu7), bg="white")
            etiq7.place(x=10, y=202)
        elif seleccion_2 == "tension":
            solu8 = (masa1*(fuerza/(masa1+masa2)))
            etiq8 = Label(ventana, text="la tension es: "+str(solu8), bg="white")
            etiq8.place(x=10, y=232)

#-----plano inclinado con un angulo-----
def inclinado_A1():
    global x_2, y_2, z_2, seleccion_3
    seleccion_3 = combo_3.get()
    if seleccion_3 == "aceleracion":
        x_2 = DoubleVar()
        masa1_2 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada1_2 = Entry(ventana, textvariable=x_2).place(x=55, y=52)

        y_2 = DoubleVar()
        masa2_2 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada2_2 = Entry(ventana, textvariable=y_2).place(x=55, y=82)

        z_2 = DoubleVar()
        angulo1_2 = Label(ventana, text="angulo", bg="cyan").place(x=0, y=112)
        entrada3_2 = Entry(ventana, textvariable=z_2).place(x=55, y=112)

        btn1_2 = Button(ventana, text="aceptar todo", command=confirmacion_5)
        btn1_2.place(x=250, y=75)
    if seleccion_3 =="tension":
        x_2 = DoubleVar()
        masa1_2 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada4_2 = Entry(ventana, textvariable=x_2).place(x=55, y=52)

        y_2 = DoubleVar()
        masa2_2 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada5_2 = Entry(ventana, textvariable=y_2).place(x=55, y=82)

        z_2 = DoubleVar()
        angulo1_2 = Label(ventana, text="angulo", bg="cyan").place(x=0, y=112)
        entrada6_2 = Entry(ventana, textvariable=z_2).place(x=55, y=112)

        btn1_1 = Button(ventana, text="aceptar todo", command=confirmacion_5)
        btn1_1.place(x=250, y=75)


#---funciones del plano inclinado con 1 angulo---
def confirmacion_5():
    global a_2, b_2, masa1_2, masa2_2, angulo1_2
    masa1_2 = x_2.get(); masa2_2 = y_2.get()
    angulo1_2 = z_2.get()
    if angulo1_2 != 0:
        if masa1_2 != 0:
            if masa2_2 != 0:
                respuesta = askyesno(title="ultima pregunta",
                                     message="preparado para saber la respuesta?")
                if respuesta:
                    if seleccion_3 == "aceleracion":
                        solu9 = (((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2))
                        etiq9 = Label(ventana, text="la aceleracion es: "+str(solu9), bg="white")
                        etiq9.place(x=10, y=202)
                    elif seleccion_3 =="tension":
                        solu10 = ((masa1_2*(((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2)))+(masa1_2*9.8*(math.sin(math.radians(angulo1_2)))))
                        etiq10 = Label(ventana, text="la tension es: "+str(solu10), bg="white")
                        etiq10.place(x=10, y=232)
    if angulo1_2 != 0:
        if masa1_2 == 0:
            a_2 = DoubleVar()
            peso1_2 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=140)
            entrada7_2 = Entry(ventana, textvariable=a_2).place(x=55, y=142)
            if masa2_2 == 0:
                b_2 = DoubleVar()
                peso2_2 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=170)
                entrada8_2 = Entry(ventana, textvariable=b_2).place(x=55, y=172)
                btn1_2= Button(ventana, text="resultado", command=confirmacion_6).place(x=250, y=150)
    if angulo1_2 != 0:
        if masa1_2 != 0:
            if masa2_2 == 0:
                b_2 = DoubleVar()
                peso2_2 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=140)
                entrada9_2 = Entry(ventana, textvariable=b_2).place(x=55, y=142)
                btn2_2= Button(ventana, text="resultado", command=confirmacion_7).place(x=250, y=150)
    if angulo1_2 != 0:
        if masa2_2 != 0:
            if masa1_2 == 0:
                a_2 = DoubleVar()
                peso_1 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=140)
                entrada_10 = Entry(ventana, textvariable=a_2).place(x=55, y=142)
                btn_3_2= Button(ventana, text="resultado", command=confirmacion_8).place(x=250, y=150)


def confirmacion_6():
    peso1_2 = a_2.get(); peso2_2 = b_2.get()
    masa1_2 = peso1_2/9.8; masa2_2 = peso2_2/9.8
    respuesta = askyesno(title="ultima pregunta",
                         message="estas listo?")
    if respuesta:
        if seleccion_3 == "aceleracion":
            solu11 = (((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2))
            etiq11 = Label(ventana, text="la aceleracion es: "+str(solu11), bg="white")
            etiq11.place(x=10, y=202)
        elif seleccion_3 =="tension":
            solu12 = ((masa1_2*(((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2)))+(masa1_2*9.8*(math.sin(math.radians(angulo1_2)))))
            etiq12 = Label(ventana, text="la tension es: "+str(solu12), bg="white")
            etiq12.place(x=10, y=232)

def confirmacion_7():
    peso2_2 = b_2.get()
    masa2_2 = peso2_2/9.8
    respuesta = askyesno(title="ultima pregunta",
                         message="estas listo?")
    if respuesta:
        if seleccion_3 == "aceleracion":
            solu13 = (((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2))
            etiq13 = Label(ventana, text="la aceleracion es: "+str(solu13), bg="white")
            etiq13.place(x=10, y=202)
        elif seleccion_3 =="tension":
            solu14 = ((masa1_2*(((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2)))+(masa1_2*9.8*(math.sin(math.radians(angulo1_2)))))
            etiq14 = Label(ventana, text="la tension es: "+str(solu14), bg="white")
            etiq14.place(x=10, y=232)

def confirmacion_8():
    peso1_2 = a_2.get()
    masa1_2 = peso1_2/9.8
    respuesta = askyesno(title="ultima pregunta",
                         message="estas listo?")
    if respuesta:
        if seleccion_3 == "aceleracion":
            solu15 = (((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2))
            etiq15 = Label(ventana, text="la aceleracion es: "+str(solu15), bg="white")
            etiq15.place(x=10, y=202)
        elif seleccion_3 =="tension":
            solu16 = ((masa1_2*(((masa2_2*9.8)-((masa1_2*9.8)*(math.sin(math.radians(angulo1_2)))))/(masa1_2+masa2_2)))+(masa1_2*9.8*(math.sin(math.radians(angulo1_2)))))
            etiq16 = Label(ventana, text="la tension es: "+str(solu16), bg="white")
            etiq16.place(x=10, y=232)

#------------todo del plano inclinado con 2 angulos----------------------
def inclinado_A2():
    global x_3, y_3, z_3, w_3, seleccion_4
    seleccion_4 = combo_4.get()
    if seleccion_4 == "aceleracion":
        x_3 = DoubleVar()
        masa1_3 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada1_3 = Entry(ventana, textvariable=x_3).place(x=55, y=52)

        y_3 = DoubleVar()
        masa2_3 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada2_3 = Entry(ventana, textvariable=y_3).place(x=55, y=82)

        z_3 = DoubleVar()
        angulo1_3 = Label(ventana, text="angulo 1", bg="cyan").place(x=0, y=110)
        entrada3_3 = Entry(ventana, textvariable=z_3).place(x=55, y=112)
        
        w_3 = DoubleVar()
        angulo2_3 = Label(ventana, text="angulo 2", bg="cyan").place(x=0, y=140)
        entrada4_3 = Entry(ventana, textvariable=w_3).place(x=55, y=142)

        btn1_3 = Button(ventana, text="aceptar todo", command=confirmacion_9)
        btn1_3.place(x=250, y=75)
    if seleccion_4 =="tension":
        x_3 = DoubleVar()
        masa1_3 = Label(ventana, text="masa 1", bg="cyan").place(x=0, y=50)
        entrada5_3 = Entry(ventana, textvariable=x_3).place(x=55, y=52)

        y_3 = DoubleVar()
        masa2_3 = Label(ventana, text="masa 2", bg="cyan").place(x=0, y=80)
        entrada6_3 = Entry(ventana, textvariable=y_3).place(x=55, y=82)

        z_3 = DoubleVar()
        angulo1_3 = Label(ventana, text="angulo 1", bg="cyan").place(x=0, y=110)
        entrada7_3 = Entry(ventana, textvariable=z_3).place(x=55, y=112)
        
        w_3 = DoubleVar()
        angulo2_3 = Label(ventana, text="angulo 2", bg="cyan").place(x=0, y=140)
        entrada8_3 = Entry(ventana, textvariable=w_3).place(x=55, y=142)

        btn1_3 = Button(ventana, text="aceptar todo", command=confirmacion_9)
        btn1_3.place(x=250, y=75)

def confirmacion_9():
    global masa1_3, masa2_3, angulo1_3, angulo2_3, a_3, b_3
    masa1_3 = x_3.get(); masa2_3 = y_3.get()
    angulo1_3 = z_3.get(); angulo2_3 = w_3.get()
    if angulo1_3 != 0:
        if angulo2_3 != 0:
            if masa1_3 != 0:
                if masa2_3 != 0:
                    respuesta = askyesno(title="ultima pregunta",
                                         message="preparado para saber la respuesta?")
                    if respuesta:
                        if seleccion_4 == "aceleracion":
                            solu17 = ((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3))
                            etiq17 = Label(ventana, text="la aceleracion es: "+str(solu17), bg="white")
                            etiq17.place(x=10, y=202)
                        elif seleccion_4 =="tension":
                            solu18 = ((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-(masa2_3*((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3)))
                            etiq18 = Label(ventana, text="la tension es: "+str(solu18), bg="white")
                            etiq18.place(x=10, y=232)
    if angulo1_3 != 0:
        if angulo2_3 != 0:
            if masa1_3 == 0:
                a_3 = DoubleVar()
                peso1_3 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=170)
                entrada9_3 = Entry(ventana, textvariable=a_3, bg="white").place(x=55, y=172)
                if masa2_3 == 0:
                    b_3 = DoubleVar()
                    masa2_3 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=200)
                    entrada2_3 = Entry(ventana, textvariable=b_3).place(x=55, y=202)
                    btn1_3 = Button(ventana, text="resultado", command=confirmacion_10).place(x=250, y=150)

    if angulo1_3 != 0:
        if angulo2_3 != 0:
            if masa1_3 != 0:
                if masa2_3 == 0:
                    b_3 = DoubleVar()
                    peso2_3 = Label(ventana, text="peso 2", bg="cyan").place(x=0, y=170)
                    entrada10_3 = Entry(ventana, textvariable=b_3).place(x=55, y=172)
                    btn2_3 = Button(ventana, text="resultado", command=confirmacion_11).place(x=250, y=150)

    if angulo1_3 != 0:
        if angulo2_3 != 0:
            if masa2_3 != 0:
                if masa1_3 == 0:
                    a_3 = DoubleVar()
                    peso1_3 = Label(ventana, text="peso 1", bg="cyan").place(x=0, y=170)
                    entrada11_3 = Entry(ventana, textvariable=a_3).place(x=55, y=172)
                    btn3_3 = Button(ventana, text="resultado", command=confirmacion_12).place(x=250, y=150)

def confirmacion_10():
    peso1_3 = a_3.get(); peso2_3 = b_3.get()
    masa1_3 = peso1_3/9.8; masa2_3 = peso2_3/9.8
    respuesta = askyesno(title="ultima pregunta",
                                         message="preparado para saber la respuesta?")
    if respuesta:
        if seleccion_4 == "aceleracion":
            solu19 = ((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3))
            etiq19 = Label(ventana, text="la aceleracion es: "+str(solu19), bg="white")
            etiq19.place(x=10, y=232)
        elif seleccion_4 =="tension":
            solu20 = ((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-(masa2_3*((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3)))
            etiq20 = Label(ventana, text="la tension es: "+str(solu20), bg="white")
            etiq20.place(x=10, y=262)

def confirmacion_11():
    peso2_3 = b_3.get()
    masa2_3 = peso2_3/9.8
    respuesta = askyesno(title="ultima pregunta",
                                         message="preparado para saber la respuesta?")
    if respuesta:
        if seleccion_4 == "aceleracion":
            solu21 = ((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3))
            etiq21 = Label(ventana, text="la aceleracion es: "+str(solu21), bg="white")
            etiq21.place(x=10, y=232)
        elif seleccion_4 =="tension":
            solu22 = ((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-(masa2_3*((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3)))
            etiq22 = Label(ventana, text="la tension es: "+str(solu22), bg="white")
            etiq22.place(x=10, y=262)


def confirmacion_12():
    peso1_3 = a_3.get()
    masa1_3 = peso1_3/9.8
    respuesta = askyesno(title="ultima pregunta",
                                         message="preparado para saber la respuesta?")
    if respuesta:
        if seleccion_4 == "aceleracion":
            solu23 = ((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3))
            etiq23 = Label(ventana, text="la aceleracion es: "+str(solu23), bg="white")
            etiq23.place(x=10, y=232)
        elif seleccion_4 =="tension":
            solu24 = ((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-(masa2_3*((((masa2_3*9.8)*(math.sin (math.radians(angulo2_3))))-((masa1_3*9.8)*(math.sin(math.radians(angulo1_3)))))/(masa1_3+masa2_3)))
            etiq24 = Label(ventana, text="la tension es: "+str(solu24), bg="white")
            etiq24.place(x=10, y=262)



#--inicio del programa--
opciones_1 = ["horizontal", "inclinado(1 angulo)", "inclinado(2 angulos)"] #lista de opciones
combo_1 = ttk.Combobox(ventana, state="readonly", values=opciones_1) #contenerdor de las opciones
combo_1.place(x=0, y=0) #lo muestra en pantalla

btn_principal = Button(ventana, text="aceptar", command=encontrar).place(x=150, y=0)
#--------------------------------------------------------------

ventana.mainloop()