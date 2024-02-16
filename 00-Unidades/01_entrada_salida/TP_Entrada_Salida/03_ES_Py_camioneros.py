import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: ES_Camioneros
---
Enunciado:

3.	Para el departamento de logística:

	A.	Es necesario saber la cantidad camiones que harian falta para transportar los 
    materiales que se utilizarán para la construcción de un edificio.
    Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar. 
    El programa deberá informar la cantidad de camiones, sabiendo que cada uno de ellos puede 
    transportar por viaje 3500kg

    B.	A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones 
    para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo 
    (en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir a una
    velocidad máxima y constante de 90 km/h  

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Toneladas")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_toneladas = customtkinter.CTkEntry(master=self)
        self.txt_toneladas.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Kilómetros")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_kilometros = customtkinter.CTkEntry(master=self)
        self.txt_kilometros.grid(row=1, column=1)
       
        self.btn_cantidad_camiones = customtkinter.CTkButton(master=self, text="Calcular cantidad de camiones", command=self.btn_cantidad_camiones_on_click)
        self.btn_cantidad_camiones.grid(row=3, pady=10, padx=30 ,columnspan=2, sticky="nsew")
        
        self.btn_tiempo_llegada = customtkinter.CTkButton(master=self, text="Calcular tiempo de llegada", command=self.btn_tiempo_llegada_on_click)
        self.btn_tiempo_llegada.grid(row=4, pady=10, padx=30, columnspan=2, sticky="nsew")
    
    def btn_cantidad_camiones_on_click(self):

        cantidad_toneladas_txt = self.txt_toneladas.get()
        cantidad_toneladas_float = float(cantidad_toneladas_txt)

        cantidad_kg = cantidad_toneladas_float * 1000
        camion_carga = 3500
        cantidad_camiones = cantidad_kg / camion_carga

        cantidad_camiones_entero = int(cantidad_camiones)

        mensaje = "La cantidad de camiones necesaria para transportar {0} kg es : {1} camiones ".format (cantidad_camiones, cantidad_camiones_entero) 
        alert(title= "Camiones", message= mensaje)

    def btn_tiempo_llegada_on_click(self):
        
        cant_kilometros_txt = self.txt_kilometros.get()
        cant_kilometros_float = float(cant_kilometros_txt)

        vel_camion = 90
        tiempo_llegada = cant_kilometros_float / vel_camion
        tiempo_llegada_entero = int(tiempo_llegada)
        mensaje = "El tiempo que tarda el camion hasta la obra es {0} hs ".format (tiempo_llegada_entero) 
        alert(title= "Tiempo de llegada", message= mensaje)






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()