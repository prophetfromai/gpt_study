from fastapi import APIRouter
from pydantic import BaseModel
from typing import Annotated
from firestore import 

router = APIRouter()

@router.get('/get_all')
async def get_all_data_from_db(db: Annotated[]):


