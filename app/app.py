import imp
import os
import sys
from fastapi import FastAPI, Request
from app import routers

from app.config.settings import get_settings
import logging
from logging.config import dictConfig
from app import dict_config
from app.db import metadata, database, engine
from fastapi_mqtt import FastMQTT, MQTTConfig
from gmqtt.client import Subscription

# from app.untils.mqtt import Mqtt
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse

dictConfig(dict_config.log_config)

log = logging.getLogger("")

# mqtt_config = MQTTConfig(host="10.8.0.9", username="hmi", password="bormech4321", version=4)

# mqtt = FastMQTT(config=mqtt_config)

app = FastAPI(
    title="API_BORMECH",
    description="API_DESC",
    version="0.2.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.state.database = database

# mqtt.init_app(app)
# Mqtt.bor(mqtt)

folder = "app/mysite/static/"

app.mount("/static", StaticFiles(directory="app/mysite/static/"))


@app.on_event("startup")
async def startup() -> None:

    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(routers.auth_router)
app.include_router(routers.route_rodzaje)
app.include_router(routers.router_homolog)
app.include_router(routers.router_badania)
# app.include_router(routers.test_router)


@app.get("/", response_class=FileResponse)
def read_index(request: Request):
    path = "app/mysite/index.html"
    return FileResponse(path)


@app.get("/{catchall:path}", response_class=FileResponse)
def read_index(request: Request):
    # check first if requested file exists
    path = request.path_params["catchall"]
    file = folder + path

    print("look for: ", path, file)
    if os.path.exists(file):
        return FileResponse(file)
    # otherwise return index files
    index = "app/mysite/index.html"
    return FileResponse(index)
