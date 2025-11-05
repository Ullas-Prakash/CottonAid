# app.py
from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from disease_classifier.dataset_handler import DatasetHandler
import numpy as np
import os
import glob

# Initialize app
app = Flask(__name__)

# Paths
MODEL_PATH = "model/enhanced_model.h5"   # change if you prefer a specific one
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model + dataset handler
model = load_model(MODEL_PATH)
handler = DatasetHandler()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', message="No file uploaded")

    image_file = request.files['file']
    if image_file.filename == '':
        return render_template('index.html', message="Please select an image")

    # Clear old uploads
    for old_file in glob.glob(os.path.join(UPLOAD_FOLDER, '*')):
        os.remove(old_file)

    # Save new file
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    # Preprocess and predict
    img = handler.preprocess_image(image_path)
    preds = model.predict(img)
    predicted_index = np.argmax(preds)
    confidence = round(float(np.max(preds)) * 100, 2)

    # Get readable label
    _, index_to_class = handler.get_class_mapping()
    predicted_label = index_to_class[predicted_index].replace('_', ' ')

    return render_template('result.html',
                           label=predicted_label,
                           confidence=confidence,
                           image_file=image_file.filename)

# Route to show uploaded image
@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
