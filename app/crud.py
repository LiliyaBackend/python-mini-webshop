from . import models
from sqlalchemy.orm import Session

def create_default_products(db: Session):
    if db.query(models.Product).count() == 0:
        db.add_all([
            models.Product(name="product_1", price=1, image="product_1.jpg"),
            models.Product(name="product_2", price=2, image="product_2.jpg"),
            models.Product(name="product_3", price=3, image="product_3.jpg"),
        ])
        db.commit()

def get_all_products(db: Session):
    return db.query(models.Product).all()
