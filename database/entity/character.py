from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database.entity.base_entity import Base
from database.entity.item import ItemModel


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


# pydantic schemas
class CharacterBase(BaseModel):
    name: str


class CharacterCreate(CharacterBase):
    pass


class CharacterModel(CharacterBase):
    id: int
    name: str
    is_active: bool = True
    items: list[ItemModel] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
