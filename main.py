
from fastapi import FastAPI
import starlette.status as status
import urllib,json,requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional,List

#pyadb MIT lisansa sahip
from ppadb.client import Client as AdbClient
from Lib.lib import StartServer,connect_device,Run_Command
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





@app.post("/")
async def submit(request: Request):
    form_data = await request.form()
    if "button1" in form_data:
        output = connect_device('127.0.0.1',5037)
        return templates.TemplateResponse("index.html", {"request": request,"output":output,"status":"Online"})
    elif "button2" in form_data:
        # Code to handle button2
        output = subprocess.check_output(['adb', 'kill-server'])
        return templates.TemplateResponse("index.html", {"request": request,"output":output.decode(),"status":"Offline"})
    else:
        return {"message": "No button was clicked."}
    



@app.post("/cmd", description="kullanıcınun bilgilerini kontrol eden  fonksiyon ")
async def commandline(request: Request,command:str=Form()):
       output=Run_Command(command)
       return templates.TemplateResponse("index.html", {"request": request,"output":output.decode(),"status":"Offline"})
     
       