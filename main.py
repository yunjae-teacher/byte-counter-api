from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def calc_bytes(text: str) -> int:
    lenb = len(text.encode("utf-8"))
    lenn = len(text)
    return (lenb - lenn) * 3 + (lenn * 2 - lenb)

@app.route("/bytecount", methods=["GET", "POST"])
def bytecount():
    if request.method == "GET":
        text = request.args.get("text", "")
    else:  # POST
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")

    byte_count = calc_euckr_bytes(text)
    return jsonify({"byte_count": byte_count, "text": text})


@app.route("/healthz")
def healthz():
    return jsonify(status="ok"), 200


# Render에서는 gunicorn이 실행하므로 app.run() 불필요
# 로컬 테스트용:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
