/**
 * Utility functions for the application.
 */

import type { Language } from '../types';

/**
 * Get localized field value based on current language
 */
export function getLocalizedField<T>(
  obj: T,
  fieldName: keyof T,
  language: Language
): string {
  if (language === 'en') {
    return (obj[fieldName] as string) || '';
  }
  
  const localizedFieldName = `${String(fieldName)}_${language}` as keyof T;
  return (obj[localizedFieldName] as string) || (obj[fieldName] as string) || '';
}

/**
 * Format heat level to descriptive text
 */
export function formatHeatLevel(level: number): string {
  if (level === 0) return 'Mild';
  if (level <= 2) return 'Medium';
  if (level <= 4) return 'Spicy';
  return 'Very Spicy';
}

/**
 * Get emoji for heat level
 */
export function getHeatEmoji(level: number): string {
  if (level === 0) return '🌱';
  if (level <= 2) return '🌶️';
  if (level <= 4) return '🌶️🌶️';
  return '🌶️🌶️🌶️';
}

/**
 * Format dietary type with emoji
 */
export function formatDietaryType(type: string): string {
  const types: Record<string, string> = {
    vegetarian: '🥬 Vegetarian',
    vegan: '🌱 Vegan',
    pescatarian: '🐟 Pescatarian',
    meat: '🍖 Meat',
  };
  return types[type.toLowerCase()] || type;
}

/**
 * Truncate text with ellipsis
 */
export function truncate(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength).trim() + '...';
}

/**
 * Format prep time
 */
export function formatPrepTime(minutes: number): string {
  if (minutes < 60) return `${minutes} min`;
  const hours = Math.floor(minutes / 60);
  const mins = minutes % 60;
  return mins > 0 ? `${hours}h ${mins}min` : `${hours}h`;
}

/**
 * Generate a shareable URL for a dish
 */
export function getShareUrl(dishId: number): string {
  return `${window.location.origin}/dishes/${dishId}`;
}

/**
 * Copy text to clipboard
 */
export async function copyToClipboard(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.error('Failed to copy:', err);
    return false;
  }
}

/**
 * Class name utility (like clsx)
 */
export function cn(...classes: (string | boolean | undefined | null)[]): string {
  return classes.filter(Boolean).join(' ');
}

/**
 * Debounce function
 */
export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

/**
 * Check if device is mobile
 */
export function isMobile(): boolean {
  return window.innerWidth < 768;
}

/**
 * Scroll to top smoothly
 */
export function scrollToTop(): void {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
