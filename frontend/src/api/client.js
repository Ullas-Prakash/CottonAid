/**
 * API Client for Cotton Disease Detection
 * Handles communication with Flask backend with fallback support
 */

const API_BASE_URL = "https://cottonaid.onrender.com";
const USE_JSON_API = import.meta.env.VITE_USE_JSON_API === 'true';

/**
 * Check if JSON API endpoint is available
 */   
export const checkJsonApiAvailable = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/health`, {
      method: 'GET',
    });
    return response.ok;
  } catch {
    console.warn('JSON API not available, will use fallback');
    return false;
  }
};

/**
 * Predict disease from image using JSON API
 * @param {File} file - Image file to analyze
 * @returns {Promise<Object>} Prediction result
 */
export const predictDiseaseJSON = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch(`${API_BASE_URL}/api/predict`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Prediction failed');
    }

    const data = await response.json();
    return {
      success: true,
      label: data.label,
      confidence: data.confidence,
      probabilities: data.probabilities || [],
      imageUrl: data.image_url,
      preventive_measures: data.preventive_measures || [],
      causing_agents: data.causing_agents || [],
      timestamp: new Date().toISOString(),
    };
  } catch (error) {
    console.error('JSON API prediction error:', error);
    throw error;
  }
};

/**
 * Predict disease using HTML form submission (fallback)
 * @param {File} file - Image file to analyze
 * @returns {Promise<Object>} Prediction result
 */
export const predictDiseaseHTML = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Prediction failed');
    }

    // Parse HTML response to extract prediction data
    const html = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    // Extract label and confidence from HTML
    // This assumes the result.html template has specific structure
    const labelElement = doc.querySelector('[data-label]') || doc.querySelector('h2');
    const confidenceElement = doc.querySelector('[data-confidence]') || doc.querySelector('.confidence');
    const imageElement = doc.querySelector('img[src*="uploads"]');

    const label = labelElement?.textContent?.trim() || 'Unknown';
    const confidenceText = confidenceElement?.textContent?.trim() || '0';
    const confidence = parseFloat(confidenceText.replace('%', '')) || 0;
    const imageUrl = imageElement?.src || '';

    return {
      success: true,
      label,
      confidence,
      probabilities: [], // Not available in HTML response
      imageUrl,
      timestamp: new Date().toISOString(),
    };
  } catch (error) {
    console.error('HTML fallback prediction error:', error);
    throw error;
  }
};

/**
 * Main prediction function with automatic fallback
 * @param {File} file - Image file to analyze
 * @returns {Promise<Object>} Prediction result
 */
export const predictDisease = async (file) => {
  // Validate file
  if (!file) {
    throw new Error('No file provided');
  }

  const maxSize = (import.meta.env.VITE_MAX_FILE_SIZE || 16) * 1024 * 1024;
  if (file.size > maxSize) {
    throw new Error(`File size exceeds ${maxSize / 1024 / 1024}MB limit`);
  }

  // Try JSON API first if enabled
  if (USE_JSON_API) {
    try {
      return await predictDiseaseJSON(file);
    } catch {
      console.warn('JSON API failed, falling back to HTML endpoint');
      return await predictDiseaseHTML(file);
    }
  }

  // Use HTML fallback directly
  return await predictDiseaseHTML(file);
};

/**
 * Get model metadata
 * @returns {Promise<Object>} Model information
 */
export const getModelMetadata = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/model/metadata`);
    if (response.ok) {
      return await response.json();
    }
  } catch {
    console.warn('Model metadata not available');
  }

  // Return default metadata if endpoint doesn't exist
  return {
    model_name: 'DenseNet121',
    model_path: 'model/enhanced_model.h5',
    classes: [
      'Aphids',
      'Army_worm',
      'Bacterial_Blight',
      'Healthy',
      'Powdery_Mildew',
      'Target_spot'
    ],
    image_size: [224, 224],
    last_trained: 'Unknown',
  };
};

/**
 * Get training metrics (if available)
 * @returns {Promise<Object>} Training metrics
 */
export const getTrainingMetrics = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/model/metrics`);
    if (response.ok) {
      return await response.json();
    }
  } catch {
    console.warn('Training metrics not available');
  }

  return null;
};

export default {
  predictDisease,
  predictDiseaseJSON,
  predictDiseaseHTML,
  getModelMetadata,
  getTrainingMetrics,
  checkJsonApiAvailable,
};
