import random

class Etapa:
    def __init__(self, nombre_etapa:str, distancia:int):
        self._nombre_etapa = nombre_etapa
        self._distancia = distancia

    def correrEtapa(self, ciclista):
        print(f"El ciclista {ciclista._nombre} inicia")

        numero_eventos = round(int(self._distancia) / 30)
        tiempo = (round(int(self._distancia) / 10)) * 60

        for e in range(numero_eventos):
            print(f"Parece que algo le esta pasando a el ciclista {ciclista._nombre}")
            if random.randint(1, 20) > ciclista._experiencia:
                evento = random.randint(1, 3)
                if evento == 1:
                    print(f"Que mala suerte el ciclista {ciclista._nombre} esta pasando por un terreno dificil!")
                    tiempo += 5
                elif evento == 2:
                    print(f"Que mala suerte el ciclista {ciclista._nombre} tuvo un pinchazo!")
                    tiempo += 10
                else:
                    print(f"Que mala suerte el ciclista {ciclista._nombre} tuvo una Caída!")
                    tiempo += 20
            else:
                print(f"Que suerte el ciclista {ciclista._nombre} salio ileso! ")

        print(f"Ciclista: {ciclista._nombre} \nTiempo de etapa {tiempo}\n")