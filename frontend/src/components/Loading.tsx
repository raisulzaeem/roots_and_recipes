/**
 * Loading spinner component
 */
import { useTranslation } from 'react-i18next';

interface LoadingProps {
  fullScreen?: boolean;
  message?: string;
}

const Loading = ({ fullScreen = false, message }: LoadingProps) => {
  const { t } = useTranslation();

  const content = (
    <div className="flex flex-col items-center justify-center space-y-4">
      <div className="loading-spinner text-primary-600 dark:text-primary-400"></div>
      <p className="text-gray-600 dark:text-gray-400 animate-pulse">
        {message || t('common.loading')}
      </p>
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
