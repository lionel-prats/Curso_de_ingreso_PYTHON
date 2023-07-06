import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Raul Lionel
Apellido: Prats Costa
División: J

=== TP 1 (E/S) Ferrete Facturacion ===
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        # caja de texto producto #1
        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        # caja de texto producto #3
        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        # caja de texto producto #3
        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_sumar = customtkinter.CTkButton(master=self, text="SUMAR", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_precio_final = customtkinter.CTkButton(master=self, text="PRECIO FINAL", command=self.btn_precio_final_on_click)
        self.btn_precio_final.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        importe_1 = float(self.txt_importe_1.get())
        importe_2 = float(self.txt_importe_2.get())
        importe_3 = float(self.txt_importe_3.get())
        sumaPreciosProductos = importe_1 + importe_2 + importe_3
        message = f"La suma de los precios ingresados equivale a {sumaPreciosProductos:.2f}"
        alert(title= 'Mensaje', message= message) 

    def btn_promedio_on_click(self):
        importe_1 = float(self.txt_importe_1.get())
        importe_2 = float(self.txt_importe_2.get())
        importe_3 = float(self.txt_importe_3.get())
        promedioPreciosProductos = (importe_1 + importe_2 + importe_3) / 3
        message = f"El promedio de los precios ingresados equivale a : {promedioPreciosProductos:.2f}"
        alert(title= 'Mensaje', message= message) 

    def btn_precio_final_on_click(self):
        importe_1 = float(self.txt_importe_1.get())
        importe_2 = float(self.txt_importe_2.get())
        importe_3 = float(self.txt_importe_3.get())
        precioFinalConIVA = (importe_1 + importe_2 + importe_3) * 1.21
        message = f"El precio final incluyendo el IVA (21%) equivale a : {precioFinalConIVA:.2f}"
        alert(title= 'Mensaje', message= message) 
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()