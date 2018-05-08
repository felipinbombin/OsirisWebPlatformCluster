# -*- coding: utf-8 -*-
from . import RedAC as ac_network
from . import RedLineas as line_network


def energy_center_model(model_input, model_output):

    datos_linea = model_input['ECM']['dc_data']
    datos_cochrane = model_input['ECM']['ac_data']

    # Crear objeto linea
    Linea1 = line_network.Linea('Linea1', datos_linea)

    # Crear objeto red AC
    Cochrane = ac_network.RedAC('Cochrane', datos_cochrane)

    # Conectar línea a red AC
    Cochrane.addLinea(Linea1)

    # Definir escenario de simulación con el diccionario creado anteriormente
    Cochrane.DefinirSimulacion(datos_cochrane)

    # Definir escenario de simulación con el diccionario creado anteriormente
    Linea1.DefinirSimulacion(datos_linea)

    # Simular operación conjunto de red AC y línea de metro con potencia base Sbase = 1 [MW]
    Cochrane.simular(1)

    # Diccionario de resultados de las simulaciones
    return Cochrane.saveresults()
