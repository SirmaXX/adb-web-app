
from fastapi import FastAPI
import starlette.status as status
import urllib,json,requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional,List
import os

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







#async def submit(request: Request,url:str=Form(),port:str=Form()):
"""
@app.post("/")
async def submit(request: Request):
    form_data = await request.form()
    if "button1" in form_data:
         os.system("adb connect 192.168.1.155:5555")
         os.system("adb reboot") 
         return templates.TemplateResponse("index.html", {"request": request,"output":"worked","status":"Online"})
    elif "button2" in form_data:
        # Code to handle button2
        output = subprocess.check_output(['adb', 'kill-server'])
        return templates.TemplateResponse("index.html", {"request": request,"status":"Offline"})
    else:
        return {"message": "No button was clicked."}
    
 """

@app.post("/")
async def submit(request: Request,host:str=Form(),port:str=Form()):
    form_data = await request.form()
    if "button1" in form_data:
         portt=int(port)
         #os.system("adb connect 127.0.0.1:5037")
         command = 'adb connect %s:%d' % (host, portt)
         os.system(command)
         os.system('adb devices')
         return templates.TemplateResponse("index.html", {"request": request,"output":"deneme","status":"Online",host:host,port:port})
    elif "button2" in form_data:
        # Code to handle button2
        output = subprocess.check_output(['adb', 'kill-server'])
        return templates.TemplateResponse("index.html", {"request": request,"status":"Offline"})
    else:
        return {"message": "No button was clicked."}




@app.post("/cmd", description="kullanıcınun bilgilerini kontrol eden  fonksiyon ")
async def commandline(request: Request,command:str=Form()):
       os.system(command) 
       output = os.system(command) 
       return templates.TemplateResponse("index.html", {"request": request,"output":output,"status":"Offline"})
     
       
