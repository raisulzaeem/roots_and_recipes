"""
Database initialization script.
Loads sample data into the database.
"""
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.models import Region, Dish, Ingredient, Occasion
from app.data.sample_data import REGIONS, DISHES, INGREDIENTS, OCCASIONS


def init_db():
    """Initialize database with tables and sample data."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Check if data already exists
        if db.query(Region).count() > 0:
            print("Database already contains data. Skipping initialization.")
            return
        
        print("Loading sample data...")
        
        # Add regions
        print("  Adding regions...")
        regions = [Region(**region_data) for region_data in REGIONS]
        db.add_all(regions)
        db.commit()
        
        # Add ingredients
        print("  Adding ingredients...")
        ingredients = [Ingredient(**ingredient_data) for ingredient_data in INGREDIENTS]
        db.add_all(ingredients)
        db.commit()
        
        # Add occasions
        print("  Adding occasions...")
        occasions = [Occasion(**occasion_data) for occasion_data in OCCASIONS]
        db.add_all(occasions)
        db.commit()
        
        # Add dishes with relationships
        print("  Adding dishes...")
        for dish_data in DISHES:
            # Extract relationship IDs
            ingredient_ids = dish_data.pop('ingredient_ids', [])
            occasion_ids = dish_data.pop('occasion_ids', [])
            
            # Create dish
            dish = Dish(**dish_data)
            
            # Add ingredient relationships
            for ing_id in ingredient_ids:
                ingredient = db.query(Ingredient).filter(Ingredient.id == ing_id).first()
                if ingredient:
                    dish.ingredients.append(ingredient)
            
            # Add occasion relationships
            for occ_id in occasion_ids:
                occasion = db.query(Occasion).filter(Occasion.id == occ_id).first()
                if occasion:
                    dish.occasions.append(occasion)
            
            db.add(dish)
        
        db.commit()
        
        print("✓ Database initialized successfully!")
        print(f"  - {len(REGIONS)} regions")
        print(f"  - {len(INGREDIENTS)} ingredients")
        print(f"  - {len(OCCASIONS)} occasions")
        print(f"  - {len(DISHES)} dishes")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
