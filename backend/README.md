# Roots & Recipes Backend

FastAPI backend for the Roots & Recipes application.

## Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database with sample data**:
   ```bash
   python -m app.init_db
   ```

4. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

   Or:
   ```bash
   python main.py
   ```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

- `GET /api/dishes` - List dishes with filters
- `GET /api/dishes/{id}` - Get dish details
- `GET /api/ingredients/{id}` - Get ingredient details
- `GET /api/regions` - List all regions
- `GET /api/occasions` - List all occasions

## Database

By default, the application uses SQLite for easy setup. The database file is created as `roots_recipes.db` in the backend directory.

To use PostgreSQL instead, update the `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/roots_recipes
```
