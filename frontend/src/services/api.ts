/**
 * API client for Roots & Recipes backend.
 */
import axios from 'axios';
import type {
  Dish,
  DishListResponse,
  DishFilters,
  Ingredient,
  Region,
  Occasion,
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Dishes API
export const dishesApi = {
  /**
   * Get list of dishes with optional filters
   */
  async getAll(filters?: DishFilters): Promise<DishListResponse> {
    const response = await api.get<DishListResponse>('/api/dishes', { params: filters });
    return response.data;
  },

  /**
   * Get a single dish by ID
   */
  async getById(id: number): Promise<Dish> {
    const response = await api.get<Dish>(`/api/dishes/${id}`);
    return response.data;
  },

  /**
   * Get ingredients for a specific dish
   */
  async getIngredients(id: number): Promise<Ingredient[]> {
    const response = await api.get<Ingredient[]>(`/api/dishes/${id}/ingredients`);
    return response.data;
  },
};

// Ingredients API
export const ingredientsApi = {
  /**
   * Get list of all ingredients
   */
  async getAll(skip = 0, limit = 100): Promise<Ingredient[]> {
    const response = await api.get<Ingredient[]>('/api/ingredients', {
      params: { skip, limit },
    });
    return response.data;
  },

  /**
   * Get a single ingredient by ID
   */
  async getById(id: number): Promise<Ingredient> {
    const response = await api.get<Ingredient>(`/api/ingredients/${id}`);
    return response.data;
  },

  /**
   * Get dishes that use a specific ingredient
   */
  async getDishes(id: number): Promise<Dish[]> {
    const response = await api.get<Dish[]>(`/api/ingredients/${id}/dishes`);
    return response.data;
  },
};

// Regions API
export const regionsApi = {
  /**
   * Get list of all regions
   */
  async getAll(): Promise<Region[]> {
    const response = await api.get<Region[]>('/api/regions');
    return response.data;
  },

  /**
   * Get a single region by ID
   */
  async getById(id: number): Promise<Region> {
    const response = await api.get<Region>(`/api/regions/${id}`);
    return response.data;
  },

  /**
   * Get dishes from a specific region
   */
  async getDishes(id: number): Promise<Dish[]> {
    const response = await api.get<Dish[]>(`/api/regions/${id}/dishes`);
    return response.data;
  },
};

// Occasions API
export const occasionsApi = {
  /**
   * Get list of all occasions
   */
  async getAll(): Promise<Occasion[]> {
    const response = await api.get<Occasion[]>('/api/occasions');
    return response.data;
  },

  /**
   * Get a single occasion by ID
   */
  async getById(id: number): Promise<Occasion> {
    const response = await api.get<Occasion>(`/api/occasions/${id}`);
    return response.data;
  },

  /**
   * Get dishes for a specific occasion
   */
  async getDishes(id: number): Promise<Dish[]> {
    const response = await api.get<Dish[]>(`/api/occasions/${id}/dishes`);
    return response.data;
  },
};

export default api;
