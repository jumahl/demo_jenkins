import yaml
import pickle
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    # Vulnerabilidad: Deserialización insegura de YAML
    config_file = request.args.get('file', 'config.yml')
    with open(config_file, 'r') as f:
        return yaml.load(f)  # Inseguro: debería usar yaml.safe_load()

@app.route('/execute')
def execute_command():
    # Vulnerabilidad: Ejecución de comandos del sistema
    cmd = request.args.get('cmd', 'echo "Hello"')
    output = subprocess.popen(cmd, shell=True)  # Inseguro: permite inyección de comandos
    return output.read()

@app.route('/load_data')
def load_data():
    # Vulnerabilidad: Deserialización insegura de pickle
    data_file = request.args.get('file', 'data.pkl')
    with open(data_file, 'rb') as f:
        return pickle.load(f)  # Inseguro: pickle puede ejecutar código malicioso

if __name__ == '__main__':
    app.run(debug=True)  # Inseguro: modo debug en producción