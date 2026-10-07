# Interfaz gráfica de usuario (GUI) en Python con Tkinter

from tkinter import *
from tkinter import ttk

ventanaPrincipal = Tk()
ventanaPrincipal.geometry("800x400")
ventanaPrincipal.title("Mi primer interfaz gráfica con Python")

# el orden en el que vayan empaquetando los objetos que contenga la ventana, es el orden en el que se muestran
# pack va por renglones
# grid por columnas y filas
etiqueta1 = Label(ventanaPrincipal, text="Calculadora")
etiqueta1.grid(row=0, column=1)

cajaTexto1 = Entry(ventanaPrincipal, width=8)
cajaTexto1.grid(row=1, column=0)

opciones = ttk.Combobox(ventanaPrincipal, values=["Sumar", "Restar", "Multiplicar", "Dividir"])
opciones.current(0)
opciones.grid(row=1, column=1)

cajaTexto2 = Entry(ventanaPrincipal, width=8)
cajaTexto2.grid(row=1, column=2)

etiqueta3 = Label(ventanaPrincipal, text="Aquí se va a mostrar el resultado")
etiqueta3.grid(column=1, row=2)

def operaciones():
    if opciones.get() == "Sumar":
        try:
            x = float(cajaTexto1.get())
            y = float(cajaTexto2.get())
            resultado = x + y
            etiqueta3["text"] = "El resultado es " + str(resultado)
        except:
            etiqueta3["text"] = "Datos Incorrectos"
    elif opciones.get() == "Restar":
        try:
            x = float(cajaTexto1.get())
            y = float(cajaTexto2.get())
            resultado = x - y
            etiqueta3["text"] = "El resultado es " + str(resultado)
        except:
            etiqueta3["text"] = "Datos Incorrectos"
    elif opciones.get() == "Multiplicar":
        try:
            x = float(cajaTexto1.get())
            y = float(cajaTexto2.get())
            resultado = x * y
            etiqueta3["text"] = "El resultado es " + str(resultado)
        except:
            etiqueta3["text"] = "Datos Incorrectos"
    else:
        try:
            x = float(cajaTexto1.get())
            y = float(cajaTexto2.get())
            resultado = x / y
            etiqueta3["text"] = "El resultado es " + str(resultado)
        except:
            etiqueta3["text"] = "Datos Incorrectos"

boton1 = Button(ventanaPrincipal, text="Realizar operación", command=operaciones)
boton1.grid(column=1, row=3)

boton2 = Button(ventanaPrincipal, text="Boton Nuevo!")


ventanaPrincipal.mainloop() # al final del código de la interfaz gráfica