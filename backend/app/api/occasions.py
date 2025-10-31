"""
Occasions API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Occasion
from ..schemas.schemas import Occasion as OccasionSchema

router = APIRouter()


@router.get("/occasions", response_model=list[OccasionSchema])
def get_occasions(db: Session = Depends(get_db)):
    """
    Get list of all occasions.
    """
    occasions = db.query(Occasion).all()
    return occasions


@router.get("/occasions/{occasion_id}", response_model=OccasionSchema)
def get_occasion(occasion_id: int, db: Session = Depends(get_db)):
    """
    Get detailed information about a specific occasion.
    
    - **occasion_id**: The ID of the occasion
    """
    occasion = db.query(Occasion).filter(Occasion.id == occasion_id).first()
    
    if not occasion:
        raise HTTPException(status_code=404, detail="Occasion not found")
    
    return occasion


@router.get("/occasions/{occasion_id}/dishes")
def get_occasion_dishes(occasion_id: int, db: Session = Depends(get_db)):
    """Get all dishes associated with a specific occasion."""
    occasion = db.query(Occasion).filter(Occasion.id == occasion_id).first()
    
    if not occasion:
        raise HTTPException(status_code=404, detail="Occasion not found")
    
    return occasion.dishes
