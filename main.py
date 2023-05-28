from fastapi import FastAPI

from controller.character import router as character_router
from controller.item import router as item_router

app = FastAPI()

app.include_router(character_router)
app.include_router(item_router)
