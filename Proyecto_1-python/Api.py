import pandas as pd
from sodapy import Socrata

def obtener_resultados_api(departamento, municipio, cultivo, registro):
    client = Socrata("https://www.datos.gov.co/resource/ch4u-f3i5.json", None)
    
    filtro = {
        "departamento": departamento,
        "municipio": municipio,
        "cultivo": cultivo,
        "$limit": registro
    }

    results = client.get("ch4u-f3i5", **filtro)
    results_df = pd.DataFrame.from_records(results)
    
    return results_df
