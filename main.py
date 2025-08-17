from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 실제 바이트 수 계산 함수 (EUC-KR 기준)
def calculate_byte_count(text: str) -> int:
    try:
        return len(text.encode("euc-kr"))
    except UnicodeEncodeError:
        # euc-kr로 인코딩 불가능한 문자가 있을 경우 utf-8로 대체
        return len(text.encode("utf-8"))

# POST 요청 처리
@app.route("/bytecount", methods=["POST"])
def bytecount_post():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    text = data["text"]
    byte_count = calculate_byte_count(text)

    return jsonify({
        "text": text,
        "bytes": byte_count
    })

# GET 요청 처리 (추가)
@app.route("/bytecount", methods=["GET"])
def bytecount_get():
    text = request.args.get("text", "")
    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    byte_count = calculate_byte_count(text)

    return jsonify({
        "text": text,
        "bytes": byte_count
    })

# 상태 확인용
@app.route("/healthz", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
