from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data), 201

@app.route('/api', methods=['PUT'])
def put_data():
    data = request.get_json()
    updated_data = {"message": "Data updated", "data": data}
    return jsonify(updated_data)
@app.route('/api', methods=['DELETE'])
def delete_data():
    return jsonify({"message": "Data deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
