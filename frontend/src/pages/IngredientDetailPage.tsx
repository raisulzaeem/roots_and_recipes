/**
 * Ingredient Detail Page - Full ingredient information
 * TODO: Implement full ingredient detail view
 */
import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { ArrowLeft } from 'lucide-react';
import { ingredientsApi } from '../services/api';
import type { Ingredient } from '../types';
import Loading from '../components/Loading';
import ErrorMessage from '../components/ErrorMessage';

const IngredientDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const { t } = useTranslation();
  const [ingredient, setIngredient] = useState<Ingredient | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchIngredient = async () => {
      if (!id) return;
      try {
        setLoading(true);
        const data = await ingredientsApi.getById(parseInt(id));
        setIngredient(data);
      } catch (err) {
        setError('Failed to load ingredient');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchIngredient();
  }, [id]);

  if (loading) return <Loading fullScreen />;
  if (error) return <ErrorMessage message={error} onRetry={() => window.location.reload()} />;
  if (!ingredient) return <ErrorMessage message="Ingredient not found" />;

  return (
    <div className="bg-gray-50 dark:bg-gray-900 min-h-screen">
      <div className="container-custom section-padding">
        <Link to="/" className="inline-flex items-center btn-ghost mb-8">
          <ArrowLeft size={20} />
          <span className="ml-2">{t('common.back')}</span>
        </Link>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          {/* Image */}
          <div className="aspect-square bg-gray-200 dark:bg-gray-700 rounded-xl overflow-hidden">
            {ingredient.image ? (
              <img
                src={ingredient.image}
                alt={ingredient.name}
                className="w-full h-full object-cover"
              />
            ) : (
              <div className="flex items-center justify-center h-full text-9xl">
                🌿
              </div>
            )}
          </div>

          {/* Info */}
          <div>
            <h1 className="text-5xl font-bold text-gray-900 dark:text-gray-100 mb-6">
              {ingredient.name}
            </h1>

            {ingredient.description && (
              <p className="text-lg text-gray-700 dark:text-gray-300 mb-8 leading-relaxed">
                {ingredient.description}
              </p>
            )}

            {ingredient.flavor_notes && (
              <div className="mb-8">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-3">
                  {t('ingredient.flavorNotes')}
                </h2>
                <p className="text-gray-700 dark:text-gray-300">
                  {ingredient.flavor_notes}
                </p>
              </div>
            )}

            {ingredient.origin && (
              <div className="mb-8">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-3">
                  {t('ingredient.origin')}
                </h2>
                <p className="text-gray-700 dark:text-gray-300">
                  {ingredient.origin}
                </p>
              </div>
            )}

            {ingredient.substitutions && ingredient.substitutions.length > 0 && (
              <div className="mb-8">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-3">
                  {t('ingredient.substitutions')}
                </h2>
                <ul className="list-disc list-inside text-gray-700 dark:text-gray-300">
                  {ingredient.substitutions.map((sub, index) => (
                    <li key={index}>{sub}</li>
                  ))}
                </ul>
              </div>
            )}

            {ingredient.allergens && ingredient.allergens.length > 0 && (
              <div>
                <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-3">
                  {t('ingredient.allergens')}
                </h2>
                <div className="flex flex-wrap gap-2">
                  {ingredient.allergens.map((allergen, index) => (
                    <span key={index} className="badge bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">
                      {allergen}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default IngredientDetailPage;
