# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:57:16 2022

@author: Diego Sanmiguel
"""

def consultar_todo_el_menu(menu):
    for item_menu in menu:
        print(item_menu)
        print("-"*50)

def generador_id(menu):
    list_id = []
    cont = 0
    mayor = "0"
    for item_menu in menu:
        list_id.append(item_menu[0].split("ID"))
        num_id = list_id[cont][1]
        cont += 1
        if num_id > mayor:
            mayor = num_id

    nuevo_id = int(mayor) + 1

    return "ID" + str(nuevo_id)

def agregar_menu(menu, id_, tipo_plato, plato):
    nuevo_menu = []
    nuevo_menu.append(id_)
    nuevo_menu.append(tipo_plato)
    nuevo_menu.append(plato)
    menu.append(nuevo_menu)

def consultar_por_tipo_plato(menu, tipo_plato):
    for item_menu in menu:
        if tipo_plato == item_menu[1]:
            print("-"*50)
            print(item_menu)
            print("-"*50)

def consultar_por_nombre_plato(menu, nombre_plato):
    for item_menu in menu:
        if nombre_plato in item_menu[2]:
            print("-"*50)
            print(item_menu)
            print("-"*50)        
           
def listar_menu_por_plato(menu):
    listado_por_tipo_de_plato = {}
    for item in menu:
        tipo_plato = item[1]
        nombre = item[2]
        if tipo_plato not in listado_por_tipo_de_plato:
            listado_por_tipo_de_plato[tipo_plato] = []

        listado_por_tipo_de_plato[tipo_plato].append(nombre)

    return listado_por_tipo_de_plato


def imprimir_diccionario(diccionario):
    for key, value in diccionario.items():
        print(key, value)
        print("-"*50)

def iniciar_aplicacion():

    menu = [
        ["ID004", "entrada", "ensalada"],
        ["ID008", "entrada", "sopa de tomate"],
        ["ID005", "entrada", "sopa de cebolla"],
        ["ID011", "bebida", "Jugo de Fresa"],
        ["ID012", "bebida", "Limonada Natural"],
        ["ID102", "plato fuerte", "pasta"],
        ["ID106", "plato fuerte", "lassagna"],
    ]

    ejecutando = True
    while ejecutando:

        ejecutando = mostrar_menu_aplicacion(menu)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(menu) -> bool:

    print("Menu de opciones")
    print(" 1 - Consultar menú")
    print(" 2 - Agregar nuevo elemento al menú")
    print(" 3 - Consultar opciones de menú por tipo de plato")
    print(" 4 - Consultar platos por nombre")
    print(" 5 - Listar el menú por tipo de plato")
    print(" 6 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        consultar_todo_el_menu(menu)

    elif opcion_elegida == "2":

        id_ = generador_id(menu)
        tipo_plato = input("Ingrese el tipo de plato que desea agregar: ")
        plato = input("Ingrese el plato que corresponde al tipo de plato agregado: ")

        agregar_menu(menu, id_, tipo_plato, plato)

    elif opcion_elegida == "3":
        tipo_plato = input("Digite el tipo de menú que desa consultar: ")
        consultar_por_tipo_plato(menu, tipo_plato)

    elif opcion_elegida == "4":
        nombre_plato = input("Digite el nombre del plato que desea consultar: ")
        consultar_por_nombre_plato(menu, nombre_plato)

    elif opcion_elegida == "5":
        listado_por_tipo_de_plato = listar_menu_por_plato(menu)
        imprimir_diccionario(listado_por_tipo_de_plato)

    elif opcion_elegida == "6":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando


if __name__ == "__main__":
    iniciar_aplicacion()