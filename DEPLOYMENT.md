# Render Deployment Guide

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
   DATABASE_URL=<Render PostgreSQL connection string>
   CORS_ORIGINS=https://rootsandspices.eu,https://www.rootsandspices.eu
   SECRET_KEY=<generate-random-string>
   DEBUG=False
   ```

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
