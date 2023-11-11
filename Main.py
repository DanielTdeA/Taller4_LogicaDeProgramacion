import random
from Ciclista import Ciclista
from Etapa import Etapa
from os import system
system("cls")

ciclistas_inscritos = []
ciclistas = []
etapas = []

def guardarInformacionCiclista(numero:int, nombre:str, edad:int, experiencia:int):
    informacion_ciclista = {}
    informacion_ciclista.update({"Numero":numero})
    informacion_ciclista.update({"Nombre":nombre})
    informacion_ciclista.update({"Edad":edad})
    informacion_ciclista.update({"Experiencia":experiencia})
    ciclistas_inscritos.append(informacion_ciclista)

def guardarInformacionEtapa(numero:int, nombre:str, kilometros:int):
    informacion_etapa = {}
    informacion_etapa.update({"Numero":numero})
    informacion_etapa.update({"Nombre":nombre})
    informacion_etapa.update({"Kilometros":kilometros})
    etapas.append(informacion_etapa)

numero_ciclistas = int(input("Ingrese la cantidad de ciclistas que van a participar: "))
numero = 1
while numero <= numero_ciclistas:
    system("cls")
    nombre = input(f"Ingresa el nombre del ciclista {numero}: ")
    edad = int(input(f"Ingresa la edad del ciclista {numero}: "))
    experiencia = 10

    if edad >= 18 and edad <= 20:
        experiencia += 3
    elif edad >= 21 and edad <= 25:
        experiencia += 4
    elif edad >= 26:
        experiencia += 5

    guardarInformacionCiclista(numero, nombre, edad, experiencia)
    numero += 1

for i in ciclistas_inscritos:
    ciclistas.append(Ciclista(i["Numero"], i["Nombre"], i["Edad"], i["Experiencia"]))

system("cls")

numero_etapas = int(input("Ingresa el numero de etapas a competir: "))

etapa = 1
while etapa <= numero_etapas:
    system("cls")
    nombre = input(f"Ingresa el nombre de la etapa {etapa}: ")
    kilometros = int(input(f"Ingresa la cantidad de kilometros de la etapa {etapa}: "))

    guardarInformacionEtapa(etapa, nombre, kilometros)
    etapa += 1

system("cls")

for _etapa in etapas:
    print(f"======== ETAPA NUMERO {_etapa['Numero']} ========")
    for _ciclista in ciclistas:
        etapa_actual = Etapa(_etapa["Nombre"], _etapa["Kilometros"])
        etapa_actual.correrEtapa(_ciclista)
    print(f"\n")