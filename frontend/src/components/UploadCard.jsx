import { useState, useRef } from 'react';
import { Upload, X, Image as ImageIcon, AlertCircle, Camera } from 'lucide-react';
import CameraCapture from './CameraCapture';

/**
 * Image upload component with drag & drop support
 * @param {Function} onUpload - Callback when file is selected
 * @param {boolean} loading - Whether upload is in progress
 */
const UploadCard = ({ onUpload, loading = false }) => {
  const [dragActive, setDragActive] = useState(false);
  const [preview, setPreview] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState('');
  const [showCamera, setShowCamera] = useState(false);
  const fileInputRef = useRef(null);

  const maxSize = (import.meta.env.VITE_MAX_FILE_SIZE || 16) * 1024 * 1024;
  const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];

  /**
   * Validate file before processing
   */
  const validateFile = (file) => {
    if (!file) {
      setError('Please select a file');
      return false;
    }

    if (!allowedTypes.includes(file.type)) {
      setError('Please upload a JPG, JPEG, or PNG image');
      return false;
    }

    if (file.size > maxSize) {
      setError(`File size must be less than ${maxSize / 1024 / 1024}MB`);
      return false;
    }

    setError('');
    return true;
  };

  /**
   * Handle file selection
   */
  const handleFile = (file) => {
    if (!validateFile(file)) {
      return;
    }

    setSelectedFile(file);

    // Create preview
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreview(reader.result);
    };
    reader.readAsDataURL(file);
  };

  /**
   * Handle drag events
   */
  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  /**
   * Handle drop event
   */
  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  /**
   * Handle file input change
   */
  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  /**
   * Clear selected file
   */
  const clearFile = () => {
    setSelectedFile(null);
    setPreview(null);
    setError('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  /**
   * Handle upload button click
   */
  const handleUpload = () => {
    if (selectedFile && onUpload) {
      onUpload(selectedFile);
    }
  };

  /**
   * Handle camera capture
   */
  const handleCameraCapture = (file) => {
    handleFile(file);
    setShowCamera(false);
  };

  return (
    <div className="card">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">
        Upload Cotton Leaf Image
      </h2>

      {/* Upload area */}
      <div
        className={`relative border-2 border-dashed rounded-xl p-8 text-center transition-all ${
          dragActive
            ? 'border-primary-500 bg-primary-50'
            : 'border-gray-300 hover:border-primary-400'
        } ${loading ? 'opacity-50 pointer-events-none' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        {!preview ? (
          <>
            <Upload className="w-16 h-16 mx-auto text-gray-400 mb-4" />
            <p className="text-lg font-semibold text-gray-700 mb-2">
              Drag & drop your image here
            </p>
            <p className="text-sm text-gray-500 mb-4">or</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
              <button
                type="button"
                onClick={() => fileInputRef.current?.click()}
                className="btn-primary flex items-center space-x-2"
                disabled={loading}
              >
                <Upload className="w-5 h-5" />
                <span>Choose File</span>
              </button>
              <button
                type="button"
                onClick={() => setShowCamera(true)}
                className="btn-secondary flex items-center space-x-2"
                disabled={loading}
              >
                <Camera className="w-5 h-5" />
                <span>Take Photo</span>
              </button>
            </div>
            <input
              ref={fileInputRef}
              type="file"
              className="hidden"
              accept="image/jpeg,image/jpg,image/png"
              onChange={handleChange}
              disabled={loading}
              aria-label="File upload"
            />
            <p className="text-xs text-gray-500 mt-4">
              Supported formats: JPG, JPEG, PNG (Max {maxSize / 1024 / 1024}MB)
            </p>
          </>
        ) : (
          <div className="fade-in">
            <div className="relative inline-block">
              <img
                src={preview}
                alt="Preview"
                className="max-h-64 rounded-lg shadow-md"
              />
              {!loading && (
                <button
                  onClick={clearFile}
                  className="absolute -top-2 -right-2 bg-red-500 hover:bg-red-600 text-white rounded-full p-2 shadow-lg transition-colors"
                  aria-label="Remove image"
                >
                  <X className="w-4 h-4" />
                </button>
              )}
            </div>
            <p className="text-sm text-gray-600 mt-4 font-medium">
              {selectedFile?.name}
            </p>
            <p className="text-xs text-gray-500">
              {(selectedFile?.size / 1024).toFixed(2)} KB
            </p>
          </div>
        )}
      </div>

      {/* Error message */}
      {error && (
        <div className="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg flex items-start space-x-2 fade-in">
          <AlertCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
          <p className="text-sm text-red-700">{error}</p>
        </div>
      )}

      {/* Upload button */}
      {preview && (
        <button
          onClick={handleUpload}
          disabled={loading || !selectedFile}
          className="btn-primary w-full mt-6 flex items-center justify-center space-x-2"
        >
          {loading ? (
            <>
              <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
              <span>Analyzing...</span>
            </>
          ) : (
            <>
              <ImageIcon className="w-5 h-5" />
              <span>Analyze Image</span>
            </>
          )}
        </button>
      )}

      {/* Info box */}
      <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
        <h3 className="font-semibold text-blue-900 mb-2 text-sm">
          📸 Tips for best results:
        </h3>
        <ul className="text-xs text-blue-800 space-y-1">
          <li>• Use clear, well-lit images</li>
          <li>• Focus on the affected leaf area</li>
          <li>• Avoid blurry or dark images</li>
          <li>• Recommended size: 224x224 pixels or larger</li>
        </ul>
      </div>

      {/* Camera Capture Modal */}
      {showCamera && (
        <CameraCapture
          onCapture={handleCameraCapture}
          onClose={() => setShowCamera(false)}
        />
      )}
    </div>
  );
};

export default UploadCard;
