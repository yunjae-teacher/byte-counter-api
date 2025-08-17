import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calc_bytes(text: str) -> int:
    try:
        return len(text.encode("euc-kr"))
    except UnicodeEncodeError:
        # EUC-KR에 없는 문자는 그냥 2바이트로 계산
        return sum(1 if ord(ch) < 128 else 2 for ch in text)

@app.route("/bytecount", methods=["GET", "POST"])
def calculate_byte_count():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
    return jsonify({"byte_count": calc_bytes(text), "text": text})

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
