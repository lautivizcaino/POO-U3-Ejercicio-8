from agente import Agente
class Investigador(Agente):
    __area:str
    __tipo:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera='', cargo='', catedra='',area='', tipo='') -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__area=area
        self.__tipo=tipo
    def __str__(self) -> str:
        return super().__str__() + 'Area de investigacion:%s Tipo de investigacion:%s '%(self.__area,self.__tipo)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                area=self.__area,
                tipo=self.__tipo
            )
        )
        return d
    
    def getArea(self):
        return self.__area
    
    def getTipo(self):
        return self.__tipo