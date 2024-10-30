import yaml
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    # Corrección: Usar yaml.safe_load() para deserialización segura
    config_file = request.args.get('file', 'config.yml')
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return jsonify(config)
    except Exception as e:
        return str(e), 400

@app.route('/execute')
def execute_command():
    # Corrección: Validar comandos permitidos
    allowed_commands = ['echo "Hello"', 'ls', 'pwd']
    cmd = request.args.get('cmd', 'echo "Hello"')
    if cmd not in allowed_commands:
        return "Comando no permitido", 400
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e), 400

@app.route('/load_data')
def load_data():
    # Corrección: Evitar el uso de pickle para datos no confiables
    return "Deserialización de pickle no permitida", 400

if __name__ == '__main__':
    app.run()  # No usar debug=True en producción