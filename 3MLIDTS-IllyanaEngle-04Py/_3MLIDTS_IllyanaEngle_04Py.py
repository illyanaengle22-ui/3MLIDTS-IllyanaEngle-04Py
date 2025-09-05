import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime
import re

# Configuracion
ARCHIVO = "DatosPersonas.txt"

def validar_campos():
    """Validar que todos los campos esten llenos y sean correctos"""
    # Verificar campos vacios
    if not all([txtNombre.get().strip(), txtApellidos.get().strip(), 
               txtTelefono.get().strip(), txtEdad.get().strip(), 
               txtEstatura.get().strip()]):
        raise ValueError("Todos los campos son obligatorios")
    
    # Verificar genero seleccionado
    if var_genero.get() == 0:
        raise ValueError("Debe seleccionar un genero")
    
    # Validar edad
    try:
        edad = int(txtEdad.get().strip())
        if edad < 1 or edad > 120:
            raise ValueError("La edad debe estar entre 1 y 120 anos")
    except ValueError:
        raise ValueError("La edad debe ser un numero valido")
    
    # Validar estatura
    try:
        estatura = float(txtEstatura.get().strip())
        if estatura < 50 or estatura > 250:
            raise ValueError("La estatura debe estar entre 50 y 250 cm")
    except ValueError:
        raise ValueError("La estatura debe ser un numero valido")
    
    # Validar telefono
    telefono = txtTelefono.get().strip()
    numeros_solo = re.sub(r'[^\d]', '', telefono)
    if len(numeros_solo) < 10:
        raise ValueError("El telefono debe tener al menos 10 digitos")
    
    return edad, estatura

def obtener_ruta_archivo():
    """Obtener ruta del archivo en la carpeta del usuario"""
    carpeta_docs = os.path.expanduser("~/Documents/RegistroPersonas")
    if not os.path.exists(carpeta_docs):
        os.makedirs(carpeta_docs)
    return os.path.join(carpeta_docs, ARCHIVO)

def limpiar_campos():
    """Limpiar todos los campos"""
    txtNombre.delete(0, tk.END)
    txtApellidos.delete(0, tk.END)
    txtTelefono.delete(0, tk.END)
    txtEdad.delete(0, tk.END)
    txtEstatura.delete(0, tk.END)
    var_genero.set(0)
    txtNombre.focus()

def guardar_valores():
    """Guardar los valores en el archivo"""
    try:
        # Validar campos
        edad, estatura = validar_campos()
        
        # Obtener valores
        nombre = txtNombre.get().strip().title()
        apellidos = txtApellidos.get().strip().title()
        telefono = txtTelefono.get().strip()
        genero = "Hombre" if var_genero.get() == 1 else "Mujer"
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Crear texto a guardar
        datos = f"""Fecha: {fecha}
Nombre: {nombre}
Apellidos: {apellidos}
Telefono: {telefono}
Edad: {edad} anos
Estatura: {estatura:.1f} cm
Genero: {genero}"""
        
        # Guardar en archivo
        ruta = obtener_ruta_archivo()
        with open(ruta, "a", encoding="utf-8") as archivo:
            if os.path.getsize(ruta) > 0:  # Si el archivo no esta vacio
                archivo.write("\n" + "-" * 40 + "\n")
            archivo.write(datos + "\n")
        
        # Mostrar confirmacion
        messagebox.showinfo("Exito", f"Datos guardados correctamente:\n\n{datos}")
        limpiar_campos()
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar: {str(e)}")

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("350x400")
ventana.title("Registro de Personas")
ventana.resizable(False, False)

# Variable para genero
var_genero = tk.IntVar()

# Titulo
lblTitulo = tk.Label(ventana, text="Registro de Personas", 
                     font=('Arial', 14, 'bold'))
lblTitulo.pack(pady=10)

# Campos de entrada
lblNombre = tk.Label(ventana, text="Nombre:")
lblNombre.pack()
txtNombre = tk.Entry(ventana, width=30)
txtNombre.pack(pady=2)

lblApellidos = tk.Label(ventana, text="Apellidos:")
lblApellidos.pack()
txtApellidos = tk.Entry(ventana, width=30)
txtApellidos.pack(pady=2)

lblTelefono = tk.Label(ventana, text="Telefono:")
lblTelefono.pack()
txtTelefono = tk.Entry(ventana, width=30)
txtTelefono.pack(pady=2)

lblEdad = tk.Label(ventana, text="Edad (anos):")
lblEdad.pack()
txtEdad = tk.Entry(ventana, width=30)
txtEdad.pack(pady=2)

lblEstatura = tk.Label(ventana, text="Estatura (cm):")
lblEstatura.pack()
txtEstatura = tk.Entry(ventana, width=30)
txtEstatura.pack(pady=2)

# Genero
lblGenero = tk.Label(ventana, text="Genero:", font=('Arial', 10, 'bold'))
lblGenero.pack(pady=(10, 5))

frameGenero = tk.Frame(ventana)
frameGenero.pack()

rbHombre = tk.Radiobutton(frameGenero, text="Hombre", 
                         variable=var_genero, value=1)
rbHombre.pack(side=tk.LEFT, padx=10)

rbMujer = tk.Radiobutton(frameGenero, text="Mujer", 
                        variable=var_genero, value=2)
rbMujer.pack(side=tk.LEFT, padx=10)

# Botones
frameBotones = tk.Frame(ventana)
frameBotones.pack(pady=20)

btnLimpiar = tk.Button(frameBotones, text="Limpiar", 
                      command=limpiar_campos, width=12)
btnLimpiar.pack(side=tk.LEFT, padx=5)

btnGuardar = tk.Button(frameBotones, text="Guardar", 
                      command=guardar_valores, width=12)
btnGuardar.pack(side=tk.LEFT, padx=5)

# Informacion del archivo
ruta_info = obtener_ruta_archivo()
lblInfo = tk.Label(ventana, text=f"Se guarda en: {ruta_info}", 
                  font=('Arial', 8), fg='gray', wraplength=320)
lblInfo.pack(pady=10)

# Enfocar primer campo y ejecutar
txtNombre.focus()
ventana.mainloop()


