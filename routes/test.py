from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import select, update, insert, delete
import json
import sys
import os

import database
import utils

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

sys.path.append(parent)

from API_work import main

router = APIRouter(prefix='/project')


@router.get('/get_map')
async def get() -> JSONResponse:
    with open('map.json', 'r') as f:
        return utils.json_responce(json.load(f))


@router.get('/setlink')
async def add(link: str) -> JSONResponse:
    main.run(link)
    return utils.json_responce({'msg': 'ok'})
