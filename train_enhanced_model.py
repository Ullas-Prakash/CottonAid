"""
Enhanced Model Training Script
Trains the comprehensive cotton disease detection model using the downloaded dataset
"""
import os
import sys
from disease_classifier.dataset_handler import DatasetHandler
from disease_classifier.enhanced_model import EnhancedDiseaseClassifier
from config import Config

def main():
    print("=" * 60)
    print("Enhanced Cotton Disease Model Training")
    print("=" * 60)
    
    # Check if dataset exists
    dataset_handler = DatasetHandler()
    if not dataset_handler.validate_dataset():
        print("❌ Dataset not found or invalid!")
        print("Please run 'python download_dataset.py' first to download the dataset.")
        return False
    
    print("✅ Dataset found and validated!")
    
    # Initialize model
    print("\nInitializing enhanced disease classifier...")
    classifier = EnhancedDiseaseClassifier()
    
    # Get class information
    class_indices, index_to_class = dataset_handler.get_class_mapping()
    num_classes = len(class_indices)
    print(f"Training for {num_classes} disease classes")
    
    # Update classifier with correct number of classes
    classifier.num_classes = num_classes
    
    # Create data generators
    print("\nCreating data generators...")
    train_gen, val_gen, test_gen = dataset_handler.create_data_generators()
    
    if not all([train_gen, val_gen, test_gen]):
        print("❌ Failed to create data generators!")
        return False
    
    print(f"✅ Data generators created:")
    print(f"  Training samples: {train_gen.samples}")
    print(f"  Validation samples: {val_gen.samples}")
    print(f"  Test samples: {test_gen.samples}")
    
    # Build model
    print("\nBuilding enhanced model architecture...")
    model = classifier.build_model()
    print("✅ Model architecture built successfully!")
    print(f"Model parameters: {model.count_params():,}")
    
    # Train model
    print("\nStarting model training...")
    print("This may take several hours depending on your hardware...")
    print("Training progress will be displayed below:")
    print("-" * 50)
    
    try:
        history = classifier.train_model(
            train_generator=train_gen,
            validation_generator=val_gen,
            epochs=20  # Limited to 20 cycles for faster training
        )
        
        if history:
            print("\n✅ Model training completed successfully!")
            
            # Plot training history
            print("\nGenerating training plots...")
            classifier.plot_training_history()
            print("✅ Training plots saved to 'model/training_history.png'")
            
        else:
            print("❌ Model training failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error during training: {e}")
        return False
    
    # Evaluate model
    print("\nEvaluating model performance...")
    try:
        evaluation_results = classifier.evaluate_model(test_gen)
        
        if evaluation_results:
            print("✅ Model evaluation completed!")
            print(f"Test Accuracy: {evaluation_results['test_accuracy']:.4f}")
            print(f"Test Top-3 Accuracy: {evaluation_results['test_top3_accuracy']:.4f}")
            
            # Check if accuracy meets requirements (90%+)
            if evaluation_results['test_accuracy'] >= 0.90:
                print("🎉 Model meets accuracy requirements (≥90%)!")
            else:
                print("⚠️  Model accuracy is below 90%. Consider:")
                print("   - Training for more epochs")
                print("   - Adjusting learning rate")
                print("   - Adding more data augmentation")
        else:
            print("❌ Model evaluation failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error during evaluation: {e}")
        return False
    
    # Verify model file exists
    if os.path.exists(Config.ENHANCED_MODEL_PATH):
        print(f"\n✅ Enhanced model saved to: {Config.ENHANCED_MODEL_PATH}")
        print("🎉 Training completed successfully!")
        
        print("\n" + "=" * 60)
        print("Next Steps:")
        print("=" * 60)
        print("1. Restart your Flask application")
        print("2. The enhanced system will automatically activate")
        print("3. Your web app now supports comprehensive disease detection!")
        print("4. Test with cotton leaf images to see the enhanced features")
        
        return True
    else:
        print("❌ Model file not found after training!")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Model training failed. Please check the errors above.")
        sys.exit(1)
    else:
        print("\n✅ Enhanced model training completed successfully!")
        sys.exit(0)