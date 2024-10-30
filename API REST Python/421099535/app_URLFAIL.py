from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta de inicio de sesión con datos sensibles en la URL (solo educativo)
@app.route('/login', methods=['GET'])
def login():
    # Obtener los parámetros de la URL
    username = request.args.get("username")
    password = request.args.get("password")

    # Verificación básica (solo para demostración)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)