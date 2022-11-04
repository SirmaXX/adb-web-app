import subprocess



def getdevices():
 """
    cihazları gösteren yapı
 """
 subprocess.run(["adb", "devices"])



getdevices()