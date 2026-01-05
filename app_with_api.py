# app_with_api.py
# Enhanced version of app.py with JSON API support for React frontend
# This is OPTIONAL - the original app.py still works without changes

from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from disease_classifier.dataset_handler import DatasetHandler
import numpy as np
import os
import glob
import json

# Initialize app
app = Flask(__name__)

# Enable CORS for React frontend (development)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    },
    r"/uploads/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    }
})

# Paths
MODEL_PATH = "model/enhanced_model.h5"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model + dataset handler
model = load_model(MODEL_PATH)
handler = DatasetHandler()

# Load disease info (preventive measures & causing agents)
DISEASE_INFO = {}
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    info_path = os.path.join(base_dir, 'data', 'disease_info.json')
    if not os.path.exists(info_path):
        info_path = os.path.join(os.getcwd(), 'data', 'disease_info.json')
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            DISEASE_INFO = json.load(f)
except Exception:
    DISEASE_INFO = {}

# ============================================================================
# ORIGINAL ROUTES (unchanged - for backward compatibility)
# ============================================================================

@app.route('/')
def home():
    """Original home route - serves HTML template"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Original prediction route - returns HTML"""
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

@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    """Original route to serve uploaded images"""
    return send_from_directory(UPLOAD_FOLDER, filename)

# ============================================================================
# NEW JSON API ROUTES (for React frontend)
# ============================================================================

@app.route('/api/health', methods=['GET'])
def api_health():
    """Health check endpoint"""
    from datetime import datetime
    return jsonify({
        'status': 'healthy',
        'message': 'JSON API is available',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON prediction endpoint"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        image_file = request.files['file']
        if image_file.filename == '':
            return jsonify({'error': 'Please select an image'}), 400

        # Clear old uploads
        for old_file in glob.glob(os.path.join(UPLOAD_FOLDER, '*')):
            try:
                os.remove(old_file)
            except:
                pass

        # Save new file
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)

        # Preprocess and predict
        img = handler.preprocess_image(image_path)
        if img is None:
            return jsonify({'error': 'Failed to process image'}), 400

        preds = model.predict(img)
        predicted_index = np.argmax(preds)
        confidence = round(float(np.max(preds)) * 100, 2)

        # Get readable label
        _, index_to_class = handler.get_class_mapping()
        predicted_label = index_to_class[predicted_index].replace('_', ' ')

        # Get all probabilities
        probabilities = []
        for idx, prob in enumerate(preds[0]):
            class_name = index_to_class[idx].replace('_', ' ')
            probabilities.append({
                'class': class_name,
                'probability': round(float(prob) * 100, 2)
            })

        from datetime import datetime
        # Generate full URL for the uploaded image
        image_url = f'http://127.0.0.1:5000/uploads/{image_file.filename}'
        # Attach preventive measures and causing agents when available
        disease_entry = DISEASE_INFO.get(predicted_label, {})
        preventive_measures = disease_entry.get('preventive_measures', [])
        causing_agents = disease_entry.get('causing_agents', [])

        return jsonify({
            'success': True,
            'label': predicted_label,
            'confidence': confidence,
            'probabilities': probabilities,
            'image_url': image_url,
            'preventive_measures': preventive_measures,
            'causing_agents': causing_agents,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/model/metadata', methods=['GET'])
def api_model_metadata():
    """Get model metadata"""
    try:
        _, index_to_class = handler.get_class_mapping()
        classes = [index_to_class[i].replace('_', ' ') for i in sorted(index_to_class.keys())]
        
        return jsonify({
            'model_name': 'DenseNet121',
            'model_path': 'model/enhanced_model.h5',
            'classes': classes,
            'num_classes': len(classes),
            'image_size': [224, 224],
            'last_trained': 'Unknown',
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/model/metrics', methods=['GET'])
def api_model_metrics():
    """Get training metrics"""
    return jsonify({
        'message': 'Training metrics not available',
        'accuracy': '~97%',
    })

# ============================================================================
# OPTIONAL: Serve React build in production
# ============================================================================

# Uncomment these routes to serve React build from Flask
# Make sure to build React first: cd frontend && npm run build
# Then copy frontend/dist to flask_app/static/react

# @app.route('/app')
# @app.route('/app/<path:path>')
# def serve_react(path=''):
#     """Serve React app"""
#     if path and os.path.exists(os.path.join('static/react', path)):
#         return send_from_directory('static/react', path)
#     return send_from_directory('static/react', 'index.html')

# Run app
if __name__ == "__main__":
    print("=" * 60)
    print("Cotton Disease Detection Server")
    print("=" * 60)
    print("Original HTML interface: http://127.0.0.1:5000/")
    print("JSON API health check:   http://127.0.0.1:5000/api/health")
    print("React frontend (dev):    http://localhost:5173/")
    print("=" * 60)
    print("\nRegistered routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.endpoint}: {rule.rule} {list(rule.methods)}")
    print("=" * 60)
    app.run(debug=False, host='127.0.0.1', port=5000)
