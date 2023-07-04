import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están al mismo precio $800 pesos final 
    A. Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%.

    B. Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40% y si es de otra marca el descuento es del 30%.

    C. Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o "FelipeLamparas" se hace un descuento del 25% y si es de otra marca el descuento es del 20%.

    D. Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es "FelipeLamparas" se hace un descuento del 10% y si es de otra marca un 5%.

    E. Si el importe final con descuento suma más de $4000 se obtiene un descuento adicional del 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas", "JeLuz", "MazIluminacion"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):

        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())

        PRECIO = 800
        total_con_descuento = 0

        total_sin_descuentos = PRECIO * cantidad

        message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}.".format(cantidad, marca, total_sin_descuentos)
        
        if cantidad >= 6:
            total_con_descuento = total_sin_descuentos * .5
            message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                total_con_descuento = total_sin_descuentos * .6
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
            else: 
                total_con_descuento = total_sin_descuentos * .7
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                total_con_descuento = total_sin_descuentos * .75
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
            else: 
                total_con_descuento = total_sin_descuentos * .8
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                total_con_descuento = total_sin_descuentos * .85
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
            elif marca == "FelipeLamparas":
                total_con_descuento = total_sin_descuentos * .90
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)
            else: 
                total_con_descuento = total_sin_descuentos * .95
                message = "Cantidad: {0}. \nMarca: {1}. \nTotal sin descuento: ARS {2}. \nTotal con descuento por cantidad y marca: ARS {3}".format(cantidad, marca, total_sin_descuentos, total_con_descuento)

        if total_con_descuento > 4000:
            total_con_descuento_adicional = total_con_descuento * .95
            message += "\nTotal con descuento adicional: ARS {0}".format(total_con_descuento_adicional)

        alert(title= 'Respuesta', message= message) 

if __name__ == "__main__":
    app = App()
    app.mainloop()