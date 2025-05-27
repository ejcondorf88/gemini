# Proyecto de Análisis de Datos

Este proyecto está diseñado para analizar datos, posiblemente relacionados con comentarios y análisis de personalidad (Big Five).

## Estructura del Proyecto

- `main.py`: Punto de entrada principal del proyecto.
- `analizador.py`: Contiene la lógica para analizar datos.
- `extractor_pdf.py`: Utilizado para extraer datos de archivos PDF.
- `comentarios_limpios.csv`: Archivo CSV con datos de comentarios.
- `BigFive Usuarios (1).pdf`: Archivo PDF con datos de usuarios.
- `requeriments.txt`: Lista de dependencias del proyecto.

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual:
   - En Windows: `venv\\Scripts\\activate`
   - En macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias: `pip install -r requeriments.txt`
5. Copia `env.template` a `.env` y añade tu token: `YOUR_TOKEN=tu_token_real`

## Uso

1. Asegúrate de que el entorno virtual esté activado.
2. Ejecuta el script principal: `python main.py`

## Notas

- El archivo `.env` contiene variables de entorno sensibles y no debe ser compartido.
- El archivo `comentarios_limpios.csv` contiene datos procesados para análisis. ![image](https://github.com/user-attachments/assets/8ea73826-c11f-44f3-a164-5836bdf5d45e)
