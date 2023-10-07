"""
import re
from datetime import datetime

def validar_vencimiento(vencimiento):
    while True:
        if not re.match(r"^[0-9/]+$", vencimiento):
            vencimiento = input("El formato no es válido. Por favor, ingrese solo 2 números para el mes, seguido de '/', y luego 2 números para el año: ")
        elif not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", vencimiento):
            vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
        else:
            mes, anio = vencimiento.split('/')

            if not (mes.isdigit() and anio.isdigit()):
                vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                continue

            mes, anio = int(mes), int(anio)

            if not (1 <= mes <= 12 and 0 <= anio <= 99):
                vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                continue

            # Obtener la fecha actual
            fecha_actual = datetime.now()
            if fecha_actual.year > anio or (fecha_actual.year == anio and fecha_actual.month > mes):
                vencimiento = input("La fecha ingresada está vencida. Ingrese nuevamente (MM/AA): ")
                continue

            if anio < 23 or (anio == 23 and mes < fecha_actual.month):
                vencimiento = input("La fecha ingresada está vencida. Ingrese nuevamente (MM/AA): ")
                continue

            return mes, anio

vencimiento = input("Ingrese el vencimiento de la tarjeta (MM/AA): ")
mes, anio = validar_vencimiento(vencimiento)
print(f"Mes: {mes}, Año: {anio}")

"""

import re
from datetime import datetime

def validar_vencimiento(vencimiento):
    while True:
        if not re.match(r"^[0-9/]+$", vencimiento):
            vencimiento = input("El formato no es válido. Por favor, ingrese solo 2 números para el mes, seguido de '/', y luego 2 números para el año: ")
        elif not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", vencimiento):
            vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
        else:
            mes, anio = vencimiento.split('/')

            if not (mes.isdigit() and anio.isdigit()):
                vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                continue

            mes, anio = int(mes), int(anio)

            if not (1 <= mes <= 12 and 0 <= anio <= 99):
                vencimiento = input("El formato de vencimiento no es válido. Ingrese nuevamente (MM/AA): ")
                continue

            # Obtener la fecha actual
            fecha_actual = datetime.now()
            fecha_comparar = datetime(fecha_actual.year % 100, fecha_actual.month, 1)

            if fecha_comparar > datetime(anio, mes, 1):
                vencimiento = input("La fecha ingresada está vencida. Ingrese nuevamente (MM/AA): ")
                continue

            return mes, anio

vencimiento = input("Ingrese el vencimiento de la tarjeta (MM/AA): ")
mes, anio = validar_vencimiento(vencimiento)
print(f"Mes: {mes}, Año: {anio}")