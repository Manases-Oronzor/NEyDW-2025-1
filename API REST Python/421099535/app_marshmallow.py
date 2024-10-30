from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Definir el esquema de validación
class DataSchema(Schema):
    name = fields.String(required=True)

data_schema = DataSchema()

@app.route('/api', methods=['POST'])
def post_data():
    try:
        # Validar los datos del cuerpo de la solicitud
        data = data_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400  # Error de validación
    return jsonify(data), 201  # Datos válidos

if __name__ == '__main__':
    app.run(debug=True)