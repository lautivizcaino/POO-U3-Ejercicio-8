from listaAgentes import ListaAgentes
from interfacesAdministradores import IDirector

class MenuDirector:
    __opcion:int
    def __init__(self) -> None:
        self.__opcion=int
    def opciones(self,lista):
        print('\nMENU DIRECTOR')
        while self.__opcion!=0:
            print('\n1 - Modificar Basico\n2 - Modificar porcentaje por cargo\n3 - Modificar porcentaje por categoria\n4 - Modificar Importe Extra\n0 - Salir\n')
            self.__opcion=int(input('Ingrese opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nOPCION 1')
                dni=input('Ingrese DNI: ')
                basico=float(input('Ingrese Nuevo Sueldo Basico: '))
                lista.modificarBasico(dni,basico)
            elif self.__opcion==2:
                print('\nOPCION 2')
                dni=input('Ingrese DNI: ')
                cargo=input('Ingrese Nuevo Cargo: ')
                lista.modificarPorcentajeporcargo(dni,cargo)

            elif self.__opcion==3:
                print('\nOPCION 3')
                dni=input('Ingrese DNI: ')
                categoria=input('Ingrese Nueva Categoria: ')
                lista.modificarPorcentajeporcategoría(dni,categoria)
            elif self.__opcion==4:
                print('\nOPCION 4')
                dni=input('Ingrese DNI: ')
                importe=float(input('Ingrese Nuevo Importe Extra: '))
                lista.modificarImporteExtra(dni,importe)
        else:
            print('\nHA SALIDO DEL MENU DIRECTOR')