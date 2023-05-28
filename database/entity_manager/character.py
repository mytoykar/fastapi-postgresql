from sqlalchemy.orm import Session

from database.entity.character import Character, CharacterCreate


def get_character_by_id(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def get_character_by_name(db: Session, name: str):
    return db.query(Character).filter(Character.name == name).first()


def get_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Character).offset(skip).limit(limit).all()


def create_character(db: Session, character: CharacterCreate):
    db_character = Character(name=character.name)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character
