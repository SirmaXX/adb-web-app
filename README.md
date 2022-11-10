# adb-web-app

# İhtiyaçlar
 Kullanıcı tarafından IP yazıldığı vakit aşağıdaki komutlar butonlar ile çalışacaktır.
 - SHUTDOWN,
 - RESTART
 - APP CLOSE
 - APP OPEN
 - APP INSTALL
 - APP UNINSTALL
 - APP LİST 


## döküman oluşturma
pdoc --html ./lib.py -o ./Docs --force


## ip ekleme
adb tcpip 5555
adb connect 192.168.0.11:5555
adb devices


## Shell kullanımı(örnek)
source shell.sh ;DetailDevices


## uygulama baslatma (root olmak gerekli)
https://stackoverflow.com/questions/4567904/how-to-start-an-application-using-android-adb-tools/4567928#4567928