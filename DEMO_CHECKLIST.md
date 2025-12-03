# CottonAid React Frontend - Demo Checklist

Use this checklist to verify the React frontend is working correctly.

## 🚀 Setup Verification

### Backend Setup
- [ ] Flask backend is running on `http://127.0.0.1:5000`
- [ ] Can access original HTML interface at `http://127.0.0.1:5000/`
- [ ] Model file exists at `model/enhanced_model.h5`
- [ ] Dataset handler is working

### Frontend Setup
- [ ] Node.js and npm are installed (`node --version`, `npm --version`)
- [ ] Frontend dependencies installed (`cd frontend && npm install`)
- [ ] `.env` file exists in `frontend/` directory
- [ ] React dev server starts (`npm run dev`)
- [ ] Can access React app at `http://localhost:5173/`

### API Integration (if using JSON API)
- [ ] `flask-cors` is installed (`pip install flask-cors`)
- [ ] Using `app_with_api.py` or API routes added to `app.py`
- [ ] API health check works: `http://127.0.0.1:5000/api/health`
- [ ] No CORS errors in browser console

## 🧪 Functional Testing

### Home Page - Upload Flow

1. **Initial Load**
   - [ ] Page loads without errors
   - [ ] Navbar displays "CottonAid" brand
   - [ ] Upload card is visible
   - [ ] "Drag & drop" area is displayed
   - [ ] Tips section shows recommended image guidelines

2. **File Selection**
   - [ ] Click "Choose File" button opens file picker
   - [ ] Select a cotton leaf image (JPG/PNG)
   - [ ] Image preview appears after selection
   - [ ] File name and size are displayed
   - [ ] "Analyze Image" button appears

3. **Drag & Drop**
   - [ ] Drag an image file over the upload area
   - [ ] Upload area highlights when dragging
   - [ ] Drop image to upload
   - [ ] Preview appears correctly

4. **Prediction**
   - [ ] Click "Analyze Image" button
   - [ ] Loading spinner appears
   - [ ] Button shows "Analyzing..." text
   - [ ] Upload area is disabled during analysis

5. **Results Display**
   - [ ] Results card appears after prediction
   - [ ] Disease name is displayed prominently
   - [ ] Confidence percentage is shown
   - [ ] Confidence bar animates
   - [ ] Uploaded image is displayed
   - [ ] Status badge shows (High/Medium/Low Confidence)
   - [ ] Recommendations section appears
   - [ ] "Analyze Another Image" button works
   - [ ] "Download Result" button works

6. **Probability Distribution** (if JSON API enabled)
   - [ ] "All Disease Probabilities" section appears
   - [ ] All 6 disease classes are listed
   - [ ] Probability bars are displayed
   - [ ] Probabilities are sorted (highest first)
   - [ ] Percentages add up to ~100%

### History Panel

1. **First Prediction**
   - [ ] History panel shows "No predictions yet" initially
   - [ ] After first prediction, history item appears
   - [ ] Item shows disease name, confidence, and timestamp

2. **Multiple Predictions**
   - [ ] Upload and analyze 2-3 different images
   - [ ] All predictions appear in history
   - [ ] Most recent prediction is at the top
   - [ ] Each item has a confidence bar

3. **History Interactions**
   - [ ] Click eye icon to view past result
   - [ ] Result card updates with historical data
   - [ ] Hover over item to see delete button
   - [ ] Click delete to remove item
   - [ ] Click "Clear All" to remove all history
   - [ ] Confirmation dialog appears before clearing

4. **Persistence**
   - [ ] Refresh page
   - [ ] History is still present (localStorage)
   - [ ] Close and reopen browser
   - [ ] History persists across sessions

### Dashboard Page

1. **Navigation**
   - [ ] Click "Dashboard" in navbar
   - [ ] Dashboard page loads
   - [ ] URL changes to `/dashboard`

2. **Statistics Cards**
   - [ ] "Total Predictions" shows correct count
   - [ ] "Avg Confidence" shows calculated average
   - [ ] "Model Type" displays "DenseNet121"
   - [ ] "Disease Classes" shows "6"

3. **Model Information**
   - [ ] Model architecture is displayed
   - [ ] Input size shows "224x224 pixels"
   - [ ] Model path is shown
   - [ ] Training accuracy is displayed

4. **Disease Classes**
   - [ ] All 6 disease classes are listed
   - [ ] Each class has a class number
   - [ ] Names are properly formatted (spaces, not underscores)

5. **Prediction Distribution** (after making predictions)
   - [ ] Chart shows distribution of predictions
   - [ ] Bars show percentage of each disease
   - [ ] Most predicted disease is at top
   - [ ] Percentages are calculated correctly

### About Page

1. **Navigation**
   - [ ] Click "About" in navbar
   - [ ] About page loads
   - [ ] URL changes to `/about`

