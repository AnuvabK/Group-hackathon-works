from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")
    image = request.files.get("image")

    # placeholder logic
    result = f"You entered: {text}"

    return result