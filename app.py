import yaml
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    # Corrección: Deserialización segura de YAML
    config_file = request.args.get('file', 'config.yml')
    with open(config_file, 'r') as f:
        try:
            config = yaml.safe_load(f)  # Uso seguro de yaml.safe_load()
        except yaml.YAMLError as e:
            return jsonify({"error": "Error al cargar configuración"}), 400
    return jsonify(config)

@app.route('/execute')
def execute_command():
    # Corrección: Ejecución de comandos del sistema
    cmd = request.args.get('cmd', 'echo "Hello"')
    if cmd not in ["echo 'Hello'", "echo 'World'"]:  # Limitar comandos permitidos
        return jsonify({"error": "Comando no permitido"}), 400
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    return jsonify({"output": result.stdout.strip()})

@app.route('/load_data')
def load_data():
    # Corrección: Evitar deserialización de pickle
    return jsonify({"error": "Deserialización insegura deshabilitada"}), 403

if __name__ == '__main__':
    app.run(debug=False)  # Modo seguro en producción
