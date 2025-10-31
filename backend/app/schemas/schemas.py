"""
Pydantic schemas for API request/response validation.
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


# ==================== Region Schemas ====================

class RegionBase(BaseModel):
    """Base region schema."""
    name: str
    name_bn: Optional[str] = None
    latitude: float
    longitude: float
    description: Optional[str] = None
    description_de: Optional[str] = None
    description_bn: Optional[str] = None


class Region(RegionBase):
    """Region schema with ID."""
    id: int
    
    class Config:
        from_attributes = True


# ==================== Ingredient Schemas ====================

class IngredientBase(BaseModel):
    """Base ingredient schema."""
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    image: Optional[str] = None
    flavor_notes: Optional[str] = None
    flavor_notes_de: Optional[str] = None
    flavor_notes_bn: Optional[str] = None
    origin: Optional[str] = None
    origin_de: Optional[str] = None
    origin_bn: Optional[str] = None
    description: Optional[str] = None
    description_de: Optional[str] = None
    description_bn: Optional[str] = None
    substitutions: Optional[List[str]] = []
    allergens: Optional[List[str]] = []


class IngredientSummary(BaseModel):
    """Simplified ingredient for dish listings."""
    id: int
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    image: Optional[str] = None
    
    class Config:
        from_attributes = True


class Ingredient(IngredientBase):
    """Full ingredient schema with ID."""
    id: int
    
    class Config:
        from_attributes = True


# ==================== Occasion Schemas ====================

class OccasionBase(BaseModel):
    """Base occasion schema."""
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    description: Optional[str] = None
    description_de: Optional[str] = None
    description_bn: Optional[str] = None
    date_type: str  # fixed, seasonal, lunar
    month: Optional[int] = None
    day: Optional[int] = None
    season: Optional[str] = None


class OccasionSummary(BaseModel):
    """Simplified occasion for dish listings."""
    id: int
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    
    class Config:
        from_attributes = True


class Occasion(OccasionBase):
    """Full occasion schema with ID."""
    id: int
    
    class Config:
        from_attributes = True


# ==================== Dish Schemas ====================

class GalleryItem(BaseModel):
    """Gallery item with media and caption."""
    url: str
    type: str  # image or video
    caption: Optional[str] = None
    caption_de: Optional[str] = None
    caption_bn: Optional[str] = None


class DishBase(BaseModel):
    """Base dish schema."""
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    hero_image: Optional[str] = None
    hero_video: Optional[str] = None
    dietary_type: Optional[str] = None
    heat_level: Optional[int] = Field(None, ge=0, le=5)
    what_it_is: Optional[str] = None
    what_it_is_de: Optional[str] = None
    what_it_is_bn: Optional[str] = None
    why_it_matters: Optional[str] = None
    why_it_matters_de: Optional[str] = None
    why_it_matters_bn: Optional[str] = None
    how_its_made: Optional[str] = None
    how_its_made_de: Optional[str] = None
    how_its_made_bn: Optional[str] = None
    taste_texture: Optional[str] = None
    taste_texture_de: Optional[str] = None
    taste_texture_bn: Optional[str] = None
    how_we_eat_it: Optional[str] = None
    how_we_eat_it_de: Optional[str] = None
    how_we_eat_it_bn: Optional[str] = None
    fun_facts: Optional[str] = None
    fun_facts_de: Optional[str] = None
    fun_facts_bn: Optional[str] = None
    allergens: Optional[List[str]] = []
    prep_time_minutes: Optional[int] = None
    map_hint: Optional[str] = None


class DishSummary(BaseModel):
    """Simplified dish for list views."""
    id: int
    name: str
    name_de: Optional[str] = None
    name_bn: Optional[str] = None
    hero_image: Optional[str] = None
    dietary_type: Optional[str] = None
    heat_level: Optional[int] = None
    region: Optional[Region] = None
    
    class Config:
        from_attributes = True


class Dish(DishBase):
    """Full dish schema with all relationships."""
    id: int
    region: Optional[Region] = None
    ingredients: List[IngredientSummary] = []
    occasions: List[OccasionSummary] = []
    gallery: Optional[List[Dict[str, Any]]] = []
    
    class Config:
        from_attributes = True


# ==================== API Response Schemas ====================

class DishListResponse(BaseModel):
    """Response for dish list endpoint."""
    dishes: List[DishSummary]
    total: int
    page: int
    page_size: int


class ErrorResponse(BaseModel):
    """Error response schema."""
    detail: str
