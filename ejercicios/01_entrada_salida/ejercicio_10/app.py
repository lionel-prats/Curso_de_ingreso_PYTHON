import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Raul Lionel
apellido: Prats Costa
division: J
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        importe = float(self.txt_importe.get())
        descuento = float(self.txt_descuento.get())
        indice_de_actualizacion = 1 - (descuento / 100)
        importe_actualizado = importe * indice_de_actualizacion
        respuesta = 'Con el descuento del {0:.2f}%, el importe original de ${1:.2f}, pasa a ser de ${2:.2f}'.format(descuento, importe, importe_actualizado)
        alert(title= 'Solución', message= respuesta) 
        self.txt_importe.delete(0,10)
        self.txt_descuento.delete(0,10)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()