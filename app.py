from flask import Flask, jsonify
import os
import math
import ruff
app = Flask(__name__)


def add(a: int, b: int) -> int:
    return a + b


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
