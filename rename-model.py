from tensorflow import keras

# Load the old model (adjust path if needed)
model = keras.models.load_model("model/enhanced_cotton_disease_model.h5", compile=False)

# Re-save it with a safe filename and updated layer names
for layer in model.layers:
    layer._name = layer.name.replace('/', '_')

# Save in the same .h5 format or the new .keras format
model.save("model/enhanced_cotton_disease_model_v2.h5")
# Or better:
# model.save("model/enhanced_cotton_disease_model.keras")
