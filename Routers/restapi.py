
from fastapi import APIRouter,Depends, Request,HTTPException
from flask import jsonify
from sqlalchemy.orm import Session
import urllib,json,requests
from app.Lib.schema import User_Schema,Device_Schema,Company_Schema
from app.Lib.Api_User_Controller import Api_User_Controller

restapiroute = APIRouter(responses={404: {"description": "Not found"}})





Job_Url="http://job:5001/"
Devices_Url="http://job:5001/devices"
Companies_Url="http://job:5001/companies/"
Users_Url="http://job:5001/users"
Market_Url="http://marketplace:5002/"
Log_Url="http://log_service:5004/"




@restapiroute.get("/")
@restapiroute.get("/index")
async def api_index(request: Request):
   return {"rest api service"}


#KULLANICILARIN REQUESTİ  BAŞLANGIÇ

@restapiroute.get("/users",description="Kullanıcıların bulunduğu liste")
async def users_panel(request: Request):
    Api_User_Controller.GetUsers(Users_Url)


@restapiroute.post("/adduser",description="kullanıcı ekleme fonksiyonu")
async def createuser(request: Request,user:User_Schema):  
     Api_User_Controller.AddUser(user.username,user.password,Users_Url)


@restapiroute.get("/deleteuser/{id}",description="kullanıcı silme fonksiyonu")
async def deleteuser(request: Request,id:int):
    Api_User_Controller.DeleteUser(Users_Url,id)


@restapiroute.get("/updateuser/{id}",description="kullanıcı adı ")
async def updateuser(request: Request,id:int):
    url=Users_Url+'/' +str(id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict
    

    
@restapiroute.post("/updateuser/{id}",description="kullanıcı adı ")
async def updateuser(request: Request,id:int,user:User_Schema):
    Api_User_Controller.Post_UpdateUser(id,user.username,user.password)
       






@restapiroute.post("/logincheck", description="kullanıcınun bilgilerini kontrol eden  fonksiyon ")
async def logincheck(request: Request,username:str,password:str):
        json_user={"username": username , "password": password }
        checklogin=requests.post("http://job:5001/users/login", json =json_user)
        if (checklogin.text =="true"):
           return True   
        else:
          return False
       
        







#KULLANICILARIN REQUESTİ BİTİŞ

@restapiroute.get("/job",description="iş servisi için get fonksiyonu")
async def api_job():
    response = urllib.request.urlopen(Job_Url)
    data = response.read()
    dict = json.loads(data)
    return dict

#CİHAZLARIN REQUESTİ BAŞLANGIÇ

@restapiroute.get("/devices",description="cihazların bulunduğu get fonksiyonu")
async def devices(request: Request):
    response = urllib.request.urlopen(Devices_Url)
    data = response.read()
    dict = json.loads(data)
    return dict



@restapiroute.post("/adddevice",description="cihaz ekleme fonksiyon")
async def createdevice(request: Request,device:Device_Schema ):  
     my_json={"ipaddress":device.ipadresi,"device_name":device.cihazismi,"macaddress":device.macadresi}    
     requests.post(Devices_Url+"/add", json =my_json)
     


@restapiroute.get("/deletedevice/{id}")
async def deletedevice(request: Request,id:int):
    url=Devices_Url+'/delete/'+str(id)
    response = requests.delete(url)
    return response
   
    


@restapiroute.get("/updatedevice/{id}",description="cihaz güncelleme sayfası")
async def updatedevice(request: Request,id:int):
    url=Devices_Url+'/' +str(id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict 
    

    
@restapiroute.post("/updatedevice/{id}",description="cihaz güncelleme request")
async def updatedevice(request: Request,id:int,cihazismi:str):
    url=Devices_Url+'/update/'+str(id)+'/'+str(cihazismi)
    #data = {'device_name': 'cihazismi'}
    response = requests.put(url)
    if(response.status_code==200):
       return response
    else:
        return "hata"




#CİHAZLARIN REQUESTİ BİTİŞ
#ŞİRKETLERİN REQUESTİ BAŞLANGIÇ

@restapiroute.get("/companies",description="şirketlerin bulunduğu get fonksiyonu")
async def companies(request: Request):
    response = urllib.request.urlopen(Companies_Url)
    data = response.read()
    dict = json.loads(data)
    return dict



@restapiroute.post("/addcompany",description="şirket ekleme fonksiyonu")
async def createcompany(request: Request,company:Company_Schema):  
     my_json={"Company_name":company.Company_name,"DevicesCount": company.DevicesCount,"Email":company.Email}  
     requests.post(Companies_Url+"add", json =my_json)



@restapiroute.get("/deletecompany/{id}",description="şirket silme requesti")
async def deletecompany(request: Request,id:int):
    url=Companies_Url+'delete/'+str(id)
    response = requests.delete(url)
    return response




@restapiroute.get("/updatecompany/{id}",description="şirket güncelleme sayfası")
async def updatecompany(request: Request,id:int):
    url=Companies_Url +str(id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict
    

    
@restapiroute.post("/updatecompany/{id}/{devicescount}",description="şirket güncelleme request")
async def updatecompany(request: Request,id:int,devicescount:int):
     url='http://job:5001/companies/update/'+str(id)+'/'+str(devicescount)
     response = requests.put(url)
     if(response.status_code==200):
       return response
     else:
        return "hata"
    

#ŞİRKETLERİN REQUESTİ BİTİŞ
#LOGLAR
@restapiroute.get("/logs",description="logların bulunduğu fonksiyon")
async def logs(request: Request):
    response = urllib.request.urlopen(Log_Url)
    data = response.read()
    dict = json.loads(data)
    return dict
