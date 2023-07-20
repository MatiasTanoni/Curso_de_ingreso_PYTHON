import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_suma_negativos = 0
        acumulador_suma_positivos = 0
        contador_negativo = 0
        contador_positivos = 0
        contador_ceros = 0
        numero_ingresado = ""
        diferencia = 0

        while numero_ingresado != None:
            numero_ingresado = prompt("ej10while", "Ingrese un numero")  

            if numero_ingresado != None:
                numero_ingresado = int(numero_ingresado)

                if numero_ingresado < 0:
                    acumulador_suma_negativos = acumulador_suma_negativos + numero_ingresado
                    contador_negativo = contador_negativo + 1
                elif numero_ingresado > 0:
                    acumulador_suma_positivos = acumulador_suma_positivos + numero_ingresado
                    contador_positivos = contador_positivos + 1
                else:
                    contador_ceros = contador_ceros + 1
            
            diferencia = contador_positivos - contador_negativo

        mensaje = f"Suma acumulada de los negativos es: {acumulador_suma_negativos}   "
        mensaje += f"La duma acumulada de los positivos {acumulador_suma_positivos}"
        mensaje += f"Cantidad de numeros positivos ingresados"
        mensaje += f"Cantidad de numeros negativos ingresados"
        mensaje += f"Cantidad de ceros"
        mensaje += f"Diferencia entre la cantidad de los números positivos ingresados y los negativos"

        alert("ej10while", message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
