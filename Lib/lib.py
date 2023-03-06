import subprocess
import os
from subprocess import check_output



def StartServer():
     try:
       return  subprocess.run(["adb", "start-server"])
     except:
        return "server başlatılamadı"

def KillServer():
   result =  subprocess.run(["adb", "kill-server"], capture_output=True, text=True)
   return result.stdout


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



