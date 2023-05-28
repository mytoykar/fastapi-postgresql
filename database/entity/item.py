from typing import Union

from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.entity.base_entity import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=False)
    description = Column(String, index=False, default="")
    owner_id = Column(Integer, ForeignKey("characters.id"))

    owner = relationship("Character", back_populates="items")


# pydantic schemas
class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None
    owner_id: int


class ItemCreate(ItemBase):
    pass


class ItemModel(ItemBase):
    id: int

    class Config:
        orm_mode = True
