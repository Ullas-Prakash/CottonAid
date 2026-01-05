import { useState, useRef, useEffect } from 'react';
import { Camera, X, RotateCcw, Check } from 'lucide-react';

/**
 * Camera capture component for taking photos
 * @param {Function} onCapture - Callback when photo is captured with File object
 * @param {Function} onClose - Callback to close camera
 */
const CameraCapture = ({ onCapture, onClose }) => {
  const [stream, setStream] = useState(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [error, setError] = useState('');
  const [facingMode, setFacingMode] = useState('environment'); // 'user' for front, 'environment' for back
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  /**
   * Start camera stream
   */
  const startCamera = async () => {
    try {
      setError('');
      const mediaStream = await navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: facingMode,
          width: { ideal: 1280 },
          height: { ideal: 720 }
        }
      });
      
      setStream(mediaStream);
      if (videoRef.current) {
        videoRef.current.srcObject = mediaStream;
      }
    } catch (err) {
      console.error('Camera access error:', err);
      setError('Unable to access camera. Please check permissions.');
    }
  };

  /**
   * Stop camera stream
   */
  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
    }
  };

  /**
   * Capture photo from video stream
   */
  const capturePhoto = () => {
    if (!videoRef.current || !canvasRef.current) return;

    const video = videoRef.current;
    const canvas = canvasRef.current;
    
    // Set canvas dimensions to match video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    // Draw video frame to canvas
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Get image data URL
    const imageDataUrl = canvas.toDataURL('image/jpeg', 0.9);
    setCapturedImage(imageDataUrl);
    
    // Stop camera after capture
    stopCamera();
  };

  /**
   * Retake photo
   */
  const retakePhoto = () => {
    setCapturedImage(null);
    startCamera();
  };

  /**
   * Confirm and use captured photo
   */
  const usePhoto = () => {
    if (!capturedImage) return;

    // Convert data URL to Blob
    fetch(capturedImage)
      .then(res => res.blob())
      .then(blob => {
        // Create File object from Blob
        const file = new File(
          [blob],
          `camera-capture-${Date.now()}.jpg`,
          { type: 'image/jpeg' }
        );
        
        // Pass file to parent component
        onCapture(file);
        handleClose();
      })
      .catch(err => {
        console.error('Error converting image:', err);
        setError('Failed to process captured image');
      });
  };

  /**
   * Switch between front and back camera
   */
  const switchCamera = () => {
    stopCamera();
    setFacingMode(prev => prev === 'user' ? 'environment' : 'user');
  };

  /**
   * Close camera and cleanup
   */
  const handleClose = () => {
    stopCamera();
    onClose();
  };

  // Start camera on mount
  useEffect(() => {
    const initCamera = async () => {
      await startCamera();
    };
    initCamera();
    return () => stopCamera();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [facingMode]);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center p-4">
      <div className="relative w-full max-w-2xl bg-white rounded-xl overflow-hidden">
        {/* Header */}
        <div className="bg-gray-800 text-white p-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold flex items-center space-x-2">
            <Camera className="w-5 h-5" />
            <span>Camera Capture</span>
          </h3>
          <button
            onClick={handleClose}
            className="p-2 hover:bg-gray-700 rounded-lg transition-colors"
            aria-label="Close camera"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Camera view or captured image */}
        <div className="relative bg-black aspect-video">
          {!capturedImage ? (
            <>
              <video
                ref={videoRef}
                autoPlay
                playsInline
                muted
                className="w-full h-full object-cover"
              />
              <canvas ref={canvasRef} className="hidden" />
              
              {/* Camera controls overlay */}
              <div className="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black to-transparent">
                <div className="flex items-center justify-center space-x-4">
                  {/* Switch camera button */}
                  <button
                    onClick={switchCamera}
                    className="p-3 bg-white bg-opacity-20 hover:bg-opacity-30 rounded-full transition-all"
                    aria-label="Switch camera"
                  >
                    <RotateCcw className="w-6 h-6 text-white" />
                  </button>

                  {/* Capture button */}
                  <button
                    onClick={capturePhoto}
                    className="w-16 h-16 bg-white rounded-full border-4 border-gray-300 hover:scale-110 transition-transform"
                    aria-label="Capture photo"
                  >
                    <div className="w-full h-full rounded-full bg-white" />
                  </button>

                  {/* Spacer for symmetry */}
                  <div className="w-12" />
                </div>
              </div>
            </>
          ) : (
            <>
              <img
                src={capturedImage}
                alt="Captured"
                className="w-full h-full object-contain"
              />
              
              {/* Captured image controls */}
              <div className="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black to-transparent">
                <div className="flex items-center justify-center space-x-4">
                  {/* Retake button */}
                  <button
                    onClick={retakePhoto}
                    className="flex items-center space-x-2 px-6 py-3 bg-white bg-opacity-20 hover:bg-opacity-30 rounded-lg transition-all text-white font-semibold"
                  >
                    <RotateCcw className="w-5 h-5" />
                    <span>Retake</span>
                  </button>

                  {/* Use photo button */}
                  <button
                    onClick={usePhoto}
                    className="flex items-center space-x-2 px-6 py-3 bg-primary-600 hover:bg-primary-700 rounded-lg transition-all text-white font-semibold"
                  >
                    <Check className="w-5 h-5" />
                    <span>Use Photo</span>
                  </button>
                </div>
              </div>
            </>
          )}
        </div>

        {/* Error message */}
        {error && (
          <div className="p-4 bg-red-50 border-t border-red-200">
            <p className="text-sm text-red-700 text-center">{error}</p>
          </div>
        )}

        {/* Instructions */}
        {!capturedImage && !error && (
          <div className="p-4 bg-gray-50 border-t border-gray-200">
            <p className="text-sm text-gray-600 text-center">
              Position the cotton leaf in the frame and tap the capture button
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default CameraCapture;
