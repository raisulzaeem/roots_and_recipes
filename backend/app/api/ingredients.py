"""
Ingredients API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Ingredient
from ..schemas.schemas import Ingredient as IngredientSchema

router = APIRouter()


@router.get("/ingredients", response_model=list[IngredientSchema])
def get_ingredients(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get list of all ingredients.
    
    - **skip**: Number of records to skip
    - **limit**: Maximum number of records to return
    """
    ingredients = db.query(Ingredient).offset(skip).limit(limit).all()
    return ingredients


@router.get("/ingredients/{ingredient_id}", response_model=IngredientSchema)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    """
    Get detailed information about a specific ingredient.
    
    - **ingredient_id**: The ID of the ingredient
    """
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return ingredient


@router.get("/ingredients/{ingredient_id}/dishes")
def get_ingredient_dishes(ingredient_id: int, db: Session = Depends(get_db)):
    """Get all dishes that use a specific ingredient."""
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return ingredient.dishes
