# React Frontend Integration Guide

This guide explains how to integrate the React frontend with your existing Flask backend.

## 📖 Overview

The React frontend is designed to work alongside your existing Flask application **without breaking any current functionality**. You have two options:

1. **Add JSON API** (Recommended): Add new API endpoints while keeping original routes
2. **Use as-is**: React frontend works with existing HTML endpoints via fallback

## 🎯 Quick Start (5 minutes)

### Step 1: Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Step 2: Install Flask CORS (for JSON API)

```bash
pip install flask-cors
```

### Step 3: Choose Your Integration Method

#### Option A: With JSON API (Recommended)

Replace `app.py` with `app_with_api.py`:

```bash
# Backup original
cp app.py app_original.py

# Use enhanced version
cp app_with_api.py app.py
```

#### Option B: Without JSON API

No changes needed! React will use HTML fallback mode.

### Step 4: Start Both Servers

**Terminal 1 - Flask Backend**:
```bash
python app.py
```

**Terminal 2 - React Frontend**:
```bash
cd frontend
npm run dev
```

### Step 5: Test

- Flask HTML interface: http://127.0.0.1:5000/
- React frontend: http://localhost:5173/
- API health check: http://127.0.0.1:5000/api/health

## 🔧 Detailed Integration

### Method 1: Add JSON API (Recommended)

This method adds new `/api/*` routes without touching existing routes.

#### What Gets Added:

- `GET /api/health` - Health check
- `POST /api/predict` - JSON prediction endpoint
- `GET /api/model/metadata` - Model information
- `GET /api/model/metrics` - Training metrics

#### Implementation:

1. **Use the enhanced app**:
   ```python
   # app_with_api.py is already configured
   # Just rename it to app.py or import from it
   ```

2. **Or manually add to your existing app.py**:
   ```python
   from flask_cors import CORS
   from api_routes import init_api

   # After creating Flask app
   CORS(app, resources={
       r"/api/*": {
           "origins": ["http://localhost:5173"],
           "methods": ["GET", "POST"]
       }
   })

   # After loading model and handler
   init_api(app, model, handler)
   ```

#### Verify It Works:

```bash
# Test health endpoint
curl http://127.0.0.1:5000/api/health

# Test prediction (with an image file)
curl -X POST -F "file=@test_image.jpg" http://127.0.0.1:5000/api/predict
```

### Method 2: HTML Fallback Only

No backend changes needed! The React frontend will:

1. Try to call `/api/predict`
2. If it fails, fall back to `/predict` (HTML endpoint)
3. Parse the HTML response to extract prediction data

#### Configuration:

In `frontend/.env`:
```env
VITE_USE_JSON_API=false
```

#### Limitations:

- No probability distributions (only top prediction)
- Slower (HTML parsing overhead)
- Less robust error handling

## 🚀 Production Deployment

### Option 1: Integrated (React + Flask Together)

Serve React build from Flask:

1. **Build React**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Copy to Flask static folder**:
   ```bash
   # Windows
   xcopy /E /I frontend\dist static\react

   # Linux/Mac
   cp -r frontend/dist static/react
   ```

3. **Add route to Flask** (in `app_with_api.py`):
   ```python
   @app.route('/app')
   @app.route('/app/<path:path>')
   def serve_react(path=''):
       if path and os.path.exists(os.path.join('static/react', path)):
           return send_from_directory('static/react', path)
       return send_from_directory('static/react', 'index.html')
   ```

4. **Access**:
   - Original interface: `http://your-domain.com/`
   - React interface: `http://your-domain.com/app`

### Option 2: Separate Deployment

Deploy React and Flask independently:

#### Deploy React:

**Netlify**:
```bash
cd frontend
npm run build
# Upload dist/ folder to Netlify
```

**Vercel**:
```bash
cd frontend
vercel deploy
```

#### Deploy Flask:

**Heroku**:
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Update CORS:

In Flask, allow your React domain:
```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-react-app.netlify.app"],
        "methods": ["GET", "POST"]
    }
})
```

#### Update React Config:

In `frontend/.env`:
```env
VITE_API_BASE_URL=https://your-flask-app.herokuapp.com
```

## 🔄 Migration Strategy

