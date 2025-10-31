# Roots & Recipes 🍛

**"It's not just food, there's a story behind it."**

Roots & Recipes is a modern, interactive web application that explores Bangladeshi cuisine through immersive storytelling, interactive maps, and rich multimedia content. Discover the cultural heritage behind each dish, from Ilish to Tehari, through stories, videos, and interactive ingredient exploration.

## ✨ Features

- **Interactive Map**: Explore dishes by region using an interactive map interface
- **Immersive Detail Pages**: Rich storytelling with images, videos, and cultural context
- **Ingredient Explorer**: Deep dive into ingredients with flavor notes, origins, and substitutions
- **Occasions Timeline**: Discover dishes by cultural events and seasons
- **Dinner Mode**: Generate QR codes to share your menu with guests
- **Multilingual**: Support for English, German, and optional Bangla
- **Dark Mode**: Comfortable viewing in any lighting condition
- **Progressive Web App**: Offline support for selected dishes

## 🛠 Tech Stack

### Frontend
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **React Router v6** for navigation
- **MapLibre GL** for interactive maps
- **react-i18next** for internationalization
- **Vite** for fast development and building

### Backend
- **Python 3.11+**
- **FastAPI** for REST API
- **SQLAlchemy** for ORM
- **PostgreSQL** for data storage
- **Pydantic** for data validation
- **Uvicorn** as ASGI server

## 📁 Project Structure

```
roots_and_recipes/
├── frontend/                # React application
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API clients
│   │   ├── hooks/          # Custom React hooks
│   │   ├── i18n/           # Translation files
│   │   ├── types/          # TypeScript definitions
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   └── package.json
│
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   └── data/           # Sample data
│   ├── requirements.txt
│   └── main.py
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- **Node.js** 18+ and npm/yarn
- **Python** 3.11+
- **PostgreSQL** 14+

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the backend directory:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/roots_recipes
   CORS_ORIGINS=http://localhost:5173
   ```

5. **Initialize database**:
   ```bash
   python -m app.init_db
   ```

6. **Run the server**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   API will be available at: `http://localhost:8000`
   API docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**:
   Create a `.env` file in the frontend directory:
   ```env
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

   App will be available at: `http://localhost:5173`

## 📊 Sample Data

The application comes with sample data for:
- **3 Dishes**: Ilish Bhaja (Fried Hilsa), Tehari (Spiced Yellow Rice), Khichuri (Rice & Lentil Comfort)
- **3 Ingredients**: Mustard Oil, Green Chili, Hilsa Fish
- **Regions**: Dhaka, Chittagong, Sylhet

## 🌍 API Endpoints

- `GET /api/dishes` - List all dishes (with filters)
- `GET /api/dishes/{id}` - Get dish details
- `GET /api/ingredients/{id}` - Get ingredient details
- `GET /api/regions` - List all regions
- `GET /api/occasions` - List all occasions

## 🎨 Features in Detail

### Home Page
- Interactive map with regional dish pins
- Featured dishes carousel
- Filters for occasion, heat level, dietary preferences

### Dish Detail Page
- Hero image or video loop
- Story sections (What, Why, How, Taste, Pairing, Fun Facts)
- Interactive ingredient chips with modals
- Media gallery with captions
- Regional origin map inset

### Ingredient Detail Page
- High-quality ingredient images
- Flavor profile and tasting notes
- Origin and cultural significance
- Substitution suggestions
- Allergen information

### Dinner Mode (Coming Soon)
- QR code generation for menu sharing
- Guest reactions and feedback
- Offline caching for selected dishes

## 🌐 Internationalization

The app supports multiple languages:
- English (default)
- German (Deutsch)
- Bangla (বাংলা) - coming soon

Switch languages using the language selector in the navigation.

## 🎨 Dark Mode

Toggle between light and dark themes using the theme switcher in the navigation bar.

## 🧪 Development

### Running Tests

**Backend**:
```bash
cd backend
pytest
```

**Frontend**:
```bash
cd frontend
npm test
```

### Building for Production

**Frontend**:
```bash
cd frontend
npm run build
```

**Backend**:
The FastAPI app can be deployed using Docker, Gunicorn, or cloud platforms like Railway, Render, or AWS.

## 📝 License

MIT License - feel free to use this project for learning and personal projects.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Enjoy exploring the rich culinary heritage of Bangladesh! 🇧🇩**
