import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        suma = 0

        for numero in self.lista_datos:
            suma = suma + numero

        cantidad_elementos_en_lista = len(self.lista_datos) 

        if cantidad_elementos_en_lista != 0:   
            promedio = suma / cantidad_elementos_en_lista
            alert("ej06_lista", f"El promedio de los valores es: {promedio}")    
        else:
            alert("ej06_lista", f"La lista esta vacia")    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()