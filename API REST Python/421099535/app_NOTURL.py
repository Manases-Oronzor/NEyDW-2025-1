from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta de inicio de sesión (sin datos sensibles en la URL)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Ejemplo simple de autenticación
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)