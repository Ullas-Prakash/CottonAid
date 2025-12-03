import { useState, useEffect } from 'react';
import { Clock, Trash2, Eye } from 'lucide-react';
import { getHistory, clearHistory, removeFromHistory } from '../utils/storage';

/**
 * Display prediction history from localStorage
 * @param {Function} onSelectResult - Callback when history item is clicked
 */
const History = ({ onSelectResult }) => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = () => {
    setHistory(getHistory());
  };

  const handleClearAll = () => {
    if (window.confirm('Are you sure you want to clear all history?')) {
      clearHistory();
      setHistory([]);
    }
  };

  const handleRemove = (id) => {
    removeFromHistory(id);
    loadHistory();
  };

  const handleView = (item) => {
    if (onSelectResult) {
      onSelectResult(item);
    }
  };

  if (history.length === 0) {
    return (
      <div className="card">
        <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center space-x-2">
          <Clock className="w-5 h-5" />
          <span>Recent Predictions</span>
        </h3>
        <p className="text-gray-500 text-center py-8">
          No predictions yet. Upload an image to get started!
        </p>
      </div>
    );
  }

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center space-x-2">
          <Clock className="w-5 h-5" />
          <span>Recent Predictions</span>
        </h3>
        <button
          onClick={handleClearAll}
          className="text-sm text-red-600 hover:text-red-700 font-medium"
        >
          Clear All
        </button>
      </div>

      <div className="space-y-3 max-h-96 overflow-y-auto">
        {history.map((item) => (
          <div
            key={item.id}
            className="border border-gray-200 rounded-lg p-3 hover:border-primary-300 hover:bg-primary-50 transition-all group"
          >
            <div className="flex items-start justify-between">
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-gray-800 truncate">
                  {item.label}
                </p>
                <p className="text-sm text-gray-600">
                  Confidence: {item.confidence}%
                </p>
                <p className="text-xs text-gray-500 mt-1">
                  {new Date(item.timestamp).toLocaleString()}
                </p>
              </div>
              
              <div className="flex items-center space-x-2 ml-2">
                <button
                  onClick={() => handleView(item)}
                  className="p-2 text-primary-600 hover:bg-primary-100 rounded-lg transition-colors"
                  aria-label="View details"
                  title="View details"
                >
                  <Eye className="w-4 h-4" />
                </button>
                <button
                  onClick={() => handleRemove(item.id)}
                  className="p-2 text-red-600 hover:bg-red-100 rounded-lg transition-colors opacity-0 group-hover:opacity-100"
                  aria-label="Remove"
                  title="Remove"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Confidence bar */}
            <div className="mt-2 w-full bg-gray-200 rounded-full h-1.5 overflow-hidden">
              <div
                className="bg-primary-500 h-full transition-all"
                style={{ width: `${item.confidence}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default History;
