"""
Dataset Download Script
Downloads and prepares the Kaggle cotton disease dataset using the built-in dataset handler
"""
import os
import sys
from disease_classifier.dataset_handler import DatasetHandler
from config import Config

def main():
    print("=" * 60)
    print("Cotton Disease Dataset Download & Preparation")
    print("=" * 60)
    
    # Initialize dataset handler
    dataset_handler = DatasetHandler()
    
    print(f"Target dataset path: {dataset_handler.dataset_path}")
    print(f"Kaggle dataset: {Config.KAGGLE_DATASET}")
    print()
    
    # Step 1: Download dataset
    print("Step 1: Downloading dataset from Kaggle...")
    print("Note: This requires Kaggle API credentials to be set up.")
    print("If you haven't set up Kaggle API, please follow these steps:")
    print("1. Go to https://www.kaggle.com/account")
    print("2. Click 'Create New API Token' to download kaggle.json")
    print("3. Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\\Users\\{username}\\.kaggle\\ (Windows)")
    print()
    
    try:
        success = dataset_handler.download_dataset()
        if success:
            print("✅ Dataset downloaded successfully!")
        else:
            print("❌ Dataset download failed!")
            return False
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        print("\nTroubleshooting tips:")
        print("- Ensure Kaggle API credentials are properly configured")
        print("- Check internet connection")
        print("- Verify the dataset exists and is accessible")
        return False
    
    # Step 2: Validate dataset structure
    print("\nStep 2: Validating dataset structure...")
    try:
        is_valid = dataset_handler.validate_dataset()
        if is_valid:
            print("✅ Dataset structure is valid!")
        else:
            print("❌ Dataset structure validation failed!")
            return False
    except Exception as e:
        print(f"❌ Error validating dataset: {e}")
        return False
    
    # Step 3: Get class information
    print("\nStep 3: Analyzing dataset classes...")
    try:
        class_indices, index_to_class = dataset_handler.get_class_mapping()
        if class_indices:
            print("✅ Class mapping retrieved successfully!")
            print(f"Found {len(class_indices)} classes:")
            for class_name, index in class_indices.items():
                print(f"  {index}: {class_name}")
        else:
            print("❌ Could not retrieve class mapping!")
            return False
    except Exception as e:
        print(f"❌ Error getting class mapping: {e}")
        return False
    
    # Step 4: Test data generators
    print("\nStep 4: Testing data generators...")
    try:
        train_gen, val_gen, test_gen = dataset_handler.create_data_generators()
        if train_gen and val_gen and test_gen:
            print("✅ Data generators created successfully!")
            print(f"Training samples: {train_gen.samples}")
            print(f"Validation samples: {val_gen.samples}")
            print(f"Test samples: {test_gen.samples}")
            print(f"Batch size: {train_gen.batch_size}")
            print(f"Image size: {train_gen.target_size}")
        else:
            print("❌ Failed to create data generators!")
            return False
    except Exception as e:
        print(f"❌ Error creating data generators: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Dataset preparation completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Run 'python train_enhanced_model.py' to train the enhanced model")
    print("2. The enhanced system will automatically activate once training is complete")
    print("3. Your web application will then support comprehensive disease detection")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Dataset preparation failed. Please check the errors above and try again.")
        sys.exit(1)
    else:
        print("\n✅ All steps completed successfully!")
        sys.exit(0)