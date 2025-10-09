import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector #libreria para la conexion a la bd
##Definicion de funciones

def InsertarRegistros(nombre, apellido, edad, estatura, telefono, genero):
    try:
        conexion = mysql.connector.Connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "formulario3m",
            port = "3307"
            )

        cursor = conexion.cursor()
        stringQuery = "INSERT INTO registros_usuario(Nombre, Apellidos, Edad, Estatura, Telefono, Genero) VALUES(%s,%s,%s,%s,%s,%s)"
        valores = nombre, apellido, edad, estatura, telefono, genero
        cursor.execute(stringQuery, valores)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("inserccion correcta a la base de datos","Los datos fueron guardados")
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexion a la base de datos", f"El error encontrado fue: {err}")

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

    # validar que los campos tengan el formato correcto
    if(es_entero_valido(edad)) and es_decimal_valido(estatura) and es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos):
        ## Generar la cadena de caracteres
        datos = "Nombre: "+ nombres +"\n"+"Apellidos: "+ apellidos +"\n"+"Edad: "+ edad +" anos\n"+"Estatura: "+ estatura +"\n"+"Telefono: "+ telefono +"\n"+"Genero: " +genero
        ## Guardar los datos en el archivo TXT
        with open("D:/Users/Neko/Documents/Programacion_Avanzada/3MDatosAgosto2025Python.txt", "a") as archivo:
            archivo.write(datos+"\n\n")
            InsertarRegistros(nombres, apellidos, edad, estatura, telefono, genero)
        ## Mostrar mensaje de confirmacion
        messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+datos)
        
        #limpiar los controles despues de guardar
        limpiar_campos()
    else:
        messagebox.showerror("Error","Por favos, ingrese datos validos en los campos")

   

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))
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


