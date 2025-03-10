import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Raul Lionel 
Apellido: Prats Costa
División: J

=== TP 2 (E/S) Ferrete Pinturas ===
Enunciado:
Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados
        Formula: (0 °F - 32) * 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        Formula: (0 °C * 9/5) + 32 = 32 °F
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)
       
        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=3, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):
        
        if self.txt_temperatura_c.get() == "":
            mensaje = "Debes ingresar un valor en °C para poder calcular el equivalente en °F"
        else:
            temperatura_c = float(self.txt_temperatura_c.get())
            equivalenteFahrenheit = (temperatura_c * 9/5) + 32
            mensaje = f"{temperatura_c} °C equivalen a {equivalenteFahrenheit} °F"

        alert(title = 'Mensaje', message = mensaje) 
        self.txt_temperatura_c.delete(0,100)
        self.txt_temperatura_f.delete(0,100)

    def btn_convertir_f_c_on_click(self):
        if self.txt_temperatura_f.get() == "":
            mensaje = "Debes ingresar un valor en °F para poder calcular el equivalente en °C"
        else:
            temperatura_f = float(self.txt_temperatura_f.get())
            equivalenteCelcius = (temperatura_f - 32) * 5/9
            mensaje = f"{temperatura_f} °F equivalen a {equivalenteCelcius} °C"

        alert(title = 'Mensaje', message = mensaje) 
        self.txt_temperatura_c.delete(0,100)
        self.txt_temperatura_f.delete(0,100)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()