/**
 * Loading spinner component
 */
import { useTranslation } from 'react-i18next';
import { useEffect, useState } from 'react';

interface LoadingProps {
  fullScreen?: boolean;
  message?: string;
  showColdStartMessage?: boolean;
}

const Loading = ({ fullScreen = false, message, showColdStartMessage = false }: LoadingProps) => {
  const { t } = useTranslation();
  const [showWarmupMessage, setShowWarmupMessage] = useState(false);

  useEffect(() => {
    // Show warmup message after 3 seconds of loading
    const timer = setTimeout(() => {
      if (showColdStartMessage) {
        setShowWarmupMessage(true);
      }
    }, 3000);

    return () => clearTimeout(timer);
  }, [showColdStartMessage]);

  const content = (
    <div className="flex flex-col items-center justify-center space-y-4 px-4">
      <div className="loading-spinner text-primary-600 dark:text-primary-400"></div>
      <p className="text-gray-600 dark:text-gray-400 animate-pulse text-center">
        {message || t('common.loading')}
      </p>
      {showWarmupMessage && (
        <div className="mt-4 p-4 bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg max-w-md">
          <p className="text-sm text-blue-800 dark:text-blue-200 text-center">
            ☕ {t('common.serverWakingUp') || 'The server is waking up from sleep. This may take 30-60 seconds on the first visit.'}
          </p>
        </div>
      )}
    </div>
  );

  if (fullScreen) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
        {content}
      </div>
    );
  }

  return <div className="py-12">{content}</div>;
};

export default Loading;
