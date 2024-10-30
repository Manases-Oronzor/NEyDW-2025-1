from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    # Ejecutar Flask con HTTPS habilitado
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))

