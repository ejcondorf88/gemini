import os
import csv
import google.generativeai as genai
from collections import defaultdict
from langdetect import detect

class Traductor:
    def __init__(self, api_key):
        """Inicializa el traductor con la clave de API de Gemini."""
        os.environ["API_KEY"] = api_key
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def traducir_a_espanol(self, texto):
        """Detecta el idioma del texto y lo traduce al español si no está en español."""
        try:
            idioma = detect(texto)
            if idioma != "es":
                prompt = f"Traduce el siguiente texto al español: {texto}"
                response = self.model.generate_content(
                    contents=prompt,
                    generation_config={"temperature": 0.3, "max_output_tokens": 500}
                )
                return response.text.strip()
            return texto
        except Exception as e:
            print(f"Error al procesar texto: {e}")
            return texto

class AnalizadorBig5:
    def __init__(self, api_key):
        """Inicializa el analizador Big 5 con la clave de API de Gemini."""
        os.environ["API_KEY"] = api_key
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def analizar_usuario(self, texto_comentarios):
        """Analiza los comentarios de un usuario para estimar los rasgos Big 5."""
        prompt = f"""
Analiza el siguiente texto de un usuario para estimar sus rasgos de personalidad según el modelo Big 5 (Apertura, Conciencia, Extraversión, Amabilidad, Neuroticismo). Asigna una puntuación aproximada (1-5, donde 1 es bajo y 5 es alto) para cada rasgo y explica brevemente el razonamiento basado en el contenido del texto.

Texto: "{texto_comentarios}"

Proporciona la evaluación en el siguiente formato:
- Apertura: [puntuación]
  - Razonamiento: [explicación]
- Conciencia: [puntuación]
  - Razonamiento: [explicación]
- Extraversión: [puntuación]
  - Razonamiento: [explicación]
- Amabilidad: [puntuación]
  - Razonamiento: [explicación]
- Neuroticismo: [puntuación]
  - Razonamiento: [explicación]
"""
        response = self.model.generate_content(
            contents=prompt,
            generation_config={"temperature": 0.3, "max_output_tokens": 1000}
        )
        return response.text.strip()

class ProcesadorComentarios:
    def __init__(self, ruta_csv, api_key):
        """Inicializa el procesador de comentarios con la ruta del CSV y la clave de API."""
        self.ruta_csv = ruta_csv
        self.traductor = Traductor(api_key)
        self.analizador = AnalizadorBig5(api_key)

    def leer_comentarios(self):
        """Lee el CSV y organiza los comentarios por usuario."""
        comentarios_por_usuario = defaultdict(list)
        with open(self.ruta_csv, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar encabezado
            for row in reader:
                usuario, comentario = row
                comentarios_por_usuario[usuario].append(comentario)
        return comentarios_por_usuario

    def procesar_y_analizar(self):
        """Procesa los comentarios, los traduce y realiza el análisis Big 5."""
        comentarios_por_usuario = self.leer_comentarios()
        resultados = {}

        for usuario, comentarios in comentarios_por_usuario.items():
            # Traducir comentarios al español
            comentarios_es = [self.traductor.traducir_a_espanol(comentario) for comentario in comentarios]
            texto_comentarios = " ".join(comentarios_es)
            
            # Analizar Big 5
            analisis = self.analizador.analizar_usuario(texto_comentarios)
            resultados[usuario] = analisis

        return resultados

    def imprimir_resultados(self):
        """Imprime los resultados del análisis Big 5 en consola."""
        resultados = self.procesar_y_analizar()
        for usuario, analisis in resultados.items():
            print(f"\nUsuario: {usuario}")
            print(analisis)
            print("-" * 50)

if __name__ == "__main__":
    # Reemplaza con tu clave de API
    api_key = "AIzaSyCfoFHpShpPiae_doO5LXvbPishafLnmFg"
    procesador = ProcesadorComentarios('comentarios_limpios.csv', api_key)
    procesador.imprimir_resultados()