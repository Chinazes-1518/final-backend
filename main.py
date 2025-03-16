from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

import database
import routes
import utils

from API_work import main


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Creating tables in database")
#     database.MyBase.metadata.create_all(bind=database.engine)
#     yield


main.run()

# app = FastAPI(lifespan=lifespan)
app = FastAPI()
app.include_router(routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return utils.json_responce({'data': 'йоу сасло?'})

# https://docs.sqlalchemy.org/en/14/orm/queryguide.html
# https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#tutorial-group-by-w-aggregates