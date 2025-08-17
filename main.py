from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calc_bytes(text: str) -> int:
    # LENB: UTF-8 바이트 수
    lenb = len(text.encode("utf-8"))
    # LEN: 문자열 길이
    lenn = len(text)
    # Excel/Google Sheets 수식 적용
    return (lenb - lenn) * 3 + ((lenn * 2) - lenb)

@app.route("/bytecount", methods=["GET", "POST"])
def bytecount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:  # POST
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")

    byte_count = calc_bytes(text)
    return jsonify({"byte_count": byte_count, "text": text}), 200

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
