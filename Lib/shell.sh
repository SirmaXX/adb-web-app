#!/bin/bash


ListDevices(){ adb devices; }

DetailDevices(){ adb devices -l; }


#source shell.sh ;ListPackages
ListPackages(){ 
  
   adb shell pm list packages ;
   }

#source shell.sh ;ListPackagesWFile
ListPackagesWFile(){ 
  
   adb shell pm list packages  | sed 's/package://i' | tee packageslist.txt

   }
InstallApp(){
adb install  -g $1;
}


UninstallApp(){
adb uninstall $1;
}

#source shell.sh ;UninstallAppWFile
UninstallAppWFile(){

   while read line; do adb uninstall $line; done < removelist.txt
}

