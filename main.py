import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calc_bytes(text: str) -> int:
    # UTF-8 인코딩 기준 바이트 수
    return len(text.encode("utf-8"))

@app.route("/bytecount", methods=["GET", "POST"])
def bytecount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:  # POST(JSON)
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
    return jsonify({"byte_count": calc_bytes(text), "text": text}), 200

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
