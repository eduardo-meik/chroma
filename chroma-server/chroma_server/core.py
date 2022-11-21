import os
from fastapi import FastAPI

from chroma_server.routes import ChromaRouter
from chroma_server.index.hnswlib import Hnswlib
from chroma_server.db.duckdb import DuckDB

# we import types here so that the user can import them from here
from chroma_server.types import (
    ProcessEmbedding, AddEmbedding, FetchEmbedding, 
    QueryEmbedding, CountEmbedding, DeleteEmbedding, 
    RawSql, Results, SpaceKeyInput)

def create_index_data_dir():
    if not os.path.exists(os.getcwd() + '/index_data'):
        os.makedirs(os.getcwd() + '/index_data')
    core._ann_index.set_save_folder(os.getcwd() + '/index_data')

core = FastAPI(debug=True)
core._db = DuckDB()
core._ann_index = Hnswlib()

create_index_data_dir()

router = ChromaRouter(app=core, db=DuckDB, ann_index=Hnswlib)
core.include_router(router.router)

# headless mode
core.heartbeat = router.root
core.add = router.add
core.count = router.count
core.fetch = router.fetch
core.reset = router.reset
core.delete = router.delete
core.get_nearest_neighbors = router.get_nearest_neighbors
core.raw_sql = router.raw_sql
core.create_index = router.create_index

# these as currently constructed require celery
# chroma_core.process = process
# chroma_core.get_status = get_status
# chroma_core.get_results = get_results