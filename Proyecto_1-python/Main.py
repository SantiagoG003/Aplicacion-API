import UI as ui
import Api as api

def main():
    try:
        departamento = ui.ingresar_departamento()
        municipio = ui.ingresar_municipio()
        cultivo = ui.ingresar_cultivo()
        registro = ui.numero_registros()

        resultados = api.obtener_resultados_api(departamento, municipio, cultivo, registro)

        print("\nResultados obtenidos:")
        if not resultados.empty:
            for idx, row in resultados.iterrows():
                print(f"\nRegistro {idx + 1}:")
                print(f"Departamento: {row['departamento']}")
                print(f"Municipio: {row['municipio']}")
                print(f"Cultivo: {row['cultivo']}")
                # Imprime otras propiedades relevantes
        else:
            print("No se encontraron resultados para los criterios especificados.")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
