# Render Deployment Guide

## Prerequisites

### 1. Create PostgreSQL Database
1. In Render dashboard, click **New** → **PostgreSQL**
2. Name: `roots-recipes-db`
3. Database: `roots_recipes`
4. User: `roots_recipes`
5. Region: Same as your web service
6. Plan: **Free**
7. Click **Create Database**
8. Copy the **Internal Database URL** (starts with `postgresql://`)

## Backend Deployment

1. **Create Web Service** on Render
2. **Settings**:
   - Name: `roots-recipes-backend`
   - Environment: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Instance Type: `Free`

3. **Environment Variables**:
   ```
   DATABASE_URL=<Render PostgreSQL Internal Database URL from above>
   CORS_ORIGINS=https://rootsandrecipes.de,https://www.rootsandrecipes.de,https://roots-and-recipes-frontend.onrender.com,http://localhost:5173
   SECRET_KEY=<generate-random-string>
   DEBUG=False
   ```
   
   **Important**: Use the **Internal Database URL** from your PostgreSQL database, not the External URL.

## Database Initialization

After the first deployment:
1. Check the deploy logs - you should see "Database initialized successfully!"
2. If data wasn't loaded, you can manually trigger it:
   - Go to your Web Service → **Shell** tab
   - Run: `python -m app.init_db`
3. Verify data exists:
   - Visit: `https://roots-and-recipes.onrender.com/api/dishes`
   - Visit: `https://roots-and-recipes.onrender.com/api/ingredients`

## Frontend Deployment

1. **Create Static Site** on Render
2. **Settings**:
   - Name: `roots-recipes-frontend`
   - Build Command: `npm run build`
   - Publish Directory: `dist`
   - Instance Type: `Free`

3. **Environment Variables**:
   ```
   VITE_API_BASE_URL=https://roots-recipes-backend.onrender.com
   ```

## Custom Domain

In Render dashboard:
- Go to your static site → Settings → Custom Domain
- Add: `rootsandspices.eu`
- Follow DNS instructions for IONOS
