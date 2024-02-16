import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:Agustin
apellido: Carabajal
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        
        tarifa_base = 15000
        descuento = 0
        aumento = 0

        estaciones = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()


        match (estaciones):
            case "Invierno":
                if destino == "Bariloche":
                    aumento = 20
                elif destino == "Cataratas" or destino == "Cordoba":
                    descuento = 10
                elif destino == "Mar del plata":
                    descuento = 20
        match (estaciones):
            case "Verano":
                if destino == "Bariloche":
                    descuento = 20
                elif destino == "Cataratas" or destino == "Cordoba":
                    aumento = 10
                elif destino == "Mar del plata":
                    aumento = 20
        match (estaciones):
            case "Primavera"|"Otoño":
                if destino == "Bariloche" or destino == "Cataratas" or destino == "Mar del plata":
                    aumento = 10
                elif destino == "Cordoba":
                    aumento = 0

        if descuento >= 10:
            descuento_a_realizar = tarifa_base * descuento / 100
            tarifa_con_descuento = tarifa_base - descuento_a_realizar
            mensaje = f"De acuerdo al destino {destino} y la estacion del año {estaciones} se aplico un descuento del {descuento}%. y su tarifa total es ${tarifa_con_descuento}"
        elif aumento >=10:
            aumento_a_realizar = tarifa_base * aumento / 100
            tarifa_con_aumento = tarifa_base + aumento_a_realizar
            mensaje = f"De acuerdo al destino {destino} y la estacion del año {estaciones} se aplico un aumento del {aumento}%. y su tarifa total es ${tarifa_con_aumento}"
        elif aumento == 0:
            mensaje = f"La tarifa total es {tarifa_base}"
        
        alert ("UTN", mensaje)  
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()