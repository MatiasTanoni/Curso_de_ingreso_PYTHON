'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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

        for _ in range(10):

            nombre = prompt("Nombre", "Ingrese su nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("Nombre", "Erro!,Ingrese su nombre")

            edad = prompt("edad","Ingrese edad, mayor de edad")
            while edad == None or not edad.isdigit() or int(edad) < 18:
                edad = prompt("Edad", "Error!, Ingrese su edad")
            edad = int(edad)    

            genero = prompt("genero", "Ingrese su genero (F-M-NB)") 
            while genero == None or not genero.isalpha() or genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("genero","Error!,Ingrese nuevamente su genero (F-M-NB)")

            tecnologia = prompt("tecnologia", "Ingrese su tecnologia (PYTHON - JS - ASP.NET)")
            while tecnologia == None or not tecnologia.isalpha() or tecnologia != "PYTHON" and tecnologia !="JS" and tecnologia !="ASP.NET":
                tecnologia = prompt("tecnologia", "Error!, Ingrese nuevamente su tecnologia (PYTHON - JS - ASP.NET)")

            puesto = prompt("puesto", "Ingrese su puesto (Jr - Ssr - Sr)")
            while puesto == None or not puesto.isalpha() or puesto !="Jr" and puesto!="Ssr" and puesto != "Sr":
                puesto = prompt("puesto", "Error!,Ingrese nuevamente su puesto (Jr - Ssr - Sr) ")

                

            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
