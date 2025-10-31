"""
Regions API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Region
from ..schemas.schemas import Region as RegionSchema

router = APIRouter()


@router.get("/regions", response_model=list[RegionSchema])
def get_regions(db: Session = Depends(get_db)):
    """
    Get list of all regions.
    """
    regions = db.query(Region).all()
    return regions


@router.get("/regions/{region_id}", response_model=RegionSchema)
def get_region(region_id: int, db: Session = Depends(get_db)):
    """
    Get detailed information about a specific region.
    
    - **region_id**: The ID of the region
    """
    region = db.query(Region).filter(Region.id == region_id).first()
    
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    return region


@router.get("/regions/{region_id}/dishes")
def get_region_dishes(region_id: int, db: Session = Depends(get_db)):
    """Get all dishes from a specific region."""
    region = db.query(Region).filter(Region.id == region_id).first()
    
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    return region.dishes
