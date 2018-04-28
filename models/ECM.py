# -*- coding: utf-8 -*-
from . import RedAC as ac_network
from . import RedLineas as line_network


def energy_center_model(model_input, model_output):
    # Crear objeto linea
    Linea1 = line_network.Linea('Linea1', DatosLinea1)

    # Crear objeto red AC
    Cochrane = ac_network.RedAC('Cochrane', DatosCochrane)

    # Conectar línea a red AC
    Cochrane.addLinea(Linea1)

    # Definir escenario de simulación con el diccionario creado anteriormente
    Cochrane.DefinirSimulacion(DatosCochrane)

    # Definir escenario de simulación con el diccionario creado anteriormente
    Linea1.DefinirSimulacion(DatosLinea1)

    # Simular operación conjunto de red AC y línea de metro con potencia base Sbase = 1 [MW]
    Cochrane.simular(1)

    # Diccionario de resultados de las simulaciones
    return Cochrane.saveresults()
