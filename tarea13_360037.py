# Edson Antonio Piñón González
# 360037
# Tarea 13

from tkinter import *


# Creación de la ventana
ventana = Tk()
ventana.geometry("700x400") # dimensiones
ventana.title("Edson Antonio Piñón González, 360037") # título

# Creación de la Entry
cajaTexto = Entry(ventana, width=15)
cajaTexto.pack(pady=20)

def cambio_color():
    try:
        if cajaTexto.get() == "Rojo":
            boton_color["fg"] = "red"
            boton_color["bg"] = "white"
            boton_color["text"] = "¡Soy rojo!"
        elif cajaTexto.get() == "Amarillo":
            boton_color["fg"] = "yellow"
            boton_color["bg"] = "light blue"
            boton_color["text"] = "¡Soy amarillo!"
    except:
        pass

boton_color = Button(ventana, text="¡Cambia mi color!", command=cambio_color)
boton_color.pack(pady=20)

etiqueta = Label(ventana, text="Escriba 'Rojo' para cambiar a color rojo. Escriba 'Amarillo' para cambiar a color amarillo. Pulse el botón a continuación.")
etiqueta.pack(pady=20)


ventana.mainloop()