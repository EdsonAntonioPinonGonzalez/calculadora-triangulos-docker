# Edson Antonio Piñón González
# 360037
# Tarea 14

from tkinter import *

# Creación de la ventana
ventana = Tk()
ventana.geometry("400x225")
ventana.title("360037 - Edson Antonio Piñón González")


# Primer etiqueta
etiqueta_1 = Label(ventana, text="Programa que Calcula Áreas de Triángulos")
etiqueta_1.pack(pady=10)


# Segunda etiqueta
etiqueta_2 = Label(ventana, text="Introduce la base:")
etiqueta_2.pack()


# Caja de texto (base)
cajaBase = Entry(ventana, width=30)
cajaBase.pack()


# Tercera etiqueta
etiqueta_3 = Label(ventana, text="Introduce la altura:")
etiqueta_3.pack()


# Caja de texto (altura)
cajaAltura = Entry(ventana, width=30)
cajaAltura.pack()


# Función para calcular el área
def calcular_area():
    try:
        # Se obtendrán los datos de las cajas de texto para poder realizar el cálculo
        base = float(cajaBase.get())
        altura = float(cajaAltura.get()) # Los valores de las dos cajas se transforman a datos float para realizar el cálculo, ya que son str inicialmente
        if base > 0 and altura > 0:
            area = base * altura / 2


            # Creación del archivo de texto que servirá como bitácora de los datos
            f = open("datosproyecto.txt", "a+")
            datos_a_guardar = "Base: " + str(base) + ", Altura: " + str(altura) + ". Area Triangulo: " + str(area) + "\n"
            f.write(datos_a_guardar)
            f.close()


            # El resultado de la operación se mostrará en la etiqueta 4, reemplazando el texto que ya está
            etiqueta_4["text"] = "El área es " + str(area)
        else:
            etiqueta_4["text"] = "ERROR: Tanto la base como el área deben de ser mayores a 0"
    except ValueError:
        # Evitar que se introduzcan caracteres no numéricos
        etiqueta_4["text"] = "ERROR: Solo introduzca datos numéricos"



# Botón para calcular el área
boton_calculo = Button(ventana, text="Calcular", command=calcular_area)
boton_calculo.pack(pady=10)


# Cuarta etiqueta
etiqueta_4 = Label(ventana, text="Aquí se mostrará el resultado")
etiqueta_4.pack()


# mainloop de la ventana
ventana.mainloop()