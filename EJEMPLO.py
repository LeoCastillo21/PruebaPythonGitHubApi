# num = input("Ingrese un número: ")
# num2 = input("Ingrese otro número: ")

# def suma(num, num2):

#     return int(num) + int(num2)

# resultado = suma(num, num2)
# print("El resultado de la suma es:", resultado)

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Convertir los valores ingresados a números enteros
num1 = int(num1)
num2 = int(num2)

# Realizar la suma
resultado = num1 + num2

# Imprimir el resultado
print("El resultado de la suma es:", resultado)


import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola, esta es tu primera aplicación de escritorio en Python!")

def center_window(window, width, height):
    # Obtiene el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula las coordenadas X e Y para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Ubica la ventana en el centro de la pantalla
    window.geometry(f"{width}x{height}+{x}+{y}")    






