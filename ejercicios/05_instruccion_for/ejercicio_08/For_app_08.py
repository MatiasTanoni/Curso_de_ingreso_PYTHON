import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("for-ej08","ingrese un numero")
        while numero_ingresado == None or not numero_ingresado.isdigit():
            numero_ingresado = prompt("for-ej06", "Ingrese un numero devuelta")

        numero_ingresado = int(numero_ingresado)
        contador = 0
        lista_numeros = range(1,numero_ingresado+1)

        for numero in lista_numeros:
            if numero_ingresado % numero == 0:
                contador = contador + 1

        if contador == 2:
            alert("Primo", "El numero ingresado es primo")
        else:
            alert("NO primo", "El numero ingresado no es primo")            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()