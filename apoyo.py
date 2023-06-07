from agente import Agente
class Apoyo(Agente):
    __categoria:int
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, categoria, carrera='', cargo='', catedra='', area='', tipo='') -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoria=categoria
    def __str__(self) -> str:
        return super().__str__() + 'Categoria:%s'%self.__categoria
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                categoria=self.__categoria
            )
        )
        return d
    
    def getCategoria(self):
        return self.__categoria
    
    def getSueldo(self):
        if self.__categoria>=1 and self.__categoria<=10:
            categoria=self.getSueldoBasico()*0.1
        elif self.__categoria>=11 and self.__categoria<=20:
            categoria=self.getSueldoBasico()*0.2
        elif self.__categoria>=21 and self.__categoria<=22:
            categoria=self.getSueldoBasico()*0.3
        return super().getSueldo() + categoria
    

    def setCategoria(self,categoria):
        self.__categoria=categoria.capitalize()