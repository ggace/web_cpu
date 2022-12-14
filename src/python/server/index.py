from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import util.Util as util

import controller.MainController as mainController
import controller.SampleController as sampleController
import controller.PostController as postController

app = FastAPI()

app.mount("/static", StaticFiles(directory="../../templates/static"), name="static")
templates = Jinja2Templates(directory="../../templates/htmls")

apis = {
    "main": {"function" : mainController.main, "comment": "메인페이지"},
    "sample": {"function" : sampleController.sample, "comment": "샘플페이지"},
    "post_getAll": {"function": postController.getAll, "comment": "포스트 전체 받기"},
    "post_getEach": {"function": postController.getEach, "comment": "포스트 각각 받기"},
    "post_create" : {"function": postController.create, "comment": "포스트 작성"}
}

htmls = {
    "test": {"location" : "test.html", "title": "테스트"},
    "posts": {"location" : "posts.html", "title": "게시물들"}
}

@app.get("/")
async def url(req:Request):
    params = {}
    if(str(req.query_params).strip() != ""):
        params = util.get_params(str(req.query_params).strip())

    controllerFunc = apis.get("main")
    if(controllerFunc != None):
        return controllerFunc["function"](params)

    return "Not exists page"

@app.get("/api/{api}")
async def url(api:str, req:Request):
    params = {}
    if(str(req.query_params).strip() != ""):
        params = util.get_params(str(req.query_params).strip())

    controller = apis.get(api)
    if(controller != None):
        return controller["function"](params)

    return "Not exists page"

@app.get("/html/{file}", response_class=HTMLResponse)
async def read_item(req: Request, file: str):
    params = {}
    if(str(req.query_params).strip() != ""):
        params = util.get_params(str(req.query_params).strip())

    controller = htmls.get(file)


    return templates.TemplateResponse(controller["location"], {"request": req, "params":params, "title" : controller["title"]})
