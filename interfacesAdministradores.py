from zope.interface import Interface
class ITesorero (Interface):
    def gastosSueldoPorEmpleado (dni):
        pass

class IDirector (Interface):
    def modificarBasico(dni, nuevoBasico):
        pass
    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):
        pass
    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):
        pass
    def modificarImporteExtra(dni, nuevoImporteExtra):
        pass