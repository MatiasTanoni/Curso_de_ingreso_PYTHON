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
        postulantes_NB = 0
        jr_menor_edad = 0
        nombre_jr_menor_edad = 0
        contador_F = 0
        acumulador_f = 0
        contador_m = 0
        acumulador_m = 0
        contador_nb = 0
        acumulador_nb = 0
        contador_js = 0
        contador_python = 0
        contador_aspnet = 0
        tecnologia_mas_postulantes = 0

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

            tecnologia = prompt("tecnologia", "Ingrese su tecnologia (PYTHON - JS - ASP NET)")
            while tecnologia == None or not tecnologia.isalpha() or tecnologia != "PYTHON" and tecnologia !=  "JS" and tecnologia != "ASP NET" :
                tecnologia = prompt("tecnologia", "Error!, Ingrese nuevamente su tecnologia (PYTHON - JS - ASP NET)")

            puesto = prompt("puesto", "Ingrese su puesto (Jr - Ssr - Sr)")
            while puesto == None or not puesto.isalpha() or puesto !="Jr" and puesto!="Ssr" and puesto != "Sr":
                puesto = prompt("puesto", "Error!,Ingrese nuevamente su puesto (Jr - Ssr - Sr) ")

            #A
            if genero == "NB" and tecnologia == "ASP NET" or tecnologia == "JS":
                if edad >= 25 or edad <= 40 and puesto == "Ssr":        
                    postulantes_NB += 1
            #B
            if puesto == "Jr":
                if jr_menor_edad == 0:
                    jr_menor_edad = edad
                    nombre_jr_menor_edad = nombre
                if edad < jr_menor_edad:
                    jr_menor_edad = edad
                    nombre_jr_menor_edad = nombre
            #C
            if genero == "F":
                contador_F += 1
                acumulador_f += edad
                promedio_f = acumulador_f / contador_F
            else: 
                promedio_f = 0
                   
            if genero == "M":
                contador_m += 1
                acumulador_m += edad 
                promedio_m = acumulador_m / contador_m
            else:
                promedio_m = 0

            if genero == "NB":
                contador_nb += 1
                acumulador_nb += edad    
                promedio_nb = acumulador_nb / contador_nb
            else:
                promedio_nb = 0  
            #D
            if tecnologia == "PYTHON":
                contador_python += 1
            if tecnologia == "JS":
                contador_js += 1
            if tecnologia == "ASP NET":
                contador_aspnet += 1

            if contador_python > contador_js and contador_python > contador_aspnet:
                tecnologia_mas_postulantes = "Python es la que mas postulantes tiene"
            if contador_js > contador_python and contador_js >contador_aspnet:
                tecnologia_mas_postulantes = "JS es la que mas postulantes tiene"
            else:
                tecnologia_mas_postulantes = "ASP NET es la tecnologia que mas tiene" 
            #E
            porcentaje_f = (contador_F * 100) / 10
            porcentaje_m = (contador_m * 100) / 10
            porcentaje_nb = (contador_nb * 10)  / 10        

            
                    

        alert(title = "tp07", message = f"Cantidad de postulantes NB: {postulantes_NB}")   
        alert(title = "TP07", message = f"Nombre del postulante Jr con menor edad: {nombre_jr_menor_edad}")
        alert(title = "TP07", message = f"Promedio de edades femenino:{promedio_f} , masculino {promedio_m}, no binario {promedio_nb}") 
        alert(title = "TP07", message = f"Tecnologia con mas postulantes: {tecnologia_mas_postulantes}")
        alert(title = "TP07", message = f"Porcentaje de postulantes de femeninos:{porcentaje_f}, masculinos {porcentaje_m}, no binarios {porcentaje_nb}")     
        alert(title = "TP07", message= f"""\nEl porcentaje por genero de los postulantes es: 
        \nMasculino: {porcentaje_m}%
        \nFemenino: {porcentaje_f}% 
        \nNo Binario: {porcentaje_nb}%
        """)

    
     
                

            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
