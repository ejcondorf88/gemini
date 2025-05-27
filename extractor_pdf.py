import fitz  # PyMuPDF
import re
import csv
from collections import defaultdict

class PDFComentarioExtractor:
    def __init__(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf
        self.data = defaultdict(list)

    def _limpiar_emojis(self, texto):
        # Quita emojis (caracteres fuera del plano básico)
        return re.sub(r'[\U00010000-\U0010ffff]', '', texto)

    def _procesar_texto(self, texto):
        usuario_actual = None

        for linea in texto.splitlines():
            linea = linea.strip()

            if not linea:
                continue

            # Buscar usuario (ej. ### Usuario: @usuario)
            match_usuario = re.match(r'^### Usuario: (@\w+)', linea)
            if match_usuario:
                usuario_actual = match_usuario.group(1)
                continue

            # Buscar comentario (ej. - "comentario...")
            match_comentario = re.match(r'^-\s*"(.*?)"', linea)
            if match_comentario and usuario_actual:
                comentario = self._limpiar_emojis(match_comentario.group(1))
                self.data[usuario_actual].append(comentario)

    def extraer(self):
        doc = fitz.open(self.ruta_pdf)

        for page in doc:
            texto = page.get_text("text")
            self._procesar_texto(texto)

        return dict(self.data)

    def guardar_csv(self, ruta_csv='comentarios_limpios.csv'):
        with open(ruta_csv, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Usuario', 'Comentario'])

            for usuario, comentarios in self.data.items():
                for comentario in comentarios:
                    writer.writerow([usuario, comentario])

# Código principal
extractor = PDFComentarioExtractor('./BigFive Usuarios (1).pdf')
comentarios = extractor.extraer()
extractor.guardar_csv()