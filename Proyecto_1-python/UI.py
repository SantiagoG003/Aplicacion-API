import numpy as np

def seleccion_usuario():
    departamento = input("Ingrese el nombre del departamento: ").upper()
    municipio = input("Ingrese el nombre del municipio: ").upper()
    cultivo = input("Ingrese el nombre del cultivo: ").capitalize()
    return departamento, municipio, cultivo


def mostrar_propiedades_cultivo(propiedades_cultivo):
    columnas_a_omitir = ['drenaje', 'riego','fertilizantes_aplicados', 'fechaanalisis', 'estado', 'tiempo_establecimiento']
    columnas_mediana = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']

    if not propiedades_cultivo.empty:
        print("Propiedades del cultivo seleccionado:")
        for indice, fila in propiedades_cultivo.iterrows():
            print("\nRegistro:")
            for columna, valor in fila.items():
                if columna not in columnas_a_omitir:
                    print(f"{columna.replace('_', ' ').title()}: {valor}")

        
        mediana_edaficas = propiedades_cultivo[columnas_mediana].median()
        print("\nMediana de las variables edáficas:")
        for columna, valor in mediana_edaficas.items():
            print(f"{columna.replace('_', ' ').title()}: {valor}")

    else:
        print("No se encontraron propiedades para el cultivo especificado en el departamento y municipio seleccionados.")