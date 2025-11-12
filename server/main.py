from flask import Flask, jsonify, request

app = Flask(__name__)

file_storage = {}


@app.route("/store", methods=["POST"])
def store_file():
    data = request.get_json()

    if not data or "file_id" not in data or "file_data" not in data:
        return jsonify({"error": "Missing file_id or file_data"}), 400

    file_id = data["file_id"]
    file_data = data["file_data"]

    file_storage[file_id] = file_data

    return jsonify({"message": f"File {file_id} stored successfully"}), 200


@app.route("/retrieve/<file_id>", methods=["GET"])
def retrieve_file(file_id):
    if file_id not in file_storage:
        return jsonify({"error": f"File {file_id} not found"}), 404

    file_data = file_storage[file_id]
    return jsonify({"file_id": file_id, "file_data": file_data}), 200




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8910)
