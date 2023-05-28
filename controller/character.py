from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from database.entity.base_entity import get_db
from database.entity.character import CharacterCreate, CharacterModel
from database.entity_manager import character as character_em

router = APIRouter(prefix="/api/character", tags=["Characters"])


@router.get("/{character_id}", response_model=CharacterModel)
def get_character_by_id(character_id: int, db: Session = Depends(get_db)):
    existing_character = character_em.get_character_by_id(
        db, character_id=character_id
    )
    if not existing_character:
        raise HTTPException(
            status_code=404,
            detail=f"Character with id: {character_id} does not exist.",
        )
    return existing_character


@router.post("/", response_model=CharacterModel)
def create_new_character(
    request: CharacterCreate, db: Session = Depends(get_db)
):
    existing_character = character_em.get_character_by_name(
        db, name=request.name
    )
    if existing_character:
        raise HTTPException(
            status_code=409, detail="Name already taken. Choose another name."
        )
    return character_em.create_character(db=db, character=request)
