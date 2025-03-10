import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Raul Lionel
apellido: Prats Costa
división: J
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
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
        sueldo = float(self.txt_sueldo.get())
        incremento = float(self.txt_incremento.get())
        indice_de_actualizacion = 1 + (incremento / 100);
        sueldo_actualizado = sueldo * indice_de_actualizacion;
        # sueldo_actualizado = sueldo + ((sueldo * incremento) / 100)
        respuesta = 'Con el incremento del {0:.2f}%, en vigencia a partir del mes que viene, tu sueldo actual (${1:.2f}), pasará a ser de ${2:.2f}'.format(incremento, sueldo, sueldo_actualizado)
        alert(title= 'Solución', message= respuesta) 
        self.txt_sueldo.delete(0,10)
        self.txt_incremento.delete(0,10)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()