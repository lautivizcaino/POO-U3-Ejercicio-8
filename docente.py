from agente import Agente
class Docente(Agente):
    __carrera:str
    __cargo:str
    __catedra:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area='', tipo='') -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def __str__(self) -> str:
        return super().__str__() + 'Carrera:%s Cargo:%s Catedra:%s '%(self.__carrera,self.__cargo,self.__catedra)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d
    
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    
    def getSueldoDocente(self):
        if self.__cargo.upper()=='SIMPLE':
            cargo=self.getSueldoBasico()*0.1
        elif self.__cargo.upper()=='SEMIEXCLUSIVO':
            cargo=self.getSueldoBasico()*0.2
        elif self.__cargo.upper()=='EXCLUSIVO':
            cargo=self.getSueldoBasico()*0.5
        return super().getSueldo() + cargo
    
    def setCargo(self,cargo):
        self.__cargo=cargo.capitalize()