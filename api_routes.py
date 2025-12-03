"""
Optional JSON API endpoints for React frontend
Add these routes to app.py to enable JSON API support
This file is ADDITIVE - it doesn't replace existing routes
"""

from flask import jsonify, request, url_for
from tensorflow.keras.models import load_model
from disease_classifier.dataset_handler import DatasetHandler
import numpy as np
import os
import glob
from datetime import datetime

# These will be initialized when added to app.py
model = None
handler = None
UPLOAD_FOLDER = "uploads"

def init_api(flask_app, ml_model, data_handler):
    """
    Initialize API routes with Flask app and model
    Call this from app.py after loading model
    """
    global model, handler
    model = ml_model
    handler = data_handler
    
    # Register routes
    flask_app.add_url_rule('/api/health', 'api_health', api_health, methods=['GET'])
    flask_app.add_url_rule('/api/predict', 'api_predict', api_predict, methods=['POST'])
    flask_app.add_url_rule('/api/model/metadata', 'api_model_metadata', api_model_metadata, methods=['GET'])
    flask_app.add_url_rule('/api/model/metrics', 'api_model_metrics', api_model_metrics, methods=['GET'])

def api_health():
    """
    Health check endpoint
    GET /api/health
    """
    return jsonify({
        'status': 'healthy',
        'message': 'JSON API is available',
        'timestamp': datetime.now().isoformat()
    })

def api_predict():
    """
    JSON prediction endpoint
    POST /api/predict
    Accepts: multipart/form-data with 'file' field
    Returns: JSON with prediction results
    """
    try:
        # Check if file is present
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

        # Return JSON response
        return jsonify({
            'success': True,
            'label': predicted_label,
            'confidence': confidence,
            'probabilities': probabilities,
            'image_url': url_for('send_uploaded_file', filename=image_file.filename, _external=True),
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def api_model_metadata():
    """
    Get model metadata
    GET /api/model/metadata
    """
    try:
        _, index_to_class = handler.get_class_mapping()
        classes = [index_to_class[i].replace('_', ' ') for i in sorted(index_to_class.keys())]
        
        return jsonify({
            'model_name': 'DenseNet121',
            'model_path': 'model/enhanced_model.h5',
            'classes': classes,
            'num_classes': len(classes),
            'image_size': [224, 224],
            'last_trained': 'Unknown',  # Can be read from a metadata file if available
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def api_model_metrics():
    """
    Get training metrics (if available)
    GET /api/model/metrics
    """
    try:
        # Check if metrics file exists
        metrics_path = 'model/metrics.json'
        if os.path.exists(metrics_path):
            import json
            with open(metrics_path, 'r') as f:
                metrics = json.load(f)
            return jsonify(metrics)
        else:
            return jsonify({
                'message': 'Training metrics not available',
                'accuracy': '~97%',
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
