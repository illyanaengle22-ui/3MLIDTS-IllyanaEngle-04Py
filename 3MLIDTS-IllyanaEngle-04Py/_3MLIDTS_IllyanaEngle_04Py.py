import tkinter as tk
from tkinter import messagebox

##Definicion de funciones
def limpiar_campos():
    txtNombre.delete(0,tk.END)
    txtApellidos.delete(0,tk.END)
    txtTelefono.delete(0,tk.END)
    txtEdad.delete(0,tk.END)
    txtEstatura.delete(0,tk.END)
    var_genero.set(0)
def borrar_fun():
    limpiar_campos() #anidacion de funciones
def guardar_valores():
    #Obtener valores desde los entrys
    nombres = txtNombre.get()
    apellidos = txtApellidos.get()
    telefono = txtTelefono.get()
    edad = txtEdad.get()
    estatura = txtEstatura.get()
    ##Obtener el genero de los RadioButtons

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    ## Generar la cadena de caracteres
    datos = "Nombre: "+ nombres +"\n"+"Apellidos: "+ apellidos +"\n"+"Edad: "+ edad +" anos\n"+"Estatura: "+ estatura +"\n"+"Telefono: "+ telefono +"\n"+"Genero: " +genero
    ## Guardar los datos en el archivo TXT
    with open("D:/Users/Neko/Documents/Programacion_Avanzada/3MDatosAgosto2025Python.txt", "a") as archivo:
        archivo.write(datos+"\n\n")
    ## Mostrar mensaje de confirmacion
    messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+datos)
    txtNombre.delete(0,tk.END)
    txtApellidos.delete(0,tk.END)
    txtTelefono.delete(0,tk.END)
    txtEdad.delete(0,tk.END)
    txtEstatura.delete(0,tk.END)
    var_genero.set(0)

##Creacion de ventana
ventana = tk.Tk()
ventana.geometry("320x350")
ventana.title("Formulacio Ver.01")
#Crear variable para el RadioButton
var_genero = tk.IntVar()

##Creacion de etiquetas y campos de entrada
lblNombre = tk.Label(ventana, text = "Nombre :")
lblNombre.pack()
txtNombre = tk.Entry()
txtNombre.pack()

lblApellidos = tk.Label(ventana, text = "Apellidos :")
lblApellidos.pack()
txtApellidos = tk.Entry()
txtApellidos.pack()

lblTelefono = tk.Label(ventana, text = "Telefono :")
lblTelefono.pack()
txtTelefono = tk.Entry()
txtTelefono.pack()

lblEdad = tk.Label(ventana, text = "Edad :")
lblEdad.pack()
txtEdad = tk.Entry()
txtEdad.pack()

lblEstatura = tk.Label(ventana, text = "Estatura :")
lblEstatura.pack()
txtEstatura = tk.Entry()
txtEstatura.pack()

lblGenero = tk.Label(ventana, text = "Genero :")
lblGenero.pack()
rbHombre = tk.Radiobutton(ventana, text= "Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text= "Mujer", variable=var_genero, value=2)
rbMujer.pack()

##Creacion de Botones
btnBorrar = tk.Button(ventana, text = "Borrar valores", command=borrar_fun)
btnBorrar.pack()
BtnGuardar = tk.Button(ventana, text = "Guardar", command=guardar_valores)
BtnGuardar.pack()

##Ejecucion de ventava
ventana.mainloop()


