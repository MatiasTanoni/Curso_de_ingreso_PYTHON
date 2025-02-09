import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):

        numero_ingresado = ""

        while numero_ingresado != None:
            numero_ingresado = prompt("Numero", "Ingrese un numero")
            
            if numero_ingresado == None:
                break

            if numero_ingresado == "" or numero_ingresado.isalpha():
                continue
            
            numero_ingresado = int(numero_ingresado)

            self.lista.append(numero_ingresado)


    def btn_mostrar_estadisticas_on_click(self):
        #a. La suma acumulada de los negativos

        acumulador_negativos = 0
        
        for numero in self.lista:
            if numero < 0:
                acumulador_negativos += numero
        alert("acumulador de negativos", f"acumulador de negativos: {acumulador_negativos}")  
        #b La suma acumulada de los positivos
        acumulador_positivos = 0
        
        for numero in self.lista:
            if numero > 0:
                acumulador_positivos += numero
        alert("acumulador de positivos", f"acumulador de positivos: {acumulador_positivos}")        
        #c. Cantidad de números positivos ingresados
        contador_positivos = 0
        for numero in self.lista:
            if numero > 0:
                contador_positivos += 1
        alert("contador positivos", f"La cantidad de numeros positivos son:{contador_positivos}")
        #d. Cantidad de números negativos ingresados
        contador_negativos = 0
        for numero in self.lista:
            if numero < 0:
                contador_negativos += 1
        alert("contador negativos", f"La cantidad de numeros negativos son:{contador_negativos}")        
        #e. Cantidad de ceros
        contador_ceros = 0
        for numero in self.lista:
            if numero == 0:
                contador_ceros += 1
        alert("contador ceros", f"La cantidad de numeros que son ceros son: {contador_ceros}")        
        #f. El minimo de los negativos
        minimo_negativo = 0
        for numero in self.lista:
            if numero < 0:
                minimo_negativo = numero
                if numero < minimo_negativo:
                    minimo_negativo = numero
        alert("mininimo negativos", f"el minimo de los negativos es: {minimo_negativo}")
        #g. El maximo de los positivos
        maximo_positivo = 0
        for numero in self.lista:
            if numero > 0:
                maximo_positivo = numero
                if numero > maximo_positivo:
                    maximo_positivo = numero
        alert("maximos positivos", f"el minimo de los negativos es: {maximo_positivo}")
        #h. El promedio de los negativos
        acumulador_negativos = 0
        contador_negativos = 0
        for numero in self.lista:
            if numero <0:
                contador_negativos += 1
                acumulador_negativos += numero
        promedio = acumulador_negativos / contador_negativos
        alert("promedio", f"el promedio de los negativos es: {promedio}")        
   

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
