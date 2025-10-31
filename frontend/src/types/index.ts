/**
 * TypeScript type definitions for the application.
 */

// Region types
export interface Region {
  id: number;
  name: string;
  name_bn?: string;
  latitude: number;
  longitude: number;
  description?: string;
  description_de?: string;
  description_bn?: string;
}

// Ingredient types
export interface IngredientSummary {
  id: number;
  name: string;
  name_de?: string;
  name_bn?: string;
  image?: string;
}

export interface Ingredient extends IngredientSummary {
  flavor_notes?: string;
  flavor_notes_de?: string;
  flavor_notes_bn?: string;
  origin?: string;
  origin_de?: string;
  origin_bn?: string;
  description?: string;
  description_de?: string;
  description_bn?: string;
  substitutions?: string[];
  allergens?: string[];
}

// Occasion types
export interface OccasionSummary {
  id: number;
  name: string;
  name_de?: string;
  name_bn?: string;
}

export interface Occasion extends OccasionSummary {
  description?: string;
  description_de?: string;
  description_bn?: string;
  date_type: 'fixed' | 'seasonal' | 'lunar';
  month?: number;
  day?: number;
  season?: string;
}

// Gallery item type
export interface GalleryItem {
  url: string;
  type: 'image' | 'video';
  caption?: string;
  caption_de?: string;
  caption_bn?: string;
}

// Dish types
export interface DishSummary {
  id: number;
  name: string;
  name_de?: string;
  name_bn?: string;
  hero_image?: string;
  dietary_type?: 'vegetarian' | 'vegan' | 'pescatarian' | 'meat';
  heat_level?: number;
  region?: Region;
}

export interface Dish extends DishSummary {
  hero_video?: string;
  what_it_is?: string;
  what_it_is_de?: string;
  what_it_is_bn?: string;
  why_it_matters?: string;
  why_it_matters_de?: string;
  why_it_matters_bn?: string;
  how_its_made?: string;
  how_its_made_de?: string;
  how_its_made_bn?: string;
  taste_texture?: string;
  taste_texture_de?: string;
  taste_texture_bn?: string;
  how_we_eat_it?: string;
  how_we_eat_it_de?: string;
  how_we_eat_it_bn?: string;
  fun_facts?: string;
  fun_facts_de?: string;
  fun_facts_bn?: string;
  allergens?: string[];
  prep_time_minutes?: number;
  map_hint?: string;
  gallery?: GalleryItem[];
  ingredients: IngredientSummary[];
  occasions: OccasionSummary[];
}

// API response types
export interface DishListResponse {
  dishes: DishSummary[];
  total: number;
  page: number;
  page_size: number;
}

// Filter types
export interface DishFilters {
  page?: number;
  page_size?: number;
  region_id?: number;
  dietary_type?: string;
  heat_level?: number;
  occasion_id?: number;
}

// Theme type
export type Theme = 'light' | 'dark';

// Language type
export type Language = 'en' | 'de' | 'bn';
