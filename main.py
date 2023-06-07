import json
from listaAgentes import ListaAgentes
from objectEncoder import ObjectEncoder
from menu import Menu
def test():
    jsonF=ObjectEncoder()
    lista=ListaAgentes()
    diccionario=jsonF.leerJSONArchivo('personal.json')
    lista=jsonF.decodificarDiccionario(diccionario)
    menu=Menu()
    menu.opciones(lista,jsonF)
    
if __name__=='__main__':
    test()