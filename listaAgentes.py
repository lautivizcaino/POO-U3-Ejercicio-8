from zope.interface import implementer
from agente import Agente
from interfaces import Interfaz
from interfacesAdministradores import ITesorero,IDirector
from nodo import Nodo
from apoyo import Apoyo
from docente import Docente
from investigador import Investigador
from docenteInvestigador import DocenteInvestigador
@implementer(Interfaz)
@implementer(ITesorero)
@implementer(IDirector)
class ListaAgentes:
    __comienzo:None
    __cantidad:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__cantidad=0
    
    def toJSON(self): 
        d = dict(
            __class__=self.__class__.__name__,
            agentes=[] 
            ) 
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            d['agentes'].append(agente.toJSON())
            aux=aux.getSiguiente()
        return d

    def agregarAgente(self,agente):
        nodo=Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__cantidad+=1
    def mostrarLista(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getAgente())
            aux=aux.getSiguiente()
    
    def crearElemento(self):
        tipoAgente=int(input('Ingrese tipo de agente (1-Apoyo/2-Docente/3-Investigador/4-Docente Investigador): '))
        cuil=input('Ingrese CUIL: ')
        apellido=input('Ingrese Apellido: ')
        nombre=input('Ingrese Nombre: ')
        sueldo=float(input('Ingrese sueldo: '))
        antiguedad=int(input('Ingrese antiguedad: '))
        if tipoAgente==1:
            categoria=int(input('Ingrese categoria: '))
            apoyo=Apoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
            nodo=Nodo(apoyo)
        elif tipoAgente==2:
            carrera=input('Ingrese carrera: ')
            cargo=input('Ingrese cargo: ')
            catedra=input('Ingrese catedra: ')
            docente=Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
            nodo=Nodo(docente)
        elif tipoAgente==3:
            area=input('Ingrese area: ')
            tipo=input('Ingrese tipo: ')
            investigador=Investigador(cuil,apellido,nombre,sueldo,antiguedad,'','','',area,tipo)
            nodo=Nodo(investigador)
        elif tipoAgente==4:
            carrera=input('Ingrese carrera: ')
            cargo=input('Ingrese cargo: ')
            catedra=input('Ingrese catedra: ')
            area=input('Ingrese area: ')
            tipo=input('Ingrese tipo: ')
            categoriaPrograma=input('Ingrese categoria de programa: ')
            importe=float(input('Ingrese importe: '))
            investigacion=input('Ingrese investigacion: ')
            docenteInvestigador=DocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo, categoriaPrograma, importe, investigacion)
            nodo=Nodo(docenteInvestigador)
        return nodo

    def insertarAgente(self):
        posicion=int(input('Ingrese la posicion de la coleccion: '))-1
        if posicion>=0 and posicion<=self.__cantidad:
            nodo=self.crearElemento()
            if nodo!=None:
                contador=0
                if posicion==0:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__cantidad+=1
                else:
                    post=self.__comienzo
                    ant=self.__comienzo
                    while post!=None and posicion>contador:
                        ant=post
                        post=post.getSiguiente()
                        contador+=1
                    if posicion==contador:
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(post)
                        self.__cantidad+=1
    def agregarAgenteFinal(self):
        nodo=self.crearElemento()
        if nodo!=None:
            if self.__comienzo==None:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__cantidad+=1
            else:
                post=self.__comienzo
                while post!=None:
                    ant=post
                    post=post.getSiguiente()
                ant.setSiguiente(nodo)
                self.__cantidad+=1
    def mostrarAgente(self):
        posicion=int(input('Ingrese la posicion de la coleccion: '))-1
        if posicion>=0 and posicion<=self.__cantidad:
            contador=0
            if posicion==0:
                print(self.__comienzo.getAgente())
            else:
                aux=self.__comienzo
                while aux!=None and posicion>contador:
                    aux=aux.getSiguiente()
                    contador+=1
                if posicion==contador:
                    print(aux.getAgente())
                    self.__cantidad+=1

    def generarListadoOrdenado(self):
        carrera=input('Ingrese carrera: ')
        tope=None
        ultima=None
        while ultima!=self.__comienzo:
            ultima=self.__comienzo
            act=self.__comienzo
            while act.getSiguiente()!=tope:
                agente=act.getAgente()
                pos=act.getSiguiente()
                agenteSig=pos.getAgente()
                if agente.getNombre().upper()>agenteSig.getNombre().upper():
                    aux=pos.getAgente()
                    pos.setAgente(agente)
                    act.setAgente(aux)
                    ultima=act
                act=pos
            tope=ultima.getSiguiente()
        
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            if isinstance(agente,DocenteInvestigador):
                carreraIns=agente.getCarrera()
                if carreraIns.upper()==carrera.upper():
                    print(agente)
            aux=aux.getSiguiente()

    def contarAgentes(self):
        area=input('Ingrese area: ')
        aux=self.__comienzo
        cDocentesInv=0
        cInvestigadores=0
        while aux!=None:
            agente=aux.getAgente()
            if isinstance(agente,DocenteInvestigador):
                areainst=agente.getArea()
                if areainst.upper()==area.upper():
                    cDocentesInv+=1
            elif isinstance(agente,Investigador):
                areainst=agente.getArea()
                if areainst.upper()==area.upper():
                    cInvestigadores+=1
            aux=aux.getSiguiente()
        print('Area:%s\nCantidad de Investigadores:%d\nCantidad de Docentes Investigadores:%d'%(area,cInvestigadores,cDocentesInv))

    def generarColeccionOrdenada(self):
        tope=None
        ultima=None
        while ultima!=self.__comienzo:
            ultima=self.__comienzo
            act=self.__comienzo
            while act.getSiguiente()!=tope:
                agente=act.getAgente()
                pos=act.getSiguiente()
                agenteSig=pos.getAgente()
                if agente.getApellido().upper()>agenteSig.getApellido().upper():
                    aux=pos.getAgente()
                    pos.setAgente(agente)
                    act.setAgente(aux)
                    ultima=act
                act=pos
            tope=ultima.getSiguiente()

        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            if isinstance(agente,DocenteInvestigador):
                tipo='Docente Investigador'
                sueldo=agente.getSueldo()
            elif isinstance(agente,Apoyo):
                tipo='Apoyo'
                sueldo=agente.getSueldo()
            elif isinstance(agente,Investigador):
                tipo='Investigador'
                sueldo=agente.getSueldo()
            elif isinstance(agente,Docente):
                tipo='Docente'
                sueldo=agente.getSueldoDocente()
            
            print('Nombre:%s Apellido:%s Tipo de Agente:%s Sueldo:%.2f'%(agente.getNombre(),agente.getApellido(),tipo,sueldo))
            aux=aux.getSiguiente()

    def mostrarTotal(self):
        categoria=input('Ingrese una categoria: ')
        aux=self.__comienzo
        tot=0.0
        while aux!=None:
            agente=aux.getAgente()
            if isinstance(agente,DocenteInvestigador):
                print('Apellido:%s Nombre:%s Importe extra:%.2f'%(agente.getApellido(),agente.getNombre(),agente.getImporte()))
                tot+=agente.getImporte()
            aux=aux.getSiguiente()
        print('TOTAL DE DINERO:%.2f'%tot)

    def guardarAgentes(self,jsonF):
        d=self.toJSON()
        jsonF.guardarJSONArchivo(d,'personal.json')
        print('\nArchivo guardado con éxito')

    def gastosSueldoPorEmpleado(self,dni):
        aux=self.__comienzo
        encontrado=False
        while aux!=None and not encontrado:
            agente=aux.getAgente()
            Cuil=agente.getCuil()
            CuilDiv=Cuil.split('-',3)
            dniIns=CuilDiv[1]
            if dniIns==dni:
                encontrado=True
            else:
                aux=aux.getSiguiente()
        return agente
    
    
    def modificarBasico(self,dni, nuevoBasico):
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            Cuil=agente.getCuil()
            CuilDiv=Cuil.split('-',3)
            dniIns=CuilDiv[1]
            if dniIns==dni:
                agente.setBasico(nuevoBasico)
                print(agente)
            aux=aux.getSiguiente()
            
    def modificarPorcentajeporcargo(self,dni, nuevoPorcentaje):
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            Cuil=agente.getCuil()
            CuilDiv=Cuil.split('-',3)
            dniIns=CuilDiv[1]
            if dniIns==dni:
                agente.setCargo(nuevoPorcentaje)
                print(agente)
            aux=aux.getSiguiente()


    def modificarPorcentajeporcategoría(self,dni, nuevoPorcentaje):
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            Cuil=agente.getCuil()
            CuilDiv=Cuil.split('-',3)
            dniIns=CuilDiv[1]
            if dniIns==dni:
                agente.setCategoria(nuevoPorcentaje)
                print(agente)
            aux=aux.getSiguiente()

            
    def modificarImporteExtra(self,dni, nuevoImporteExtra):
        aux=self.__comienzo
        while aux!=None:
            agente=aux.getAgente()
            Cuil=agente.getCuil()
            CuilDiv=Cuil.split('-',3)
            dniIns=CuilDiv[1]
            if dniIns==dni:
                agente.setImporte(nuevoImporteExtra)
                print(agente)
            aux=aux.getSiguiente()