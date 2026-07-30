# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

COMISION_BASICA = 0.05
COMISION_ALTA = 0.08
META_COMISION_ALTA = 30000
META_BONO = 50000
BONO = 500
ANCHO_REPORTE = 44

# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas):
    if ventas > META_COMISION_ALTA:
        porcentaje = COMISION_ALTA
        bono = BONO if ventas > META_BONO else 0
    else:
        porcentaje = COMISION_BASICA
        bono = 0

    comision = round(ventas * porcentaje, 2)
    return round(comision + bono, 2)


def calcular_comisiones():
    total_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for nombre, ventas in vendedores:
        total_comision = calcular_comision(ventas)
        total_pagar += total_comision
        print(nombre + ": Q " + str(total_comision))

    # ta = tp * 1.12
    # print("con iva", ta)

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()