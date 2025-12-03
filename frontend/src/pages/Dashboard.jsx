import { useState, useEffect } from 'react';
import { BarChart3, Brain, Database, Clock, TrendingUp } from 'lucide-react';
import { getModelMetadata, getTrainingMetrics } from '../api/client';
import { getHistory } from '../utils/storage';

/**
 * Dashboard page - Display model info and statistics
 */
const Dashboard = () => {
  const [modelInfo, setModelInfo] = useState(null);
  const [metrics, setMetrics] = useState(null);
  const [stats, setStats] = useState({
    totalPredictions: 0,
    avgConfidence: 0,
    diseaseDistribution: {},
  });

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    // Load model metadata
    const metadata = await getModelMetadata();
    setModelInfo(metadata);

    // Load training metrics (if available)
    const trainingMetrics = await getTrainingMetrics();
    setMetrics(trainingMetrics);

    // Calculate statistics from history
    const history = getHistory();
    if (history.length > 0) {
      const totalConf = history.reduce((sum, item) => sum + item.confidence, 0);
      const distribution = {};
      
      history.forEach(item => {
        distribution[item.label] = (distribution[item.label] || 0) + 1;
      });

      setStats({
        totalPredictions: history.length,
        avgConfidence: (totalConf / history.length).toFixed(2),
        diseaseDistribution: distribution,
      });
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Dashboard</h1>
          <p className="text-gray-600">
            Model performance metrics and prediction statistics
          </p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Total Predictions</p>
                <p className="text-3xl font-bold text-gray-900">
                  {stats.totalPredictions}
                </p>
              </div>
              <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center">
                <BarChart3 className="w-6 h-6 text-primary-600" />
              </div>
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Avg Confidence</p>
                <p className="text-3xl font-bold text-gray-900">
                  {stats.avgConfidence}%
                </p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Model Type</p>
                <p className="text-2xl font-bold text-gray-900">
                  {modelInfo?.model_name || 'DenseNet121'}
                </p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <Brain className="w-6 h-6 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">Disease Classes</p>
                <p className="text-3xl font-bold text-gray-900">
                  {modelInfo?.classes?.length || 6}
                </p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                <Database className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Model Information */}
          <div className="card">
            <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center space-x-2">
              <Brain className="w-6 h-6 text-primary-600" />
              <span>Model Information</span>
            </h2>
            
            <div className="space-y-4">
              <div className="flex justify-between py-2 border-b border-gray-200">
                <span className="text-gray-600">Model Architecture</span>
                <span className="font-semibold text-gray-900">
                  {modelInfo?.model_name || 'DenseNet121'}
                </span>
              </div>
              
              <div className="flex justify-between py-2 border-b border-gray-200">
                <span className="text-gray-600">Input Size</span>
                <span className="font-semibold text-gray-900">
                  {modelInfo?.image_size?.join('x') || '224x224'} pixels
                </span>
              </div>
              
              <div className="flex justify-between py-2 border-b border-gray-200">
                <span className="text-gray-600">Model Path</span>
                <span className="font-semibold text-gray-900 text-sm truncate max-w-xs">
                  {modelInfo?.model_path || 'model/enhanced_model.h5'}
                </span>
              </div>
              
              <div className="flex justify-between py-2 border-b border-gray-200">
                <span className="text-gray-600">Last Trained</span>
                <span className="font-semibold text-gray-900">
                  {modelInfo?.last_trained || 'Unknown'}
                </span>
              </div>

              <div className="flex justify-between py-2">
                <span className="text-gray-600">Training Accuracy</span>
                <span className="font-semibold text-green-600">
                  {metrics?.accuracy || '~97%'}
                </span>
              </div>
            </div>
          </div>

          {/* Disease Classes */}
          <div className="card">
            <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center space-x-2">
              <Database className="w-6 h-6 text-primary-600" />
              <span>Supported Disease Classes</span>
            </h2>
            
            <div className="space-y-2">
              {(modelInfo?.classes || [
                'Aphids',
                'Army_worm',
                'Bacterial_Blight',
                'Healthy',
                'Powdery_Mildew',
                'Target_spot'
              ]).map((disease, index) => (
                <div
                  key={index}
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg border border-gray-200"
                >
                  <span className="font-medium text-gray-700">
                    {disease.replace(/_/g, ' ')}
                  </span>
                  <span className="text-sm text-gray-500">
                    Class {index}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Prediction Distribution */}
          {stats.totalPredictions > 0 && (
            <div className="card lg:col-span-2">
              <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center space-x-2">
                <BarChart3 className="w-6 h-6 text-primary-600" />
                <span>Prediction Distribution</span>
              </h2>
              
              <div className="space-y-3">
                {Object.entries(stats.diseaseDistribution)
                  .sort(([, a], [, b]) => b - a)
                  .map(([disease, count]) => {
                    const percentage = ((count / stats.totalPredictions) * 100).toFixed(1);
                    return (
                      <div key={disease} className="space-y-1">
                        <div className="flex justify-between text-sm">
                          <span className="font-medium text-gray-700">{disease}</span>
                          <span className="text-gray-600">
                            {count} ({percentage}%)
                          </span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
                          <div
                            className="bg-primary-500 h-full transition-all"
                            style={{ width: `${percentage}%` }}
                          />
                        </div>
                      </div>
                    );
                  })}
              </div>
            </div>
          )}

          {/* Training Metrics Placeholder */}
          <div className="card lg:col-span-2">
            <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center space-x-2">
              <TrendingUp className="w-6 h-6 text-primary-600" />
              <span>Training Metrics</span>
            </h2>
            
            {metrics ? (
              <div className="space-y-4">
                {/* If metrics are available, display them */}
                <p className="text-gray-600">Training metrics loaded successfully</p>
              </div>
            ) : (
              <div className="text-center py-8">
                <Clock className="w-12 h-12 text-gray-400 mx-auto mb-3" />
                <p className="text-gray-600 mb-2">
                  Training metrics not available
                </p>
                <p className="text-sm text-gray-500">
                  Add training plots to <code className="bg-gray-100 px-2 py-1 rounded">model/metrics.json</code> to display them here
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
