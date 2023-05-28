from typing import List, Optional

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from database.entity.base_entity import get_db
from database.entity.item import ItemCreate, ItemModel
from database.entity_manager import item as item_em
from utils.pagination import PaginationParams, pagination_params

router = APIRouter(prefix="/api/item", tags=["Items"])


@router.get("/{item_id}", response_model=ItemModel)
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    existing_item = item_em.get_item_by_id(db, item_id=item_id)
    if not existing_item:
        raise HTTPException(
            status_code=404,
            detail=f"Item with id: {item_id} does not exist.",
        )
    return existing_item


@router.get("/", response_model=List[ItemModel])
def get_items_by_owner(
    query: Optional[PaginationParams] = Depends(pagination_params),
    db: Session = Depends(get_db),
):
    return item_em.get_items_by_filter(
        db=db, filters=query.filters, skip=query.skip, limit=query.limit
    )


@router.post("/", response_model=ItemModel)
def create_new_item(request: ItemCreate, db: Session = Depends(get_db)):
    return item_em.create_item(db=db, item=request)
