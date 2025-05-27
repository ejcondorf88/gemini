import os
from dotenv import load_dotenv
from extractor_pdf import PDFComentarioExtractor
from analizador import AnalizadorBig5
from analizador import ProcesadorComentarios

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la API key desde las variables de entorno
api_key = os.getenv('YOUR_TOKEN')

# Inicializar el extractor de PDF
csv = PDFComentarioExtractor('./BigFive Usuarios (1).pdf')
comentarios = csv.extraer()
test = csv.guardar_csv()

# Procesar y analizar los comentarios
procesador = ProcesadorComentarios('comentarios_limpios.csv', api_key)
procesador.procesar_y_analizar()
procesador.imprimir_resultados()


