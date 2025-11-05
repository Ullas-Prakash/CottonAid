"""
Dataset Handler for Cotton Disease Detection
Handles Kaggle dataset download, preprocessing, and data preparation
"""
import os
import kagglehub
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import cv2
from config import Config

class DatasetHandler:
    def __init__(self):
        self.dataset_path = Config.DATASET_PATH
        self.image_size = Config.IMAGE_SIZE
        self.batch_size = Config.BATCH_SIZE
        self.disease_classes = Config.DISEASE_CLASSES
        
    def download_dataset(self):
        """Download the Kaggle dataset using kagglehub"""
        try:
            print("Downloading cotton disease dataset from Kaggle...")
            path = kagglehub.dataset_download(Config.KAGGLE_DATASET)
            print(f"Dataset downloaded to: {path}")
            
            # Copy to our dataset directory
            import shutil
            if os.path.exists(self.dataset_path):
                shutil.rmtree(self.dataset_path)
            shutil.copytree(path, self.dataset_path)
            
            return True
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            return False
    
    def preprocess_image(self, image_path):
        """Preprocess individual image for model input"""
        try:
            # Load image
            image = load_img(image_path, target_size=self.image_size)
            image_array = img_to_array(image)
            
            # Normalize pixel values
            image_array = image_array / 255.0
            
            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
        except Exception as e:
            print(f"Error preprocessing image {image_path}: {e}")
            return None
    
    def create_data_generators(self):
        """Create data generators for training, validation, and testing"""
        try:
            # Data augmentation for training
            train_datagen = ImageDataGenerator(
                rescale=1./255,
                rotation_range=20,
                width_shift_range=0.2,
                height_shift_range=0.2,
                horizontal_flip=True,
                zoom_range=0.2,
                validation_split=0.2
            )
            
            # Only rescaling for validation/test
            test_datagen = ImageDataGenerator(rescale=1./255)
            
            # Training generator
            train_generator = train_datagen.flow_from_directory(
                os.path.join(self.dataset_path, 'train'),
                target_size=self.image_size,
                batch_size=self.batch_size,
                class_mode='categorical',
                subset='training'
            )
            
            # Validation generator
            validation_generator = train_datagen.flow_from_directory(
                os.path.join(self.dataset_path, 'train'),
                target_size=self.image_size,
                batch_size=self.batch_size,
                class_mode='categorical',
                subset='validation'
            )
            
            # Test generator
            test_generator = test_datagen.flow_from_directory(
                os.path.join(self.dataset_path, 'test'),
                target_size=self.image_size,
                batch_size=self.batch_size,
                class_mode='categorical',
                shuffle=False
            )
            
            return train_generator, validation_generator, test_generator
            
        except Exception as e:
            print(f"Error creating data generators: {e}")
            return None, None, None
    
    def get_class_mapping(self):
        """Get mapping between class indices and disease names"""
        try:
            # Create a temporary generator to get class indices
            temp_datagen = ImageDataGenerator(rescale=1./255)
            temp_generator = temp_datagen.flow_from_directory(
                os.path.join(self.dataset_path, 'train'),
                target_size=self.image_size,
                batch_size=1,
                class_mode='categorical'
            )
            
            class_indices = temp_generator.class_indices
            index_to_class = {v: k for k, v in class_indices.items()}
            
            return class_indices, index_to_class
            
        except Exception as e:
            print(f"Error getting class mapping: {e}")
            return None, None
    
    def validate_dataset(self):
        """Validate that the dataset is properly structured"""
        try:
            train_path = os.path.join(self.dataset_path, 'train')
            test_path = os.path.join(self.dataset_path, 'test')
            
            if not os.path.exists(train_path) or not os.path.exists(test_path):
                print("Dataset structure is invalid. Missing train or test directories.")
                return False
            
            # Check for class directories
            train_classes = os.listdir(train_path)
            test_classes = os.listdir(test_path)
            
            print(f"Found {len(train_classes)} classes in training set")
            print(f"Found {len(test_classes)} classes in test set")
            print(f"Training classes: {train_classes}")
            
            return len(train_classes) > 0 and len(test_classes) > 0
            
        except Exception as e:
            print(f"Error validating dataset: {e}")
            return False