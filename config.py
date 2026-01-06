import os

class Config:
    # Model paths
    ENHANCED_MODEL_PATH = os.getenv("ENHANCED_MODEL_PATH", "frontend/model/enhanced_cotton_disease_model.h5")
    FALLBACK_MODEL_PATH = os.getenv("FALLBACK_MODEL_PATH", "frontend/model/DenseNet121.h5")
    
    # Dataset configuration
    KAGGLE_DATASET = os.getenv("KAGGLE_DATASET", "paridhijain02122001/cotton-crop-disease-detection")
    DATASET_PATH = os.getenv("DATASET_PATH", "dataset")
    
    # Image processing
    IMAGE_SIZE = (224, 224)
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 32))
    
    # Prediction settings
    CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.5))
    MAX_PREDICTION_TIME = int(os.getenv("MAX_PREDICTION_TIME", 10))
    
    # Upload settings
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
    
    # Disease classes (static list)
    DISEASE_CLASSES = [
        "Aphids",
        "Army_worm",
        "Bacterial_Blight",
        "Healthy",
        "Powdery_Mildew",
        "Target_spot"
    ]
    
    @staticmethod
    def init_app(app):
        """Initialize Flask app with configuration"""
        app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
        app.config['MAX_CONTENT_LENGTH'] = Config.MAX_FILE_SIZE
        
        # Ensure upload directory exists
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(os.path.dirname(Config.ENHANCED_MODEL_PATH), exist_ok=True)
