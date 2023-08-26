#------Listas-----------#
"""
comida = ["Nachos","Tacos","Hot Dog","Hamburgesa"]
print(comida)
print(type(comida))
"""

#-------Tuplas-----------#
"""
Semana=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

for x in Semana:
    print(x)

print(type(Semana))
"""

#--------Diccionario-----#
"""
Alumnos={
2054603: "Danyelin",
2022069: "Edwin",
1843610: "Zahid",
1817307: "Eric",
1966947: "Damian"
}

for x,j  in Alumnos.items():
    print("Matricula: ",x," Nombre: ",j)
print(type(Alumnos))
"""


#-----Conjuntos-----#
"""
Material = {"Madera","Piedra","Hierro","Oro","Diamante"}
for x  in Material:
    print([x])
print(type(Material))
"""

#------Ejercicio1--------#
"""
import re
while True:
    _edad = (input("Cual es tu edad?: "))
    if _edad =="":
         print("Error debes de ingresar tu edad para continuar. Intenta de nuevo")
         continue
    r_edad=r"^([0-9]{1,3})$"
    if not(re.match(r_edad,_edad)):
        print("Error, Dato no permitido, intenta de nuevo")
        continue
    edad = int(_edad)
    if edad >= 18:
            print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    break
"""