2. **Content**
   - [ ] Mission statement is displayed
   - [ ] Feature cards show (4 cards)
   - [ ] Technology stack is listed
   - [ ] All 6 detectable diseases are described
   - [ ] Contact links are present (GitHub, Email)

## 📱 Responsive Design Testing

### Desktop (1920x1080)
- [ ] Layout uses full width appropriately
- [ ] Navbar items are horizontal
- [ ] Upload and history are side-by-side
- [ ] All text is readable
- [ ] Images scale properly

### Tablet (768x1024)
- [ ] Layout adjusts for medium screens
- [ ] Navbar remains horizontal
- [ ] Upload and history stack vertically
- [ ] Touch targets are adequate
- [ ] No horizontal scrolling

### Mobile (375x667)
- [ ] Navbar shows hamburger menu
- [ ] Menu opens/closes correctly
- [ ] All content is accessible
- [ ] Upload area is touch-friendly
- [ ] Buttons are large enough
- [ ] Text is readable without zooming
- [ ] No content is cut off

## ♿ Accessibility Testing

### Keyboard Navigation
- [ ] Tab through all interactive elements
- [ ] Focus indicators are visible
- [ ] Enter/Space activates buttons
- [ ] Escape closes mobile menu
- [ ] No keyboard traps

### Screen Reader (if available)
- [ ] Images have alt text
- [ ] Buttons have descriptive labels
- [ ] Form inputs have labels
- [ ] ARIA labels are present
- [ ] Page structure is logical

### Color Contrast
- [ ] Text is readable on all backgrounds
- [ ] Links are distinguishable
- [ ] Buttons have sufficient contrast
- [ ] Status indicators are clear

## 🎨 Visual Testing

### Styling
- [ ] Colors match design (green primary theme)
- [ ] Fonts are consistent
- [ ] Spacing is uniform
- [ ] Borders and shadows are subtle
- [ ] Hover states work on all buttons
- [ ] Active states show on nav links

### Animations
- [ ] Loading spinner rotates smoothly
- [ ] Confidence bars animate on load
- [ ] Toast notifications fade in
- [ ] Page transitions are smooth
- [ ] No janky animations

### Icons
- [ ] All icons display correctly (Lucide React)
- [ ] Icons are properly sized
- [ ] Icons have appropriate colors
- [ ] Icons align with text

## 🔔 Notifications Testing

### Success Toast
- [ ] Upload an image successfully
- [ ] Green success toast appears
- [ ] Toast shows "Image analyzed successfully!"
- [ ] Toast auto-closes after 5 seconds
- [ ] Can manually close toast with X button

### Error Toast
- [ ] Try uploading invalid file (e.g., .txt)
- [ ] Red error toast appears
- [ ] Error message is descriptive
- [ ] Toast can be closed manually

### Warning Toast (if applicable)
- [ ] Yellow warning toast displays correctly
- [ ] Warning icon is shown

## 🔄 Error Handling

### Network Errors
- [ ] Stop Flask backend
- [ ] Try to upload image
- [ ] Error toast appears with helpful message
- [ ] App doesn't crash
- [ ] Can retry after backend restarts

### Invalid Files
- [ ] Upload non-image file (.txt, .pdf)
- [ ] Error message appears
- [ ] Upload area remains functional

### Large Files
- [ ] Try uploading file > 16MB
- [ ] Error message about file size appears
- [ ] Upload is prevented

### Missing Files
- [ ] Click "Analyze Image" without selecting file
- [ ] Appropriate error handling occurs

## 🚀 Performance Testing

### Load Times
- [ ] Initial page load < 2 seconds
- [ ] Navigation between pages is instant
- [ ] Image preview loads quickly
- [ ] Prediction completes in < 5 seconds

### Bundle Size
- [ ] Run `npm run build`
- [ ] Check dist/ folder size
- [ ] Main bundle < 500KB (gzipped)

### Memory
- [ ] Upload 10+ images
- [ ] Check browser memory usage
- [ ] No memory leaks
- [ ] History doesn't cause slowdown

## 🔧 Developer Experience

### Code Quality
- [ ] Run `npm run lint` - no errors
- [ ] Code is properly formatted
- [ ] Components are well-organized
- [ ] Comments explain complex logic

### Build Process
- [ ] `npm run build` completes successfully
- [ ] No build warnings
- [ ] `npm run preview` serves build correctly
- [ ] Build output is optimized

## 📊 Test Results Summary

**Date**: _______________  
**Tester**: _______________  
**Environment**: _______________

### Overall Status
- [ ] All critical features working
- [ ] No blocking issues
- [ ] Ready for production

### Issues Found
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Notes
_____________________________________________________
_____________________________________________________
_____________________________________________________

## ✅ Sign-off

- [ ] Frontend developer approval
- [ ] Backend integration verified
- [ ] User acceptance testing passed
- [ ] Documentation is complete

**Approved by**: _______________  
**Date**: _______________
