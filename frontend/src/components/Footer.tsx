/**
 * Footer component
 */
import { useTranslation } from 'react-i18next';

const Footer = () => {
  const { t } = useTranslation();
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-50 dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800">
      <div className="container-custom py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Brand */}
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <span className="text-3xl">🍛</span>
              <span className="text-xl font-bold text-primary-600 dark:text-primary-400">
                {t('app.title')}
              </span>
            </div>
            <p className="text-gray-600 dark:text-gray-400 mb-4">
              {t('footer.tagline')}
            </p>
            <p className="text-sm text-gray-500 dark:text-gray-500">
              {t('app.tagline')}
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-4">
              Quick Links
            </h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="/"
                  className="text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                >
                  {t('nav.home')}
                </a>
              </li>
              <li>
                <a
                  href="/dishes"
                  className="text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                >
                  {t('nav.dishes')}
                </a>
              </li>
              <li>
                <a
                  href="/ingredients"
                  className="text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                >
                  {t('nav.ingredients')}
                </a>
              </li>
              <li>
                <a
                  href="/occasions"
                  className="text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                >
                  {t('nav.occasions')}
                </a>
              </li>
            </ul>
          </div>

          {/* About */}
          <div>
            <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-4">
              About
            </h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm mb-4">
              Roots & Recipes celebrates the rich culinary heritage of Bangladesh
              through interactive storytelling and immersive experiences.
            </p>
            <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
              <span>{t('footer.madeWith')}</span>
            </div>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-800">
          <p className="text-center text-sm text-gray-500 dark:text-gray-500">
            {t('footer.copyright').replace('2025', currentYear.toString())}
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
