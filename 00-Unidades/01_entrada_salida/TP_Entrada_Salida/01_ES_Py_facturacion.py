import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: AGUSTIN
apellido: CARABAJAL
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        #Enunciado:
        #Para el departamento de facturación:
        #A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
        #B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	    #C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

    def btn_total_on_click(self):

        producto_1_txt = self.txt_importe_1.get()
        producto_1_float = float(producto_1_txt)
        

        producto_2_txt = self.txt_importe_2.get()
        producto_2_float = float(producto_2_txt)

        producto_3_txt = self.txt_importe_3.get()
        producto_3_float = float(producto_3_txt)

        resultado_suma_float = producto_1_float + producto_2_float + producto_3_float
        resultado_suma_txt = str (resultado_suma_float)

        mensaje = "El precio total es de: " + resultado_suma_txt
        alert(title= "total", message= mensaje)


    def btn_promedio_on_click(self):
        
        producto_1_txt = self.txt_importe_1.get()
        producto_1_float = float(producto_1_txt)

        producto_2_txt = self.txt_importe_2.get()
        producto_2_float = float(producto_2_txt)

        producto_3_txt = self.txt_importe_3.get()
        producto_3_float = float(producto_3_txt)

        resultado_suma_float = producto_1_float + producto_2_float + producto_3_float
        resultado_suma_txt = str (resultado_suma_float)

        promedio = 3
        resultado_promedio_float = resultado_suma_float / promedio
        resultado_promedio_txt = str(resultado_promedio_float)

        mensaje = "El total de los productos es: {0} " "\nEl promedio del total es: {1} ".format(resultado_suma_txt,resultado_promedio_txt)
        alert(title= "Promedio", message= mensaje)


    def btn_total_iva_on_click(self):
        
        producto_1_txt = self.txt_importe_1.get()
        producto_1_float = float(producto_1_txt)

        producto_2_txt = self.txt_importe_2.get()
        producto_2_float = float(producto_2_txt)

        producto_3_txt = self.txt_importe_3.get()
        producto_3_float = float(producto_3_txt)

        resultado_suma_float = producto_1_float + producto_2_float + producto_3_float
        resultado_suma_txt = str (resultado_suma_float)

        iva_float = 21
        incemento_iva = resultado_suma_float * iva_float /100
        total_con_iva = resultado_suma_float + incemento_iva

        mensaje = "El precio total es de: {0} " "\n+ IVA 21%" "\nEl precio final es: {1}".format(resultado_suma_txt,total_con_iva) 
        alert(title= "total con IVA", message= mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()