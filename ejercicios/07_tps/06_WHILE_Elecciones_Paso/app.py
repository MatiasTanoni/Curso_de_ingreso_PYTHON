'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):     
        maximo_votos = 0
        minimo_votos = None
        candidato_maximo_votos = ""
        candidato_minimo_votos = ""
        total_votos = 0
        total_edades= 0
        candidatos= 0
        edad_menos_votado = 0
        
        while True:

            nombre = prompt("nombres", "ingrese los nombres")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("nombres", "Error!, Ingrese nuevamente los nombres")

            edad = prompt("edad", "ingrese las edades, mayores a 25 años")
            while edad == None or not edad.isdigit() or int(edad) <25:
                edad = prompt("edad", "Error!, Ingrese nuevamente las edades")
            edad = int(edad)
            total_edades += edad

                    
            votos = prompt("votos", "ingrese los votos")
            while votos == None or not votos.isdigit() or votos <= 0:
                votos = prompt("votos", "Error!, Ingrese nuevamente los votos")
            
               
            total_votos = total_votos + votos

           
            if maximo_votos == 0 and minimo_votos == 0:
                maximo_votos = votos
                minimo_votos = votos
            if votos >= maximo_votos:
                candidato_maximo_votos = nombre
                maximo_votos = votos
            elif votos <= minimo_votos:
                candidato_minimo_votos = nombre
                edad_menos_votado = edad
                minimo_votos = votos

            candidatos += 1            
 
            continuar = question("Titulo", "¿Desea continuar?")
            if not continuar:
                break

        promedio_edades = total_edades / candidatos    

        print("TP06", f"El candidato con mas votos es {candidato_maximo_votos}, el candidato con menos votos es {candidato_minimo_votos} y tiene {edad_menos_votado} votos, El promedio de de las edades de los candidatos es: {promedio_edades}, El total de votos emitidos es:{total_votos}")    
               

                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
