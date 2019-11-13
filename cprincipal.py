from tkinter import *
from tkinter import ttk
from sintomas import *

def seleccion():
    vb.destroy()

#Atributos visuales -> modificar a necesidad
vb = Tk()
vb.title('Pesdet')
vb.geometry('250x100')

#En esta variable se guarda el cultivo a trabajar
opcion = IntVar()

#Botones para seleccion de cultivo -> modificar valores de ser necesario
check_enf = Radiobutton(vb, text='Revisar enfermedades', value=0, variable=opcion)
chexk_plagas = Radiobutton(vb, text='Revisar plagas', value=1, variable=opcion)

#Con este boton se realiza la verificacion de el cultivo seleciconado
btn_opcion = Button(vb, text='Empezar', command=seleccion)

#Posicionamiento de los elementos en la ventana
check_enf.place(relx=0, rely=0.1)
chexk_plagas.place(relx=0.55, rely=0.1)
btn_opcion.place(relx=0.5, rely=0.8, anchor=CENTER)

vb.mainloop()

#-----------------------------------------------------------------------------------------------
def clicked():
    ventana.destroy()

#Atributos visuales -> modificar a necesidad
ventana = Tk()
ventana.title('Pesdet')
ventana.geometry('400x150')

#En esta variable se guarda el cultivo a trabajar
cultivo = IntVar()

#Botones para seleccion de cultivo -> modificar valores de ser necesario
cafe = Radiobutton(ventana, text='Café', value=1, variable=cultivo)
platano = Radiobutton(ventana, text='Plátano', value=2, variable=cultivo)
maiz = Radiobutton(ventana, text='Maíz tradicional', value=3, variable=cultivo)
frijol = Radiobutton(ventana, text='Frijol', value=4, variable=cultivo)
citrico = Radiobutton(ventana, text='Cítricos', value=5, variable=cultivo)

#Con este boton se realiza la verificacion de el cultivo seleciconado
btn_seleccion = Button(ventana, text='Empezar', command=clicked)

#Posicionamiento de los elementos en la ventana
cafe.place(relx=0.1, rely=0.1)
platano.place(relx=0.1, rely=0.25)
maiz.place(relx=0.1, rely=0.4)
frijol.place(relx=0.1, rely=0.55)
citrico.place(relx=0.1, rely=0.7)
btn_seleccion.place(relx=0.5, rely=0.9, anchor=CENTER)

if opcion.get() == 0:
    vb.mainloop()
#--------------------------------------------------------------------------------------------------
def diagnosticar():
    ventanaSins.destroy()

#Atributos de la ventana que muestra los posibles sintomas que puede presentar un determinado cultivo
ventanaSins = Tk()
ventanaSins.title('Pesdet')
ventanaSins.geometry('500x500')

#Esta funcion carga el sintoma en una lista de sintomas de cultivo

#Esta variable sintomas genera una lista de todos los sintomas que puede presentar un cultivo
sintomas_cultivo = []
#Con esta variable se van a crear las casillas de verificacion
sintomasV = []
casillas = []

#Sintomas del cafe
if cultivo.get() == 1:
    sintomas_cultivo = [1, 2, 3, 4, 5]
#Sintomas del platano
elif cultivo.get() == 2:
    sintomas_cultivo = [6, 7, 8, 14, 9, 10, 11, 12, 13]
#sintomas maiz
elif cultivo.get() == 3:
    sintomas_cultivo = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
#sintomas frijol
elif cultivo.get() == 4:
    sintomas_cultivo = [15, 17, 18, 16, 19, 20, 21, 22, 23, 24, 25]
#Sintomas de los cultivos de citricos
elif cultivo.get() == 5:
    sintomas_cultivo = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

btn_calculoenf = Button(ventanaSins, text='Diagnosticar', command=diagnosticar)
btn_calculoenf.place(relx=0.7, rely=0.5)

for s in range(len(sintomas_cultivo)):
    sintomasV.append(False)
    sintomasV[s] = BooleanVar()
    casillas.append(Checkbutton(ventanaSins, text=sintomas[sintomas_cultivo[s]], variable=sintomasV[s]))
    casillas[s].place(relx=0.1, rely=(s/len(sintomas_cultivo)))

ventanaSins.mainloop()
#En esta lista se van a guardar los sintomas detectados por el usuario
#es aqui donde se opera el calculo de la enfermedad
sins_enf = []
for s in range(len(sintomasV)):
    if sintomasV[s].get():
        sins_enf.append(sintomas[sintomas_cultivo[s]])

#print(sins_enf)
ills = consultarEnfermedad(sins_enf)
#----------------------------------------------------------------------------
#En la ultima ventana se muestra cual enfermedad padece la planta
#Tambien se debe agregar el tratamiento pertinente para la enfermedad
ventanaD = Tk()
ventanaD.title('Diagnóstico')
ventanaD.geometry('500x500')

texto = 'Enfermedad detectada: ' + ills[0]
label_diagnostico = Label(ventanaD, text=texto)
label_diagnostico.place(relx=0.5, rely=0.5, anchor=CENTER)

ventanaD.mainloop()