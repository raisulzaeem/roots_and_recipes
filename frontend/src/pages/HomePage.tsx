/**
 * Home Page - Main landing page with map, featured dishes, and filters
 */
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { dishesApi, regionsApi } from '../services/api';
import type { DishSummary, Region } from '../types';
import Loading from '../components/Loading';
import ErrorMessage from '../components/ErrorMessage';

const HomePage = () => {
  const { t } = useTranslation();
  const [dishes, setDishes] = useState<DishSummary[]>([]);
  const [regions, setRegions] = useState<Region[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isFirstLoad, setIsFirstLoad] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [dishesData, regionsData] = await Promise.all([
          dishesApi.getAll({ page: 1, page_size: 6 }),
          regionsApi.getAll(),
        ]);
        setDishes(dishesData.dishes);
        setRegions(regionsData);
        setIsFirstLoad(false);
      } catch (err) {
        setError('Failed to load data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <Loading fullScreen showColdStartMessage={isFirstLoad} />;
  if (error) return <ErrorMessage message={error} onRetry={() => window.location.reload()} />;

  return (
    <div className="bg-gray-50 dark:bg-gray-900">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-r from-primary-600 to-primary-700 dark:from-primary-700 dark:to-primary-800 text-white">
        <div className="container-custom section-padding text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6 animate-fade-in">
            {t('home.hero.title')}
          </h1>
          <p className="text-xl md:text-2xl mb-8 text-primary-100 max-w-3xl mx-auto animate-slide-up">
            {t('home.hero.subtitle')}
          </p>
          <Link
            to="#dishes"
            className="inline-block bg-white text-primary-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors shadow-lg animate-slide-up"
          >
            {t('home.hero.cta')}
          </Link>
        </div>
        <div className="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-gray-50 dark:from-gray-900 to-transparent"></div>
      </section>

      {/* Featured Dishes */}
      <section id="dishes" className="section-padding">
        <div className="container-custom">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('home.featured.title')}
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400">
              {t('home.featured.subtitle')}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {dishes.filter(dish => dish.id !== 2).map((dish) => (
              <Link
                key={dish.id}
                to={`/dishes/${dish.id}`}
                className="card-hover overflow-hidden"
              >
                <div className="aspect-video bg-gray-200 dark:bg-gray-700 relative">
                  {dish.hero_image ? (
                    <img
                      src={dish.hero_image}
                      alt={dish.name}
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <div className="flex items-center justify-center h-full text-6xl">
                      🍛
                    </div>
                  )}
                  {dish.heat_level !== undefined && (
                    <div className="absolute top-4 right-4 bg-white dark:bg-gray-800 px-3 py-1 rounded-full text-sm font-medium">
                      {'🌶️'.repeat(Math.max(1, dish.heat_level))}
                    </div>
                  )}
                </div>
                <div className="p-6">
                  <h3 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">
                    {dish.name}
                  </h3>
                  {dish.region && (
                    <p className="text-sm text-gray-600 dark:text-gray-400 mb-3">
                      📍 {dish.region.name}
                    </p>
                  )}
                  {dish.dietary_type && (
                    <span className="badge-primary capitalize">
                      {dish.dietary_type}
                    </span>
                  )}
                </div>
              </Link>
            ))}
          </div>

          <div className="text-center mt-12">
            <Link to="/dishes" className="btn-primary">
              {t('home.featured.viewAll')}
            </Link>
          </div>
        </div>
      </section>

      {/* Regions Preview */}
      <section className="section-padding bg-white dark:bg-gray-800">
        <div className="container-custom">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('home.map.title')}
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400">
              {t('home.map.subtitle')}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {regions.map((region) => (
              <div
                key={region.id}
                className="card p-6 text-center hover:shadow-xl transition-shadow"
              >
                <h3 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">
                  {region.name}
                </h3>
                <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
                  {region.description}
                </p>
                <div className="text-sm text-gray-500 dark:text-gray-500">
                  📍 {region.latitude.toFixed(4)}, {region.longitude.toFixed(4)}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-padding bg-gradient-to-r from-secondary-600 to-secondary-700 text-white">
        <div className="container-custom text-center">
          <h2 className="text-4xl font-bold mb-4">
            Start Your Culinary Journey
          </h2>
          <p className="text-xl mb-8 text-secondary-100 max-w-2xl mx-auto">
            Explore the rich heritage and flavors of Bangladesh, one dish at a time.
          </p>
          <Link to="/dishes" className="btn bg-white text-secondary-600 hover:bg-gray-100">
            Explore All Dishes
          </Link>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
