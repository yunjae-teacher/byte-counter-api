from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/bytecount", methods=["POST"])
def calculate_byte_count():
    data = request.get_json()
    text = data.get("text", "")
    lenb = len(text.encode("euc-kr"))
    lenn = len(text)
    byte_count = (lenb - lenn) * 3 + (lenn * 2 - lenb)
    return jsonify({"byte_count": byte_count})

@app.route("/", methods=["GET"])
def home():
    return "Byte Counter API is running."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
