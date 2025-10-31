"""
Dishes API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..models.models import Dish, Region, Ingredient, Occasion
from ..schemas.schemas import Dish as DishSchema, DishSummary, DishListResponse

router = APIRouter()


@router.get("/dishes", response_model=DishListResponse)
def get_dishes(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page"),
    region_id: Optional[int] = Query(None, description="Filter by region"),
    dietary_type: Optional[str] = Query(None, description="Filter by dietary type"),
    heat_level: Optional[int] = Query(None, ge=0, le=5, description="Filter by heat level"),
    occasion_id: Optional[int] = Query(None, description="Filter by occasion"),
    db: Session = Depends(get_db)
):
    """
    Get list of dishes with optional filters.
    
    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 10, max: 100)
    - **region_id**: Filter by region
    - **dietary_type**: Filter by dietary type (vegetarian, vegan, pescatarian, meat)
    - **heat_level**: Filter by heat level (0-5)
    - **occasion_id**: Filter by occasion
    """
    # Build query
    query = db.query(Dish)
    
    # Apply filters
    if region_id:
        query = query.filter(Dish.region_id == region_id)
    if dietary_type:
        query = query.filter(Dish.dietary_type == dietary_type)
    if heat_level is not None:
        query = query.filter(Dish.heat_level == heat_level)
    if occasion_id:
        query = query.join(Dish.occasions).filter(Occasion.id == occasion_id)
    
    # Get total count
    total = query.count()
    
    # Apply pagination
    offset = (page - 1) * page_size
    dishes = query.offset(offset).limit(page_size).all()
    
    return {
        "dishes": dishes,
        "total": total,
        "page": page,
        "page_size": page_size
    }


@router.get("/dishes/{dish_id}", response_model=DishSchema)
def get_dish(dish_id: int, db: Session = Depends(get_db)):
    """
    Get detailed information about a specific dish.
    
    - **dish_id**: The ID of the dish
    """
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    
    return dish


@router.get("/dishes/{dish_id}/ingredients")
def get_dish_ingredients(dish_id: int, db: Session = Depends(get_db)):
    """Get all ingredients for a specific dish."""
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    
    return dish.ingredients
