/**
 * Dish Detail Page - Full dish information with story, ingredients, and media
 * TODO: Implement full dish detail view with all sections
 */
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { ArrowLeft } from 'lucide-react';
import { dishesApi } from '../services/api';
import type { Dish } from '../types';
import Loading from '../components/Loading';
import ErrorMessage from '../components/ErrorMessage';

const DishDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const { t } = useTranslation();
  const [dish, setDish] = useState<Dish | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchDish = async () => {
      if (!id) return;
      try {
        setLoading(true);
        const data = await dishesApi.getById(parseInt(id));
        setDish(data);
      } catch (err) {
        setError('Failed to load dish');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchDish();
  }, [id]);

  if (loading) return <Loading fullScreen />;
  if (error) return <ErrorMessage message={error} onRetry={() => window.location.reload()} />;
  if (!dish) return <ErrorMessage message="Dish not found" />;

  return (
    <div className="bg-gray-50 dark:bg-gray-900 min-h-screen">
      {/* Hero Section */}
      <div className="relative h-96 bg-gray-200 dark:bg-gray-700">
        {dish.hero_image ? (
          <img
            src={dish.hero_image}
            alt={dish.name}
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="flex items-center justify-center h-full text-9xl">🍛</div>
        )}
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
        <Link
          to="/"
          className="absolute top-8 left-8 btn bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm"
        >
          <ArrowLeft size={20} />
          <span className="ml-2">{t('common.back')}</span>
        </Link>
        <div className="absolute bottom-0 left-0 right-0 p-8">
          <div className="container-custom">
            <h1 className="text-5xl font-bold text-white mb-2">{dish.name}</h1>
            {dish.region && (
              <p className="text-xl text-white/90">📍 {dish.region.name}</p>
            )}
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="container-custom section-padding">
        {/* What it is */}
        {dish.what_it_is && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.whatItIs')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              {dish.what_it_is}
            </p>
          </section>
        )}

        {/* Why it matters */}
        {dish.why_it_matters && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.whyItMatters')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              {dish.why_it_matters}
            </p>
          </section>
        )}

        {/* Ingredients */}
        {dish.ingredients && dish.ingredients.length > 0 && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.ingredients')}
            </h2>
            <div className="flex flex-wrap gap-3">
              {dish.ingredients.map((ingredient) => (
                <Link
                  key={ingredient.id}
                  to={`/ingredients/${ingredient.id}`}
                  className="badge-primary text-base px-4 py-2 hover:bg-primary-200 dark:hover:bg-primary-800 transition-colors"
                >
                  {ingredient.name}
                </Link>
              ))}
            </div>
          </section>
        )}

        {/* How it's made */}
        {dish.how_its_made && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.howItsMade')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-line">
              {dish.how_its_made}
            </p>
          </section>
        )}

        {/* Taste & Texture */}
        {dish.taste_texture && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.tasteTex')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              {dish.taste_texture}
            </p>
          </section>
        )}

        {/* How we eat it */}
        {dish.how_we_eat_it && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.howWeEatIt')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              {dish.how_we_eat_it}
            </p>
          </section>
        )}

        {/* Fun Facts */}
        {dish.fun_facts && (
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4">
              {t('dish.sections.funFacts')}
            </h2>
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-line">
              {dish.fun_facts}
            </p>
          </section>
        )}
      </div>
    </div>
  );
};

export default DishDetailPage;
