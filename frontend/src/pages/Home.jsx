import { useState } from 'react';
import UploadCard from '../components/UploadCard';
import ResultCard from '../components/ResultCard';
import History from '../components/History';
import Toast from '../components/Toast';
import { predictDisease } from '../api/client';
import { addToHistory } from '../utils/storage';

/**
 * Home page - Main upload and prediction interface
 */
const Home = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [toast, setToast] = useState(null);

  /**
   * Handle image upload and prediction
   */
  const handleUpload = async (file) => {
    setLoading(true);
    setResult(null);
    setToast(null);

    try {
      const prediction = await predictDisease(file);
      
      // Add to history
      addToHistory(prediction);
      
      // Show result
      setResult(prediction);
      
      // Show success toast
      setToast({
        type: 'success',
        message: 'Image analyzed successfully!',
      });
    } catch (error) {
      console.error('Prediction error:', error);
      setToast({
        type: 'error',
        message: error.message || 'Failed to analyze image. Please try again.',
      });
    } finally {
      setLoading(false);
    }
  };

  /**
   * Start new prediction
   */
  const handleNewPrediction = () => {
    setResult(null);
    setToast(null);
  };

  /**
   * View result from history
   */
  const handleSelectHistory = (item) => {
    setResult(item);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Cotton Disease Detection
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Upload an image of a cotton leaf to detect diseases using advanced AI technology.
            Get instant results with confidence scores and recommendations.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main content */}
          <div className="lg:col-span-2 space-y-8">
            {!result ? (
              <UploadCard onUpload={handleUpload} loading={loading} />
            ) : (
              <ResultCard result={result} onNewPrediction={handleNewPrediction} />
            )}

            {/* Features */}
            {!result && (
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="card text-center">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <span className="text-2xl">🔬</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-2">
                    AI-Powered Analysis
                  </h3>
                  <p className="text-sm text-gray-600">
                    Advanced deep learning model trained on thousands of cotton disease images
                  </p>
                </div>

                <div className="card text-center">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <span className="text-2xl">⚡</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-2">
                    Instant Results
                  </h3>
                  <p className="text-sm text-gray-600">
                    Get disease predictions in seconds with detailed confidence scores
                  </p>
                </div>

                <div className="card text-center">
                  <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                    <span className="text-2xl">📊</span>
                  </div>
                  <h3 className="font-semibold text-gray-800 mb-2">
                    Detailed Insights
                  </h3>
                  <p className="text-sm text-gray-600">
                    View probability distributions and get actionable recommendations
                  </p>
                </div>
              </div>
            )}
          </div>

          {/* Sidebar */}
          <div className="lg:col-span-1">
            <History onSelectResult={handleSelectHistory} />
          </div>
        </div>

        {/* Supported diseases */}
        <div className="mt-12 card">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
            Detectable Diseases
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {[
              { name: 'Aphids', emoji: '🐛' },
              { name: 'Army Worm', emoji: '🐛' },
              { name: 'Bacterial Blight', emoji: '🦠' },
              { name: 'Healthy', emoji: '✅' },
              { name: 'Powdery Mildew', emoji: '🍄' },
              { name: 'Target Spot', emoji: '🎯' },
            ].map((disease) => (
              <div
                key={disease.name}
                className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg border border-gray-200"
              >
                <span className="text-2xl">{disease.emoji}</span>
                <span className="text-sm font-medium text-gray-700">
                  {disease.name}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Toast notifications */}
      {toast && (
        <Toast
          type={toast.type}
          message={toast.message}
          onClose={() => setToast(null)}
        />
      )}
    </div>
  );
};

export default Home;
