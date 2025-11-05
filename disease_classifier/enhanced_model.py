# disease_classifier/enhanced_model.py
import os
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.optimizers import Adam
from disease_classifier.dataset_handler import DatasetHandler
from config import Config

# Load data
handler = DatasetHandler()
train_gen, val_gen, test_gen = handler.create_data_generators()

num_classes = len(train_gen.class_indices)
print(f"Detected {num_classes} classes from dataset.")


# Check for existing trained model
model_path = "model/enhanced_model.h5"
if os.path.exists(model_path):
    model = load_model(model_path)
    print("✅ Loaded existing model from disk.")
else:
    print("⚙️ Building new model using DenseNet121...")
    base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=Config.IMAGE_SIZE + (3,))
    x = GlobalAveragePooling2D()(base_model.output)
    
    x = Dropout(0.4)(x)

    # ✅ Automatically detect number of classes
    num_classes = len(train_gen.class_indices)
    print(f"Detected {num_classes} classes from dataset.")

    # ✅ Build output layer dynamically
    output = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=output)


    # Freeze base layers initially
    for layer in base_model.layers:
        layer.trainable = False

# Compile model
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=20,
    verbose=1
)

# Save the trained model
os.makedirs("model", exist_ok=True)
model.save(model_path)
print("💾 Model saved successfully to:", model_path)

# Evaluate on test data
loss, acc = model.evaluate(test_gen)
print(f"✅ Test Accuracy: {acc*100:.2f}%")
