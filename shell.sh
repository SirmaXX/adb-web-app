#!/bin/bash
testA() {
  echo "TEST A";
}


ListDevices(){ adb devices; }

DetailDevices(){ adb devices -l; }

ListPackages(){ 
    adb shell pm list packages; }