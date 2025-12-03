# CottonAid React Frontend

Modern, responsive React-based frontend for the Cotton Disease Detection system.

## 🚀 Features

- **Modern UI**: Clean, responsive design built with React and Tailwind CSS
- **Drag & Drop Upload**: Easy image upload with preview
- **Real-time Predictions**: Instant disease detection with confidence scores
- **Dashboard**: View model metrics and prediction statistics
- **History**: Track recent predictions with localStorage
- **Accessibility**: WCAG compliant with keyboard navigation and ARIA labels
- **Mobile-First**: Fully responsive design for all devices

## 📋 Prerequisites

- Node.js 16+ and npm
- Flask backend running (see parent directory)

## 🛠️ Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` if needed:
   ```env
   VITE_API_BASE_URL=http://127.0.0.1:5000
   VITE_USE_JSON_API=true
   VITE_MAX_FILE_SIZE=16
   ```

## 🏃 Running the App

### Development Mode

```bash
npm run dev
```

The app will be available at `http://localhost:5173/`

### Production Build

```bash
npm run build
```

Build output will be in the `dist/` folder.

### Preview Production Build

```bash
npm run preview
```

## 🧪 Testing

### Run Unit Tests

```bash
npm test
```

### Run Tests with Coverage

```bash
npm run test:coverage
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── api/
│   │   └── client.js          # API client with fallback logic
│   ├── components/
│   │   ├── Navbar.jsx          # Navigation bar
│   │   ├── UploadCard.jsx      # Image upload component
│   │   ├── ResultCard.jsx      # Prediction results display
│   │   ├── History.jsx         # Prediction history
│   │   └── Toast.jsx           # Toast notifications
│   ├── pages/
│   │   ├── Home.jsx            # Main upload page
│   │   ├── Dashboard.jsx       # Model metrics dashboard
│   │   └── About.jsx           # About page
│   ├── utils/
│   │   └── storage.js          # localStorage utilities
│   ├── App.jsx                 # Main app component
│   ├── main.jsx                # Entry point
│   └── index.css               # Global styles
├── public/                     # Static assets
├── .env                        # Environment variables
├── .env.example                # Environment template
├── package.json                # Dependencies
├── vite.config.js              # Vite configuration
└── tailwind.config.js          # Tailwind configuration
```

## 🔌 API Integration

The frontend supports two modes:

### 1. JSON API Mode (Recommended)

Uses the `/api/predict` endpoint for JSON responses.

**Requirements**:
- Flask backend with `app_with_api.py` running
- `VITE_USE_JSON_API=true` in `.env`

**Benefits**:
- Full probability distributions
- Better error handling
- Cleaner data flow

### 2. HTML Fallback Mode

Falls back to the original `/predict` endpoint if JSON API is unavailable.

**How it works**:
- Submits form data to `/predict`
- Parses HTML response
- Extracts prediction data

## 🎨 Customization

### Styling

The app uses Tailwind CSS. Customize colors in `tailwind.config.js`:

```js
theme: {
  extend: {
    colors: {
      primary: {
        // Your custom colors
      },
    },
  },
}
```

### API Endpoint

Change the backend URL in `.env`:

```env
VITE_API_BASE_URL=http://your-backend-url:5000
```

## 🚢 Deployment

### Option 1: Serve with Flask (Integrated)

1. Build the React app:
   ```bash
   npm run build
   ```

2. Copy build to Flask static folder:
   ```bash
   # Windows
   xcopy /E /I dist ..\static\react

   # Linux/Mac
   cp -r dist ../static/react
   ```

3. Uncomment the React serving routes in `app_with_api.py`

4. Access at `http://127.0.0.1:5000/app`

### Option 2: Separate Deployment

Deploy React and Flask separately:

1. **React**: Deploy `dist/` to Netlify, Vercel, or any static host
2. **Flask**: Deploy backend to Heroku, AWS, or any Python host
3. **Configure CORS**: Update CORS settings in Flask to allow your React domain

## 🔧 Troubleshooting

### CORS Errors

If you see CORS errors in the browser console:

1. Make sure Flask backend has `flask-cors` installed:
   ```bash
   pip install flask-cors
   ```

2. Verify CORS is configured in Flask:
   ```python
   from flask_cors import CORS
   CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173"]}})
   ```

### API Connection Failed

1. Check Flask backend is running: `http://127.0.0.1:5000/api/health`
2. Verify `.env` has correct `VITE_API_BASE_URL`
3. Check browser console for error messages

### Build Errors

1. Clear node_modules and reinstall:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

2. Clear Vite cache:
   ```bash
   rm -rf node_modules/.vite
   ```

## 📝 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_BASE_URL` | `http://127.0.0.1:5000` | Flask backend URL |
| `VITE_USE_JSON_API` | `true` | Use JSON API endpoint |
| `VITE_MAX_FILE_SIZE` | `16` | Max upload size in MB |

## 🤝 Contributing

1. Follow the existing code style
2. Use ESLint and Prettier
3. Write tests for new components
4. Update documentation

## 📄 License

Same as parent project.

## 🆘 Support

For issues or questions:
- Check the troubleshooting section above
- Review the integration guide in `INTEGRATION.md`
- Open an issue on GitHub
