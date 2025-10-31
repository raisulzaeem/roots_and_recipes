"""
SQLAlchemy database models for Roots & Recipes.
"""
from sqlalchemy import Column, Integer, String, Float, Text, JSON, ForeignKey, Table
from sqlalchemy.orm import relationship
from ..database import Base

# Association table for many-to-many relationship between dishes and ingredients
dish_ingredients = Table(
    'dish_ingredients',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)

# Association table for many-to-many relationship between dishes and occasions
dish_occasions = Table(
    'dish_occasions',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id'), primary_key=True),
    Column('occasion_id', Integer, ForeignKey('occasions.id'), primary_key=True)
)


class Region(Base):
    """Geographic region model."""
    __tablename__ = "regions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    name_bn = Column(String)  # Bengali name
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(Text)
    description_de = Column(Text)  # German translation
    description_bn = Column(Text)  # Bengali translation
    
    # Relationships
    dishes = relationship("Dish", back_populates="region")


class Dish(Base):
    """Dish model with full details and relationships."""
    __tablename__ = "dishes"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic info
    name = Column(String, nullable=False, index=True)
    name_de = Column(String)  # German translation
    name_bn = Column(String)  # Bengali translation
    
    # Media
    hero_image = Column(String)  # URL or path to hero image
    hero_video = Column(String)  # URL or path to hero video
    gallery = Column(JSON)  # List of image/video URLs with captions
    
    # Classification
    region_id = Column(Integer, ForeignKey('regions.id'))
    dietary_type = Column(String)  # vegetarian, vegan, pescatarian, meat
    heat_level = Column(Integer)  # 0-5 scale
    
    # Story sections (with translations)
    what_it_is = Column(Text)
    what_it_is_de = Column(Text)
    what_it_is_bn = Column(Text)
    
    why_it_matters = Column(Text)
    why_it_matters_de = Column(Text)
    why_it_matters_bn = Column(Text)
    
    how_its_made = Column(Text)
    how_its_made_de = Column(Text)
    how_its_made_bn = Column(Text)
    
    taste_texture = Column(Text)
    taste_texture_de = Column(Text)
    taste_texture_bn = Column(Text)
    
    how_we_eat_it = Column(Text)
    how_we_eat_it_de = Column(Text)
    how_we_eat_it_bn = Column(Text)
    
    fun_facts = Column(Text)
    fun_facts_de = Column(Text)
    fun_facts_bn = Column(Text)
    
    # Additional metadata
    allergens = Column(JSON)  # List of allergens
    prep_time_minutes = Column(Integer)
    map_hint = Column(String)  # Additional location context
    
    # Relationships
    region = relationship("Region", back_populates="dishes")
    ingredients = relationship("Ingredient", secondary=dish_ingredients, back_populates="dishes")
    occasions = relationship("Occasion", secondary=dish_occasions, back_populates="dishes")


class Ingredient(Base):
    """Ingredient model with details and substitutions."""
    __tablename__ = "ingredients"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic info
    name = Column(String, nullable=False, index=True)
    name_de = Column(String)
    name_bn = Column(String)
    
    # Media
    image = Column(String)
    
    # Details
    flavor_notes = Column(Text)
    flavor_notes_de = Column(Text)
    flavor_notes_bn = Column(Text)
    
    origin = Column(Text)
    origin_de = Column(Text)
    origin_bn = Column(Text)
    
    description = Column(Text)
    description_de = Column(Text)
    description_bn = Column(Text)
    
    # Practical info
    substitutions = Column(JSON)  # List of substitute ingredients
    allergens = Column(JSON)  # List of allergens
    
    # Relationships
    dishes = relationship("Dish", secondary=dish_ingredients, back_populates="ingredients")


class Occasion(Base):
    """Cultural occasions and events."""
    __tablename__ = "occasions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    name_de = Column(String)
    name_bn = Column(String)
    
    description = Column(Text)
    description_de = Column(Text)
    description_bn = Column(Text)
    
    date_type = Column(String)  # fixed, seasonal, lunar
    month = Column(Integer)  # For fixed dates
    day = Column(Integer)  # For fixed dates
    season = Column(String)  # For seasonal occasions
    
    # Relationships
    dishes = relationship("Dish", secondary=dish_occasions, back_populates="occasions")
