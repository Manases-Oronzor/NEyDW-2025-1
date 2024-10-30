from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Validación con Marshmallow
class DataSchema(Schema):
    name = fields.String(required=True)

data_schema = DataSchema()

# Ruta para manejar POST con validación
@app.route('/api', methods=['POST'])
def post_data():
    try:
        data = data_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"error": "Invalid input"}), 400  # Mensaje genérico
    return jsonify(data), 201

# Manejador de errores internos
@app.errorhandler(500)
def handle_500_error(e):
    return jsonify({"error": "Internal server error"}), 500  # Genérico

if __name__ == '__main__':
    app.run(debug=True)