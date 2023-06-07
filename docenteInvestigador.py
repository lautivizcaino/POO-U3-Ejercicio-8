from docente import Docente
from investigador import Investigador

class DocenteInvestigador(Investigador,Docente):    
    __categoriaPrograma:str
    __importe:float
    __investigacion:str
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo, categoriaPrograma, importe, investigacion) -> None:
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoriaPrograma=categoriaPrograma
        self.__importe=importe
        self.__investigacion=investigacion
    def __str__(self) -> str:
        return super().__str__() + 'Categoria en programa de incentivos:%s Importe extra:%s Investigación:%s'%(self.__categoriaPrograma,self.__importe,self.__investigacion)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.getCarrera(),
                cargo=self.getCargo(),
                catedra=self.getCatedra(),
                area=self.getArea(),
                tipo=self.getTipo(),
                categoriaPrograma=self.__categoriaPrograma,
                importe=self.__importe,
                investigacion=self.__investigacion
            )
        )
        return d
    
    def getCategoriaPrograma(self):
        return self.__categoriaPrograma
    def getImporte(self):
        return self.__importe
    def getInvestigacion(self):
        return self.__investigacion
    
    def getSueldo(self):
        return self.getSueldoDocente() + self.__importe
    
    def setImporte(self,importe):
        self.__importe=importe