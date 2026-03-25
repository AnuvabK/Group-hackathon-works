import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        text_query = request.form.get("text", "").strip()
        image_file = request.files.get("image")

        if not text_query and (not image_file or image_file.filename == ""):
            return "Please provide an image or a description.", 400

        result = ""
   
        if text_query:
            result += f"You entered: {text_query}\n"

        if image_file and image_file.filename != "":
            result += f"Image uploaded: {image_file.filename}\n"

        return result

    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
