from tkinter import *
import math
from tkinter import ttk

class calculo:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x500") #dimencinoes ventana principal
        self.ventana.iconbitmap("icono.ico") # monito
        self.ventana.title("cinematica") #titulo
        self.ventana.config(bg='pink') #color del fondo
        
#----------------------------------------------------
# crear capsulas 
#----------------------------------------------------        
        self.peso_objeto_1 =Label(self.ventana,text='Peso objeto 1', font=('arial',16))
        self.peso_objeto_1.config(width=11,height=1,bg="cyan")
        self.peso_objeto_1.place(x=50,y=50)
        
        self.peso_objeto_1_relleno=StringVar()
        self.peso_objeto_1_relleno=Entry(self.ventana,bd=2 ,font=('Magic Bright Serif',10))
        self.peso_objeto_1_relleno.place(x=50,y=75)
        
        
        self.l_peso_objeto_2 =Label(self.ventana,text='Peso objeto 2', font=('arial',16))
        self.l_peso_objeto_2.config(width=11,height=1,bg="cyan")
        self.l_peso_objeto_2.place(x=50,y=100)
        
        self.e_peso_objeto_2_relleno=StringVar()
        self.e_peso_objeto_2_relleno=Entry(self.ventana,bd=2, font=('Magic Bright Serif',10))
        self.e_peso_objeto_2_relleno.place(x=50,y=125)        
        
        self.masa_1 =Label(self.ventana,text='Masa 1' ,font=('arial',16))
        self.masa_1.config(width=11,height=1,bg="cyan")
        self.masa_1.place(x=50,y=150)
        
        self.masa_1_relleno=StringVar()
        self.masa_1_relleno=Entry(self.ventana,bd=2 ,font=('Magic Bright Serif',10))
        self.masa_1_relleno.place(x=50,y=175)
        
        
        self.calculo=Label(self.ventana,text='Selccione que decea calcular' ,font=('arial',16))
        self.calculo.config(bg="cyan")
        self.calculo.place(x=475,y=50)
        
        self.var_combo1=StringVar()
        self.op_combo= ('','aceleracion','calculo 2','calculo 3') #discustir
        self.combobox=ttk.Combobox(self.ventana, state='readonly',
                                    width= 20 ,font= ('Magic Bright Serif',10,'bold'),
                                    textvariable=self.var_combo1,values=self.op_combo)
        
        self.combobox.current(0)
        self.combobox.place(x=475,y=90)
        
        self.resultados =Label(self.ventana,text='Resultado',bd=2 , font=('arial',16))
        self.resultados.config(width=11,height=1,bg="cyan")
        self.resultados.place(x=475,y=220)
        
        self.resultados=Label(self.ventana)
        self.resultados.config(width=40,height=15)
        self.resultados.place(x=475,y=250)
    
    #------------------------------------------------------------------------------------------
    # botones
    #------------------------------------------------------------------------------------------
        self.boton_1=Button(self.ventana,text='Calcular',bd=2 , font=('arial',16))
        self.boton_1.config(width=10,height=3)
        self.boton_1.place(x=20,y=350)
        
        self.boton_2=Button(self.ventana,text='Limpiar',bd=2 , font=('arial',16))
        self.boton_2.config(width=10,height=3)
        self.boton_2.place(x=200,y=350)
        
        self.boton_3 =Button(self.ventana,text="EXIT",command=exit)#,bg="RED")
        self.boton_3.config(width=4,height=1)
        self.boton_3.place(x=155, y= 450)
        
        


        self.ventana.mainloop()
              
    #def DATOS(self)
        
        
calculo() #llama a todos 