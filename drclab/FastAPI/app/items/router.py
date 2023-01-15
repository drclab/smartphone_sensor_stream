from .schemas import ItemSchema
from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.get('/items', tags=['items'], response_model=List[ItemSchema])
def list_item() -> List[ItemSchema]:
    return []

@router.get('/items/{id}', tags=['items'])
def read_item(id: int) -> int:
    return id

@router.post('/items', tags=['items'], response_model=ItemSchema)
def create_item(data: ItemSchema):
    return data

