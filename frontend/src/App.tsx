/**
 * Main App component with routing
 */
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useTheme } from './hooks';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import DishesPage from './pages/DishesPage';
import DishDetailPage from './pages/DishDetailPage';
import IngredientDetailPage from './pages/IngredientDetailPage';
import NotFoundPage from './pages/NotFoundPage';

function App() {
  const { theme } = useTheme();

  return (
    <Router>
      <div className={`min-h-screen flex flex-col ${theme === 'dark' ? 'dark' : ''}`}>
        <Navbar />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/dishes" element={<DishesPage />} />
            <Route path="/dishes/:id" element={<DishDetailPage />} />
            <Route path="/ingredients" element={<Navigate to="/" replace />} />
            <Route path="/ingredients/:id" element={<IngredientDetailPage />} />
            <Route path="/occasions" element={<Navigate to="/" replace />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
