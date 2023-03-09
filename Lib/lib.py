import subprocess
import os
from subprocess import check_output
from ppadb.client import Client

import json

def StartServer():
     try:
       return  subprocess.run(["adb", "start-server"])
     except:
        return "server başlatılamadı"

def KillServer():
   result =  subprocess.run(["adb", "kill-server"], capture_output=True, text=True)
   return result.stdout


#127.0.0.1
#5037
def connect_device(host,port):
    StartServer()
    adb = Client(host=host,port=port)
    devices = adb.devices()
    if len(devices) == 0:
        return "No Devices Attached"
    return devices[0]



def GetDevices():
 """
    cihazları gösteren fonksiyon
 """
 subprocess.run(["adb", "devices"])



def GetDevicesDetailed():
 """
    cihazları gösteren detaylı fonksiyon
 """
 result = subprocess.run(["adb", "devices","-l"], stdout=subprocess.PIPE)
 return result.stdout.decode('utf-8')



def PackageList():
   """
    yüklü paketleri gösteren fonksiyon
   """
   cmd = "adb shell pm list packages"
   returned_value = os.system(cmd)  # returns the exit code in unix
   
   print('returned value:', returned_value)



def İnstallApp(file):
   """
    apk yükler
   """
   subprocess.run(["adb", "install","-g",file])


def Run_Command(command):
   cmd = command
   output = os.popen(cmd).read()
   packages = output.split('\n')
   return  packages





