from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import select, update, insert, delete

import database
import utils

router = APIRouter(prefix='/test')


@router.get('/get')
async def get() -> JSONResponse:
    with database.sessions.begin() as session:
        req = session.execute(select(database.User))
        return utils.json_responce(req.scalars().all())


@router.get('/add')
async def add(name: str, age: int) -> JSONResponse:
    with database.sessions.begin() as session:
        req = session.execute(insert(database.User).values(name=name, age=age))
        return utils.json_responce({'z': 'v'})


@router.get('/delete')
async def deleteasdsadasd(id: int) -> JSONResponse:
    with database.sessions.begin() as session:
        req = session.execute(delete(database.User).where(database.User.id == id))
        return utils.json_responce({'z': 'v'})
