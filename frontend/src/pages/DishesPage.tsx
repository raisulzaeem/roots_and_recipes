/**
 * Dishes List Page - Shows all available dishes
 */
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { dishesApi } from '../services/api';
import type { DishSummary } from '../types';
import Loading from '../components/Loading';
import ErrorMessage from '../components/ErrorMessage';

const DishesPage = () => {
  const { t } = useTranslation();
  const [dishes, setDishes] = useState<DishSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isFirstLoad, setIsFirstLoad] = useState(true);

  useEffect(() => {
    const fetchDishes = async () => {
      try {
        setLoading(true);
        const data = await dishesApi.getAll({ page: 1, page_size: 100 });
        setDishes(data.dishes);
        setIsFirstLoad(false);
      } catch (err) {
        setError('Failed to load dishes');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchDishes();
  }, []);

  if (loading) return <Loading fullScreen showColdStartMessage={isFirstLoad} />;
  if (error) return <ErrorMessage message={error} onRetry={() => window.location.reload()} />;

  return (
    <div className="bg-gray-50 dark:bg-gray-900 min-h-screen">
      {/* Header */}
      <section className="bg-gradient-to-r from-primary-600 to-primary-700 dark:from-primary-700 dark:to-primary-800 text-white py-16">
        <div className="container-custom text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            {t('nav.dishes')}
          </h1>
          <p className="text-xl text-primary-100">
            Explore {dishes.length} traditional Bangladeshi dishes
          </p>
        </div>
      </section>

      {/* Dishes Grid */}
      <section className="section-padding">
        <div className="container-custom">
          {dishes.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-gray-600 dark:text-gray-400 text-lg">
                No dishes available yet.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {dishes.map((dish) => (
                <Link
                  key={dish.id}
                  to={`/dishes/${dish.id}`}
                  className="card-interactive group"
                >
                  {/* Dish Image */}
                  <div className="relative h-48 overflow-hidden rounded-t-xl bg-gray-200 dark:bg-gray-700">
                    {dish.hero_image ? (
                      <img
                        src={dish.hero_image}
                        alt={dish.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                        onError={(e) => {
                          e.currentTarget.src = 'https://via.placeholder.com/400x300?text=🍛';
                        }}
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-6xl">
                        🍛
                      </div>
                    )}
                    
                    {/* Heat Level Badge */}
                    {dish.heat_level && (
                      <div className="absolute top-3 right-3 bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm px-3 py-1 rounded-full flex items-center space-x-1">
                        <span className="text-sm font-medium">
                          {'🌶️'.repeat(dish.heat_level)}
                        </span>
                      </div>
                    )}
                  </div>

                  {/* Dish Info */}
                  <div className="p-6">
                    <h3 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors">
                      {dish.name}
                    </h3>
                    
                    {dish.name_bn && (
                      <p className="text-sm text-gray-500 dark:text-gray-400 mb-3 font-hind">
                        {dish.name_bn}
                      </p>
                    )}

                    {/* Tags */}
                    <div className="flex flex-wrap gap-2">
                      {dish.dietary_type && (
                        <span className="badge-primary text-xs">
                          {dish.dietary_type}
                        </span>
                      )}
                      {dish.region && (
                        <span className="badge-secondary text-xs">
                          📍 {dish.region.name}
                        </span>
                      )}
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
};

export default DishesPage;
