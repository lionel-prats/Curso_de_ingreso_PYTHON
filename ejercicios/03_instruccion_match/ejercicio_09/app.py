import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Raul Lionel 
apellido: Prats Costa 
division: J
--------------------
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
        pass
        tarifa_base = 15000
        destino_seleccionado = self.combobox_destino.get()
        estacion_seleccionada = self.combobox_estaciones.get()
        message= f'''
        Destino seleccionado: {destino_seleccionado}.
        Estación seleccionada: {estacion_seleccionada}.
        Tarifa base: ${tarifa_base}.
        '''
        match estacion_seleccionada:
            case "Otoño" | "Primavera":
                match destino_seleccionado:
                    case "Cordoba":
                        message+= "Ajuste por temporada: -."
                        message+= f"\nTotal a pagar: ${tarifa_base}."
                    case _:
                        message+= "Ajuste por temporada: +10%."
                        message+= f"\nTotal a pagar: ${tarifa_base * 1.1}."
            case "Invierno":
                match destino_seleccionado:
                    case "Bariloche":
                        message+= "Ajuste por temporada: +20%."
                        message+= f"\nTotal a pagar: ${tarifa_base * 1.2}."
                    case "Mar del plata":
                        message+= "Ajuste por temporada: -20%."
                        message+= f"\nTotal a pagar: ${tarifa_base * .8}."
                    case _:
                        message+= "Ajuste por temporada: -10%."
                        message+= f"\nTotal a pagar: ${tarifa_base * .9}."
            case _:
                match destino_seleccionado:
                    case "Bariloche":
                        message+= "Ajuste por temporada: -20%."
                        message+= f"\nTotal a pagar: ${tarifa_base * .8}."
                    case "Mar del plata":
                        message+= "Ajuste por temporada: +20%."
                        message+= f"\nTotal a pagar: ${tarifa_base * 1.2}."
                    case _:
                        message+= "Ajuste por temporada: +10%."
                        message+= f"\nTotal a pagar: ${tarifa_base * 1.1}."

        alert(title= "Mensaje", message= message)
            
    
if __name__ == "__main__":
    app = App()
    app.mainloop()