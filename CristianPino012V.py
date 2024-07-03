# Evaluación 3
import csv
import random
import os
import time
lista_registro = []
sectores = ("San Bernardo", "Calera de Tango", "Buin")


def menu_cat():
    os.system("cls")
    print("         CatPremiun")
    print("___________________________")
    print("")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

def registrar_pedido():
    os.system("cls")
    print("Registrar pedido")
    try:
        num_pedido = int(input("Ingrese número de pedido: "))
        lista_registro = num_pedido
    except ValueError:
        print("Debe ingresar un número.")
    
    try:
        cliente = str(input("Ingrese nombre y apellido del cliente: "))
        lista_registro = cliente
    except ValueError:
        print("Ingrese sólo texto.")
        
    try:
        direccion = str(input("Ingrese dirección: "))
        lista_registro = direccion
    except ValueError:
        print("Ingrese sólo texto.")

    try:
        comuna = str(input("Ingrese Comuna: "))
        lista_registro = comuna
    except ValueError:
        print("Ingrese sólo texto.")

    while True:
        sacos = ()
        cinco = 0
        diez = 0
        veinte = 0
        resp_sacos = int(input("Ingrese el peso del saco (5 kls., 10 kls., 20 kls.): "))
        resp_cantidad = int(input("Ingrese cantidad de sacos: "))
        if resp_sacos == 5:
            cinco = resp_sacos
        elif resp_sacos == 10:
            diez = resp_sacos
        elif resp_sacos == 20:
            veinte = resp_sacos
        
        if resp_cantidad >0:
            sacos = resp_cantidad
            break



def listar_todos_los_pedidos():
    print("Estoy cansado jefe")


def imprimir_hoja_de_ruta():
    print("No he podido estudiar")

def salir_del_programa():
    print("Se me olvidó todo")




os.system("cls")
print(menu_cat())
print("")
opcion = int(input("Ingrese una opción: "))
while True:
    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        listar_todos_los_pedidos()
    elif opcion == 3:
        imprimir_hoja_de_ruta()
    elif opcion == 4:
        salir_del_programa()


print(lista_registro)

