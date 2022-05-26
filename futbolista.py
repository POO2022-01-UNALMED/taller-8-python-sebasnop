from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        
        this._golesMarcados = golesMarcados
        this._tarjetasRojas = tarjetasRojas
        this._piernaHabil = piernaHabil
        
        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getGolesMarcados(self):
        return self._golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def getPiernaHabil(self):
        return self._piernaHabil

    def __str__(self):
        return "Mi nombre es " + self._getNombre() + " soy profesional en el deporte " + self._deporte + " Tengo " + self._edad + " años de edad y llevo " + self._añosPracticando + " años en el deporte"