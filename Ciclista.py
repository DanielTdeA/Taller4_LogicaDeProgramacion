from Persona import Persona

class Ciclista(Persona):
    def __init__(self, numero:int, nombre:str, edad:int, experiencia:int):
        super().__init__(nombre, edad)
        self._numero = numero
        self._experiencia = experiencia