
from fastapi import FastAPI
import starlette.status as status
import urllib,json,requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional,List
from ppadb.client import Client as AdbClient
from Lib.lib import StartServer
import subprocess

import json
app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")





@app.get("/")
@app.get("/index")
async def api_index(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})


@app.get("/logincheck", description="kullanıcınun bilgilerini kontrol eden  fonksiyon ")
async def logincheck(request: Request,username:str=Form(),password:str=Form()):
       return templates.TemplateResponse("login", {"request": request})





@app.post("/submit")
async def submit(request: Request):
    form_data = await request.form()
    if "button1" in form_data:
        output = StartServer()
        return templates.TemplateResponse("index.html", {"request": request,"output":output})
    elif "button2" in form_data:
        # Code to handle button2
        output = subprocess.check_output(['adb', 'kill-server'])
        return templates.TemplateResponse("index.html", {"request": request,"output":output.decode()})
    else:
        return {"message": "No button was clicked."}