from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calc_bytes(text: str) -> int:
    # Excel/Google Sheets 방식: (LEN + LENB)/2
    lenn = len(text)                  # LEN
    lenb = len(text.encode("utf-8"))  # LENB (UTF-8)
    return (lenn + lenb) // 2         # 항상 정수가 나옴(한글/ASCII 기준)

@app.route("/bytecount", methods=["GET", "POST"])
def bytecount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")

    byte_count = calc_bytes(text)  # ✅ 올바른 함수 호출
    return jsonify({"byte_count": byte_count, "text": text}), 200

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
