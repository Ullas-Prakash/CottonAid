/**
 * Local storage utilities for prediction history
 */

const HISTORY_KEY = 'cotton_disease_history';
const MAX_HISTORY_ITEMS = 20;

/**
 * Get prediction history from localStorage
 * @returns {Array} Array of prediction objects
 */
export const getHistory = () => {
  try {
    const history = localStorage.getItem(HISTORY_KEY);
    return history ? JSON.parse(history) : [];
  } catch (error) {
    console.error('Error reading history:', error);
    return [];
  }
};

/**
 * Add prediction to history
 * @param {Object} prediction - Prediction result to save
 */
export const addToHistory = (prediction) => {
  try {
    const history = getHistory();
    
    // Add new prediction at the beginning
    const newHistory = [
      {
        id: Date.now(),
        ...prediction,
        timestamp: prediction.timestamp || new Date().toISOString(),
      },
      ...history,
    ].slice(0, MAX_HISTORY_ITEMS); // Keep only last N items

    localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
    return newHistory;
  } catch (error) {
    console.error('Error saving to history:', error);
    return getHistory();
  }
};

/**
 * Clear all history
 */
export const clearHistory = () => {
  try {
    localStorage.removeItem(HISTORY_KEY);
  } catch (error) {
    console.error('Error clearing history:', error);
  }
};

/**
 * Remove specific item from history
 * @param {number} id - ID of item to remove
 */
export const removeFromHistory = (id) => {
  try {
    const history = getHistory();
    const newHistory = history.filter(item => item.id !== id);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
    return newHistory;
  } catch (error) {
    console.error('Error removing from history:', error);
    return getHistory();
  }
};

export default {
  getHistory,
  addToHistory,
  clearHistory,
  removeFromHistory,
};
