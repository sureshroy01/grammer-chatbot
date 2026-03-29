from flask import Flask, render_template, request, jsonify
import language_tool_python
import os

app = Flask(__name__)

tool = language_tool_python.LanguageTool('en-US')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    text = request.json["text"]
    corrected = tool.correct(text)
    return jsonify({"result": corrected})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)