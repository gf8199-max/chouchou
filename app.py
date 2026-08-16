from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
@app.get("/health")
def health():
    return jsonify({"success": True, "service": "douyin-monitor"})
