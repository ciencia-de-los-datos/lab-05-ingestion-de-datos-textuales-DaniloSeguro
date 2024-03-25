import os
import pandas as pd

def read_files(directorio):
    datos = []
    for sentimiento in os.listdir(directorio): # Iterar sobre las carpetas pos y neg
        path_sentimiento = os.path.join(directorio, sentimiento) # Crear la ruta completa
        if os.path.isdir(path_sentimiento): # Verificar que sea un directorio
            for archivo in os.listdir(path_sentimiento): # Iterar sobre los archivos
                if archivo.endswith(".txt"): # Verificar que sea un archivo de texto
                    with open(os.path.join(path_sentimiento, archivo), 'r', encoding='utf-8') as f: # Leer el archivo
                        frase = f.read() # Leer el contenido del archivo
                        datos.append((frase, sentimiento)) # Agregar la frase y el sentimiento a la lista
    return datos

# Descomprimir el archivo data.zip
import zipfile
with zipfile.ZipFile("data.zip", 'r') as zip_ref: # Abrir el archivo zip
    zip_ref.extractall("data") # Extraer los archivos en la carpeta data

# Leer los archivos de entrenamiento
train_data = read_files("data/train") 

# Leer los archivos de prueba
test_data = read_files("data/test")

# Crear DataFrames
train_df = pd.DataFrame(train_data, columns=['phrase', 'sentiment'])
test_df = pd.DataFrame(test_data, columns=['phrase', 'sentiment'])

# Guardar en archivos CSV
train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)