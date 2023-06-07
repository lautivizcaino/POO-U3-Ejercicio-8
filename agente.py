
class Agente:
    __cuil:str
    __apellido:str
    __nombre:str
    __sueldo:float
    __antiguedad:int
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carrera='',cargo='',catedra='',area='',tipo='') -> None:
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldo=sueldo
        self.__antiguedad=antiguedad
    def __str__(self) -> str:
        return 'CUIL:%s Apellido:%s Nombre:%s Sueldo:%s Antiguedad:%s '%(self.__cuil,self.__apellido,self.__nombre,self.__sueldo,self.__antiguedad)
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.__cuil,
                apellido=self.__apellido,
                nombre=self.__nombre,
                sueldo=self.__sueldo,
                antiguedad=self.__antiguedad
            )
        )
        return d
    
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBasico(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__antiguedad
    
    def getSueldo(self):
        return self.__sueldo+self.__sueldo*self.__antiguedad*0.01
    
    def setBasico(self,basico):
        self.__sueldo=basico
    