/**
 * Error message component
 */
import { useTranslation } from 'react-i18next';
import { AlertCircle } from 'lucide-react';

interface ErrorMessageProps {
  message?: string;
  onRetry?: () => void;
}

const ErrorMessage = ({ message, onRetry }: ErrorMessageProps) => {
  const { t } = useTranslation();

  return (
    <div className="py-12 px-4">
      <div className="max-w-md mx-auto text-center">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-red-100 dark:bg-red-900 mb-4">
          <AlertCircle className="w-8 h-8 text-red-600 dark:text-red-400" />
        </div>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
          {t('common.error')}
        </h3>
        <p className="text-gray-600 dark:text-gray-400 mb-6">
          {message || 'An unexpected error occurred'}
        </p>
        {onRetry && (
          <button onClick={onRetry} className="btn-primary">
            {t('common.tryAgain')}
          </button>
        )}
      </div>
    </div>
  );
};

export default ErrorMessage;
