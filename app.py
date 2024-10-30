import yaml
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    # Corrección: Deserialización segura de YAML
    config_file = request.args.get('file', 'config.yml')
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)  # Uso seguro de yaml.safe_load()
        return jsonify(config)
    except FileNotFoundError:
        return jsonify({"error": "Archivo de configuración no encontrado"}), 404
    except yaml.YAMLError as e:
        return jsonify({"error": "Error al cargar configuración"}), 400

@app.route('/execute')
def execute_command():
    # Corrección: Ejecución de comandos del sistema
    cmd = request.args.get('cmd', 'echo "Hello"')
    allowed_commands = {
        "echo 'Hello'": ["echo", "Hello"],
        "echo 'World'": ["echo", "World"]
    }
    if cmd not in allowed_commands:
        return jsonify({"error": "Comando no permitido"}), 400
    try:
        result = subprocess.run(allowed_commands[cmd], capture_output=True, text=True, check=True)
        return jsonify({"output": result.stdout.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error al ejecutar el comando"}), 500

@app.route('/load_data')
def load_data():
    # Corrección: Evitar deserialización de pickle
    return jsonify({"error": "Deserialización insegura deshabilitada"}), 403

if __name__ == '__main__':
    app.run(debug=False)  # Modo seguro en producción