import os
import logging
from flask import Flask, render_template, send_from_directory

# Configurar logging para facilitar la depuración
logging.basicConfig(level=logging.DEBUG)

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key_for_development")

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/claude')
def claude():
    return render_template('claude.html')

@app.route('/asistente')
def asistente():
    return render_template('asistente.html')

@app.route('/comparacion')
def comparacion():
    return render_template('comparacion.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/codigo')
def codigo():
    # Usaremos una nueva plantilla sin el problema del 'keyword'
    return render_template('codigo_real.html')

@app.route('/descargar/streamlit')
def descargar_streamlit():
    return send_from_directory('static', 'app_qrgb_streamlit.py')

@app.route('/version-web')
def version_web():
    return render_template('version_web.html')

@app.route('/descargar/version-web')
def descargar_version_web():
    return send_from_directory('static', 'github_pages_qrgb.zip')

@app.route('/descargar/proyecto-completo')
def descargar_proyecto_completo():
    return send_from_directory('.', 'proyecto_qrgb_completo_v2.zip')

# Si el archivo se ejecuta directamente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
