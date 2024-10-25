from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated, List
from app.dependencies import get_firestore_client
from google.cloud import firestore

router = APIRouter()

class NoteModel(BaseModel):
    title: str
    content: str
    userId: str
    
class NotesResponseModel(BaseModel):
    message: List[NoteModel]

class CreateNoteModel(BaseModel):
    title: str
    content: str
    userId: str


@router.get('/get_all')
async def get_all_data_from_db(note: CreateNoteModel, db: Annotated[firestore.Client, Depends(get_firestore_client)]) -> NotesResponseModel:
    # referenc to the mydocs/notes collection
    notes_ref = db.collection('mydocs/notes')

    # stream the documents a generator
    docs = notes_ref.stream()

    docs_dict = [NoteModel(**doc.dict()) for doc in docs]
    return NotesResponseModel(message=docs_dict)

@router.post('/add_note')
async def add_note(note: CreateNoteModel, db: Annotated[firestore.Client, Depends(get_firestore_client)]):
    try:
        notes_ref = db.collection('mydocs/notes')

        notes_ref.add(note.model_dump())

        return {"message": "Note added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding note: {str(e)}")