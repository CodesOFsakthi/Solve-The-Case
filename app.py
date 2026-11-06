from pathlib import Path

from flask import Flask, send_from_directory

app = Flask(__name__)
ROOT = Path(__file__).resolve().parent


@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")


@app.get("/video/<path:filename>")
def video(filename):
    return send_from_directory(ROOT / "video", filename)