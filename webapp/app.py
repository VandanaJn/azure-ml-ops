from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np
from transformers import RobertaTokenizer
import os
app = Flask(__name__)

# Load tokenizer and ONNX model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = ort.InferenceSession(os.path.join("webapp", "roberta_sentiment.onnx"))

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

@app.route("/")
def home():
    return "<h1>Hello from ONNX sentiment predictor!</h1>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    print(text)

    # Tokenize input
    encoded = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    inputs = {k: to_numpy(v) for k, v in encoded.items()}

    # Run inference
    output = session.run(None, inputs)
    prediction = int(np.argmax(output[0]))

    return jsonify({"positive": bool(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)