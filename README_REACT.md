# Cotton Disease Detection - React Frontend Edition

Modern web application for detecting diseases in cotton plants using deep learning, now with a beautiful React frontend!

## 🌟 What's New

This project now includes a **modern React-based frontend** alongside the original Flask HTML interface:

- ✨ Modern, responsive UI with Tailwind CSS
- 📊 Enhanced dashboard with analytics
- 📱 Mobile-first design
- ♿ Accessibility compliant
- 🔄 Prediction history tracking
- 🎨 Professional, clean interface
- ⚡ Fast and smooth user experience

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Option 1: Automated Setup (Windows)

```bash
start_dev.bat
```

### Option 2: Automated Setup (Linux/Mac)

```bash
chmod +x start_dev.sh
./start_dev.sh
```

### Option 3: Manual Setup

**1. Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**2. Install frontend dependencies:**
```bash
cd frontend
npm install
cd ..
```

**3. Start Flask backend:**
```bash
python app_with_api.py
```

**4. Start React frontend (new terminal):**
```bash
cd frontend
npm run dev
```

**5. Open your browser:**
- Original HTML interface: http://127.0.0.1:5000/
- React frontend: http://localhost:5173/
- API health check: http://127.0.0.1:5000/api/health

## 📁 Project Structure

```
Cotton-Plant-Disease-Classification/
├── frontend/                    # React frontend application
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── api/                # API client
│   │   └── utils/              # Utilities
│   ├── public/                 # Static assets
│   └── package.json            # Frontend dependencies
├── templates/                   # Original Flask templates
├── static/                      # Static files
├── disease_classifier/          # ML model code
├── pest_predictor/             # Pest prediction module
├── model/                      # Trained models
├── uploads/                    # Uploaded images
├── app.py                      # Original Flask app
├── app_with_api.py            # Enhanced Flask app with JSON API
├── api_routes.py              # JSON API endpoints
├── requirements.txt           # Python dependencies
└── README_REACT.md            # This file
```

## 🎯 Features

### Original Features (Preserved)
- ✅ Disease detection using DenseNet121
- ✅ 6 disease classes detection
- ✅ High accuracy (~97%)
- ✅ Image upload and analysis
- ✅ Confidence scores

### New React Frontend Features
- ✨ Modern, responsive UI
- 📊 Dashboard with model metrics
- 📈 Prediction statistics
- 🕐 Prediction history
- 📱 Mobile-optimized
- ♿ Accessibility features
- 🎨 Professional design
- ⚡ Fast performance
- 🔔 Toast notifications
- 💾 Local storage for history

## 🔧 Technology Stack

### Backend
- Flask - Web framework
- TensorFlow/Keras - Deep learning
- DenseNet121 - CNN architecture
- OpenCV - Image processing
- NumPy - Numerical computing

### Frontend
- React 19 - UI framework
- Vite - Build tool
- Tailwind CSS - Styling
- React Router - Navigation
- Axios - HTTP client
- Lucide React - Icons

## 📖 Documentation

- **[Frontend README](frontend/README.md)** - Frontend setup and development
- **[Integration Guide](INTEGRATION.md)** - Backend integration details
- **[Demo Checklist](DEMO_CHECKLIST.md)** - Testing checklist
- **[Summary](REACT_FRONTEND_SUMMARY.md)** - Complete implementation summary

## 🎨 Screenshots

### React Frontend
- Modern upload interface with drag & drop
- Real-time prediction results
- Detailed probability distributions
- Responsive dashboard
- Prediction history panel

### Original HTML Interface
- Still fully functional at http://127.0.0.1:5000/
- No changes to existing functionality

## 🔌 API Endpoints

### Original Routes (Unchanged)
- `GET /` - HTML upload page
- `POST /predict` - HTML prediction
- `GET /uploads/<filename>` - Serve uploaded images

### New JSON API Routes (Optional)
- `GET /api/health` - Health check
- `POST /api/predict` - JSON prediction
- `GET /api/model/metadata` - Model information
- `GET /api/model/metrics` - Training metrics

## 🚢 Deployment

### Development
```bash
# Backend
python app_with_api.py

# Frontend
cd frontend && npm run dev
```

### Production - Integrated
```bash
# Build React
cd frontend
npm run build

# Copy to Flask
cp -r dist ../static/react

# Deploy Flask
python app_with_api.py
```

### Production - Separate
- Deploy React to Netlify/Vercel
- Deploy Flask to Heroku/AWS
- Configure CORS

See [INTEGRATION.md](INTEGRATION.md) for detailed deployment instructions.

## 🧪 Testing

### Frontend Tests
```bash
cd frontend
npm test
```

### Manual Testing
Use the [Demo Checklist](DEMO_CHECKLIST.md) for comprehensive testing.

## 🐛 Troubleshooting

### CORS Errors
```bash
pip install flask-cors
```

### API Not Found
Make sure you're using `app_with_api.py`:
```bash
python app_with_api.py
```

### Frontend Build Fails
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

See [INTEGRATION.md](INTEGRATION.md) for more troubleshooting tips.

## 📊 Detectable Diseases

1. **Aphids** - Insect pests
2. **Army Worm** - Caterpillar damage
3. **Bacterial Blight** - Bacterial infection
4. **Healthy** - No disease
5. **Powdery Mildew** - Fungal disease
6. **Target Spot** - Fungal disease

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

Same as the original project.

## 🙏 Credits

### Original Project
- [Original Repository](https://github.com/Sakshi053/Cotton-Plant-Disease-Classification-Web-Application)
- Myat Myint Zu Thin
- Prachi Gupta

### React Frontend
- Built with modern web technologies
- Designed for extensibility and maintainability

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review the troubleshooting section
3. Open an issue on GitHub

## 🎯 Next Steps

1. **Try it out**: Follow the Quick Start guide
2. **Explore features**: Use the Demo Checklist
3. **Deploy**: Choose your deployment strategy
4. **Extend**: Add new features easily

## 🌟 Highlights

- **Non-Breaking**: Original Flask app works unchanged
- **Modern**: Latest React and Tailwind CSS
- **Complete**: All features + enhancements
- **Documented**: Comprehensive guides
- **Tested**: Unit tests included
- **Production-Ready**: Optimized builds
- **Accessible**: WCAG compliant
- **Extensible**: Easy to add features

---

**Built with ❤️ for modern agriculture** 🌱

Enjoy your new Cotton Disease Detection system with a beautiful, modern interface!
