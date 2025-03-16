from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def json_responce(data: dict) -> JSONResponse:
    return JSONResponse(jsonable_encoder(data), headers={'Access-Control-Allow-Origin': '*'})
