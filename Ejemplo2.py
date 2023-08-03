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

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi Aplicación")

# Configurar la ventana para que esté centrada
center_window(ventana, 400, 200)

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para mostrar un mensaje")
etiqueta.pack(pady=20)

# Crear un botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()


import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

ventana = tk.Tk()
ventana.title("Ventana Centrada")

# Definir el ancho y alto de la ventana
width = 400
height = 300

# Usar la función para centrar la ventana
center_window(ventana, width, height)

# Agregar contenido a la ventana, como etiquetas, botones, etc.

ventana.mainloop()
