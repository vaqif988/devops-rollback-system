from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "unknown")

@app.route("/")
def index():
    return f"Hello from Flask app! Version: {VERSION}\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
