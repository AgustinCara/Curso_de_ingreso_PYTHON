import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: AGUSTIN
apellido: CARABAJAL
---
Ejercicio: entrada_salida_09bis
---
Enunciado:
Al presionar el botón 'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        txt_sueldo = self.txt_sueldo.get()
        sueldo_float = float (txt_sueldo)
        sueldo_act = sueldo_float

        txt_incremento = self.txt_incremento.get()
        incremento_float = float(txt_incremento)
     
        incremento_pesos = sueldo_float * incremento_float /100
        nuevo_sueldo = sueldo_float + incremento_pesos

        mensaje = "Sueldo actual: {0},  Sueldo actualizado con incremento: {1}".format (sueldo_float,nuevo_sueldo) 
        alert(title= "Resultado", message= mensaje)

        #mensaje = "Tu sueldo actualizado es: {0}".format (nuevo_sueldo) 
        #alert(title= "Resultado", message= mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()