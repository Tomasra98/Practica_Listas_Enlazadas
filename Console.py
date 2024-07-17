import Practica_LE as Practica_LE
from Practica_LE import *
Sala_de_Urgencias = Priority_Queue()

def Consola():
    print("Sala de Urgencias")
    print("-----------------")
    print("Ingrese 1 para insertar un paciente")
    print("Ingrese 2 para atender algún paciente")
    print("Ingrese 3 para mostrar los pacientes en la Sala de Urgencias")
    print("Ingrese 4 para actualizar la prioridad de algún paciente existente")
    print("Ingrese 5 para atender a la mitad de cada lote")
    print("Ingrese 6 para salir de la Sala de Urgencias")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Crear_paciente(Sala_de_Urgencias)
        return Consola()
    if opcion == 2:
        Atención(Sala_de_Urgencias)
        return Consola()
    if opcion == 3:
        Sala_de_Urgencias.Mostrar_cola()
        return Consola()
    if opcion == 4:
        Actualizar_prioridad(Sala_de_Urgencias, Sala_de_Urgencias.head)
        return Consola()
    if opcion == 5:
        Atender_Mitad_De_Cada_Lote(Sala_de_Urgencias)
    if opcion == 6:
        print("------------------------------------------------------------------")
        return print("Has salido de la Sala de Urgencias")
    return Consola()
    
Consola()