### Phase 1: Parallel Running (Recommended)

Run both interfaces side-by-side:

- Keep original HTML interface at `/`
- Add React interface at `/app`
- Users can choose which to use
- Gather feedback

### Phase 2: Gradual Migration

1. Make React the default (`/` → React, `/legacy` → HTML)
2. Monitor for issues
3. Keep HTML as fallback

### Phase 3: Full Migration

1. Remove HTML templates (optional)
2. React becomes the only interface
3. Keep API endpoints for future integrations

## 🧪 Testing Checklist

### Backend Testing:

- [ ] Original `/` route still works
- [ ] Original `/predict` route still works
- [ ] `/api/health` returns 200
- [ ] `/api/predict` accepts images and returns JSON
- [ ] CORS headers are present in API responses

### Frontend Testing:

- [ ] Upload page loads
- [ ] Image upload works (drag & drop and file picker)
- [ ] Prediction returns results
- [ ] Results display correctly
- [ ] History saves and loads
- [ ] Dashboard shows model info
- [ ] Mobile responsive
- [ ] Keyboard navigation works

### Integration Testing:

```bash
# Test with curl
curl -X POST -F "file=@test_cotton_leaf.jpg" \
  http://127.0.0.1:5000/api/predict

# Expected response:
{
  "success": true,
  "label": "Healthy",
  "confidence": 95.5,
  "probabilities": [...],
  "image_url": "http://127.0.0.1:5000/uploads/test_cotton_leaf.jpg"
}
```

## 🐛 Common Issues

### Issue: CORS Error

**Symptom**: Browser console shows "CORS policy" error

**Solution**:
```bash
pip install flask-cors
```

Add to Flask:
```python
from flask_cors import CORS
CORS(app)
```

### Issue: API Not Found

**Symptom**: 404 on `/api/predict`

**Solution**: Make sure you're using `app_with_api.py` or have added the API routes

### Issue: Image Not Displaying

**Symptom**: Prediction works but image doesn't show

**Solution**: Check CORS allows the `/uploads/` route:
```python
CORS(app, resources={
    r"/api/*": {"origins": "*"},
    r"/uploads/*": {"origins": "*"}
})
```

### Issue: Build Fails

**Symptom**: `npm run build` errors

**Solution**:
```bash
rm -rf node_modules package-lock.json
npm install
npm run build
```

## 📊 Performance Optimization

### Frontend:

1. **Enable gzip compression** in Flask:
   ```python
   from flask_compress import Compress
   Compress(app)
   ```

2. **Add caching headers**:
   ```python
   @app.after_request
   def add_header(response):
       if 'static' in request.path:
           response.cache_control.max_age = 31536000
       return response
   ```

3. **Lazy load images**:
   Already implemented in React components

### Backend:

1. **Use production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app
   ```

2. **Enable model caching**:
   Model is loaded once at startup (already implemented)

## 🔐 Security Considerations

### Production Checklist:

- [ ] Disable Flask debug mode (`debug=False`)
- [ ] Set specific CORS origins (not `*`)
- [ ] Add file upload validation
- [ ] Implement rate limiting
- [ ] Use HTTPS in production
- [ ] Sanitize file names
- [ ] Add authentication (if needed)

### Example Security Config:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/predict', methods=['POST'])
@limiter.limit("10 per minute")
def api_predict():
    # ... prediction code
```

## 📚 Additional Resources

- [Flask CORS Documentation](https://flask-cors.readthedocs.io/)
- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html)
- [React Router Documentation](https://reactrouter.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 🆘 Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review the frontend README.md
3. Check browser console for errors
4. Check Flask logs for backend errors
5. Open an issue with:
   - Error message
   - Steps to reproduce
   - Environment details (OS, Node version, Python version)

## 📝 Summary

**Minimum changes to get started**:
1. `pip install flask-cors`
2. Use `app_with_api.py` instead of `app.py`
3. `cd frontend && npm install && npm run dev`

**Zero backend changes option**:
1. Set `VITE_USE_JSON_API=false` in `frontend/.env`
2. `cd frontend && npm install && npm run dev`

Both your original Flask app and the new React frontend will work perfectly! 🎉
