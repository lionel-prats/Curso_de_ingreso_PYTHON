import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
nombre: Raul Lionel
apellido: Prats Costa
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA") # esta linea de codigo le pone titulo a la ventana principal
       
        self.btn_mostrar = customtkinter.CTkButton( master = self, text = "Mostrar", command = self.btn_mostrar_on_click ) # declaro un boton
        self.btn_mostrar.grid( row = 2, pady = 20, columnspan = 2, sticky = "nsew" ) # posiciono el boton en pantalla (nsew == north south east west)

    def btn_mostrar_on_click(self):
        nombre = prompt(
            title = 'entrada_salida - ejercicio_02',
            prompt = "Ingrese un dato",
        )
        alert( title = 'INFO', message = nombre )
        
if __name__ == "__main__":
    app = App()
    app.mainloop()