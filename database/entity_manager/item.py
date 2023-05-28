from sqlalchemy.orm import Session

from database.entity.item import Item, ItemCreate
from utils.pagination import Filters

filter_map = {"character_id": "owner_id", "name": "name"}


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_item_by_name(db: Session, item_name: int):
    return db.query(Item).filter(Item.name == item_name).first()


def get_items_by_filter(
    db: Session, filters: Filters, skip: int = 0, limit: int = 100
):
    translated_filters = {
        filter_map.get(f_name): f_value
        for f_name, f_value in filters.dict().items()
        if f_value is not None
    }
    return (
        db.query(Item)
        .filter_by(**translated_filters)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_items_by_owner_id(
    db: Session, owner_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(Item)
        .filter(Item.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_item(db: Session, item: ItemCreate):
    db_item = Item(
        name=item.name, owner_id=item.owner_id, description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
