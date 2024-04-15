#Objetivo del programa
#/Interactuar con diferentes Bots de de Discord Propios

#Importar elementos de trabajo.
from tkinter import *
import tkinter as tk
from PIL import ImageTk, ImageColor, ImageDraw
import os

#-------------------------------------------------------------------------------------------
#Insertar elementos de conexion versatil con la carpeta principal.
carpeta_principal = os.path.dirname(__file__)
print(carpeta_principal)
carpeta_imagenes = os.path.join(carpeta_principal, "Imagen_Python_PNG")
#-------------------------------------------------------------------------------------------
#Crear elementos principales de la ventana de trabajo.
ventana_principal = tk.Tk()
ventana_principal.iconbitmap(os.path.join(carpeta_imagenes, "Logo_EnDesarrollo.ico"))
ventana_principal.geometry ("300x200")
ventana_principal.title ("Ventana.Trabajo.BOT_DISCORD")
ventana_principal.resizable(0,0)
#-------------------------------------------------------------------------------------------
#Definir funciones.
def OffWindow():
    ventana_principal.destroy()






boton_cerrar_ventana = Button(text= "Cerrar ventana", command= OffWindow, fg= "purple")
boton_cerrar_ventana.place(x= 0, y= 0)


#-------------------------------------------------------------------------------------------
#Insertar Imagenes
#imagen_bot_desarrollo_discord = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "Bot_Discord_Desarrollo.png")).resize(100, 20))
#imagen_bot_desarrollo_discord.pack()
ventana_principal.mainloop()