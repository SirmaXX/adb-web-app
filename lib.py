import subprocess
import os




def StartServer():
 """
    server başlatan fonksiyon
 """
 subprocess.run(["adb", "start-server"])


def KillServer():
 """
    server durduran fonksiyon
 """
 subprocess.run(["adb", "kill-server"])



def GetDevices():
 """
    cihazları gösteren fonksiyon
 """
 subprocess.run(["adb", "devices"])



def GetDevicesDetailed():
 """
    cihazları gösteren detaylı fonksiyon
 """
 subprocess.run(["adb", "devices","-l"])



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


İnstallApp("apps/app-debug1.apk")