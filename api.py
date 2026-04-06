import requests
import csv
import os

def extraer_datos_paises(lista_codigos):
    """Extrae datos de países desde la API de restcountries.com"""
    url_base = "https://restcountries.com/v3.1/alpha/"
    resultados = []

    for codigo in lista_codigos:
        codigo_limpio = codigo.strip().upper()
        if not codigo_limpio: 
            continue
        
        try:
            respuesta = requests.get(f"{url_base}{codigo_limpio}", timeout=5)
            if respuesta.status_code == 200:
                datos_api = respuesta.json()[0]
                info = {
                    "code": codigo_limpio,
                    "name": datos_api.get('name', {}).get('common', 'N/A'),
                    "region": datos_api.get('region', 'N/A'),
                    "population": datos_api.get('population', 0)
                }
                resultados.append(info)
                print(f"✓ API: Datos de {codigo_limpio} obtenidos.")
        except Exception as e:
            print(f"✗ Error con {codigo_limpio}: {e}")

    return resultados

def generar_csv_paises(ruta_usuarios="data/users.csv", ruta_salida="data/countries.csv"):
    """Lee códigos de país del CSV de usuarios y genera el CSV de países"""
    
    # Paso 1: Leer códigos únicos del CSV de usuarios
    codigos_unicos = set()
    
    try:
        with open(ruta_usuarios, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                if 'country_code' in fila:
                    codigos_unicos.add(fila['country_code'].strip())
        
        print(f"📂 CSV leído. Se encontraron {len(codigos_unicos)} países únicos.")
        
        # Paso 2: Consultar la API
        lista_codigos = sorted(list(codigos_unicos))
        datos_paises = extraer_datos_paises(lista_codigos)
        
        # Paso 3: Crear nuevo CSV con los datos de la API
        if datos_paises:
            with open(ruta_salida, mode='w', newline='', encoding='utf-8') as archivo:
                fieldnames = ['code', 'name', 'region', 'population']
                writer = csv.DictWriter(archivo, fieldnames=fieldnames)
                
                writer.writeheader()
                for pais in datos_paises:
                    writer.writerow(pais)
            
            print(f"\n✓ CSV generado exitosamente: {ruta_salida}")
            print(f"✓ {len(datos_paises)} países insertados.\n")
            
            # Mostrar resultado
            print("--- DATOS INSERTADOS EN countries.csv ---")
            for p in datos_paises:
                print(f"  {p['code']}: {p['name']} | {p['region']} | Población: {p['population']:,}")
            
            return True
        else:
            print("✗ No se obtuvieron datos de la API.")
            return False
            
    except FileNotFoundError:
        print(f"✗ No encontré el archivo {ruta_usuarios}")
        return False

# Ejecutar si se corre este archivo directamente
if __name__ == "__main__":
    generar_csv_paises()