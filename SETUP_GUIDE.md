# 🚀 Roots & Recipes - Complete Setup Guide

This guide will help you get both the backend and frontend running locally.

## Prerequisites

- **Python 3.11+** installed
- **Node.js 18+** and npm installed
- **Git** (optional, for version control)

---

## 📦 Step 1: Backend Setup

### 1.1 Navigate to Backend Directory
```powershell
cd backend
```

### 1.2 Create Virtual Environment
```powershell
python -m venv venv
```

### 1.3 Activate Virtual Environment
```powershell
# Windows PowerShell
.\venv\Scripts\activate

# Or if you see execution policy errors:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\activate
```

### 1.4 Install Dependencies
```powershell
pip install -r requirements.txt
```

### 1.5 Initialize Database with Sample Data
```powershell
python -m app.init_db
```

You should see:
```
Creating database tables...
Loading sample data...
  Adding regions...
  Adding ingredients...
  Adding occasions...
  Adding dishes...
✓ Database initialized successfully!
  - 3 regions
  - 3 ingredients
  - 3 occasions
  - 3 dishes
```

### 1.6 Run the Backend Server
```powershell
uvicorn app.main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

✅ **Backend is now running!** Keep this terminal open.

---

## 🎨 Step 2: Frontend Setup

### 2.1 Open a NEW Terminal/PowerShell Window

### 2.2 Navigate to Frontend Directory
```powershell
cd frontend
```

### 2.3 Install Dependencies
```powershell
npm install
```

This will install all required packages including:
- React
- TypeScript
- Tailwind CSS
- React Router
- Axios
- i18next
- And more...

### 2.4 Run the Development Server
```powershell
npm run dev
```

The frontend will be available at:
- **App**: http://localhost:5173

✅ **Frontend is now running!**

---

## 🎉 Step 3: Test the Application

### 3.1 Open Your Browser
Navigate to: **http://localhost:5173**

### 3.2 What You Should See
1. **Home Page**: Hero section with "Discover the Stories Behind Bangladeshi Cuisine"
2. **Featured Dishes**: 3 sample dishes (Ilish Bhaja, Tehari, Khichuri)
3. **Regions**: 3 regions (Dhaka, Chittagong, Sylhet)

### 3.3 Test Navigation
- Click on a dish card to view details
- Click on an ingredient chip to view ingredient details
- Use the navigation menu to explore
- Try the dark mode toggle (moon/sun icon)
- Try the language selector (globe icon)

### 3.4 Test the API Directly
Visit http://localhost:8000/docs and try:
- `GET /api/dishes` - List all dishes
- `GET /api/dishes/1` - Get Ilish Bhaja details
- `GET /api/ingredients/1` - Get Mustard Oil details
- `GET /api/regions` - List all regions

---

## 🛠 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'fastapi'`
**Solution**: Make sure you activated the virtual environment:
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Problem**: Database already contains data
**Solution**: This is normal if you run `init_db.py` multiple times. The script skips initialization if data exists.

**Problem**: Port 8000 is already in use
**Solution**: Kill the process using port 8000 or use a different port:
```powershell
uvicorn app.main:app --reload --port 8001
```
Don't forget to update `frontend/.env` with the new port!

### Frontend Issues

**Problem**: `Cannot find module 'react'` or similar TypeScript errors
**Solution**: Install dependencies:
```powershell
npm install
```

**Problem**: Port 5173 is already in use
**Solution**: Vite will automatically use the next available port (5174, 5175, etc.)

**Problem**: API requests failing (CORS errors)
**Solution**: Make sure:
1. Backend is running on http://localhost:8000
2. Frontend `.env` file has: `VITE_API_BASE_URL=http://localhost:8000`
3. Restart the frontend dev server after changing `.env`

---

## 📚 Next Steps

### Add More Dishes
Edit `backend/app/data/sample_data.py` and add more dishes to the `DISHES` list, then re-run:
```powershell
python -m app.init_db
```

### Customize Styling
Edit `frontend/tailwind.config.js` to change colors, fonts, etc.

### Add Translations
Edit translation files:
- `frontend/src/i18n/locales/en.json` (English)
- `frontend/src/i18n/locales/de.json` (German)

### Add Images
Place images in `frontend/public/images/` and update the URLs in sample data.

### Deploy
- **Backend**: Deploy to Railway, Render, Heroku, or AWS
- **Frontend**: Deploy to Vercel, Netlify, or GitHub Pages

---

## 📝 Quick Reference

### Backend Commands
```powershell
cd backend
.\venv\Scripts\activate
python -m app.init_db          # Initialize database
uvicorn app.main:app --reload   # Run server
```

### Frontend Commands
```powershell
cd frontend
npm run dev      # Development server
npm run build    # Production build
npm run preview  # Preview production build
```

### URLs
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## 🎯 Project Structure Overview

```
roots_and_recipes/
├── backend/
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── data/           # Sample data
│   │   ├── config.py       # Configuration
│   │   ├── database.py     # Database setup
│   │   ├── init_db.py      # DB initialization
│   │   └── main.py         # FastAPI app
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API client
│   │   ├── hooks/          # Custom hooks
│   │   ├── i18n/           # Translations
│   │   ├── types/          # TypeScript types
│   │   └── utils/          # Utilities
│   ├── package.json
│   └── README.md
│
└── README.md               # Main README
```

---

## ❓ Need Help?

- Check the main **README.md** for feature details
- Check **backend/README.md** for API documentation
- Check **frontend/README.md** for frontend-specific info
- Visit API docs at http://localhost:8000/docs for interactive API testing

---

**Happy Cooking! 🍛**
