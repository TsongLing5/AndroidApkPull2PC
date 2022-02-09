# -*- coding utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow,QListWidget,QListWidgetItem,QCheckBox,QApplication,QWidget,QPushButton
import sys
from CheckListWidget import CheckListWidget

# this code is to extract Android app
PCPath=" C:\\Users\\tsong\\Desktop\\apk\\" #apk save path
sPath="C:/Users/tsong/Desktop/apk/"
adbCMD="adb devices"
checkAllStatus=False
#adb cmd constant
packageList="adb shell pm list package"  #package list get
packagePath="adb shell pm path "
pullapk="adb pull "

def ReadAPK():
    list=os.popen(packageList).read().split("\n")  #get all apk from device
    gui.insetData(list)  #inset list to

def extractAPK():
    list=gui.getChoised()
    for ls in list:
        package=ls.replace("package:","")
        print("package:"+package)  #result: package:com.weico.international
        # pPath=os.system(packagePath+"com.weico.international")  #get apk path  //return execute result but not info
        pPath=os.popen(packagePath+package)  #get apk path
        path=pPath.read()[8:-1]
        print(path)

        # print(path.replace("\/","\\" ))
        print(pullapk+path[8:1]+PCPath)
        apkName=package.replace("com.","")+".apk"
        # apkName=""+".apk"
        if(os.path.isfile(sPath+apkName)):
            print("File is exist,pass this one.")
        else:
            if(len(path)==0):
                print("Error ,apk not exist.")
            else:
                 apk = os.system(pullapk + path.replace("\/", "\\") + PCPath + apkName)  # extert apk

def selectAllAPK():
    if(checkBox.isChecked()):

        gui.checkAll()  # Check All
    else:
        gui.uncheckAll()  #Uncheck All

if __name__ == "__main__":
    app=QApplication(sys.argv)

    window=QMainWindow()
    window.setWindowTitle("ARIA")
    window.resize(510,820)
    gui=CheckListWidget(window)
    gui.reSize(400,800)
    gui.move(10,10)

    checkBox=QCheckBox("ALL",window)
    checkBox.move(420,0)
    checkBox.clicked.connect(selectAllAPK)

    #get apk list button
    rAPK = QPushButton(window)
    rAPK.setText("读取APK列表")
    rAPK.move(420, 25)
    rAPK.resize(80, 20)
    rAPK.clicked.connect(ReadAPK)

    # Extract apk list button
    eAPK = QPushButton(window)
    eAPK.setText("提取APK")
    eAPK.move(420,50)
    eAPK.resize(80,20)
    eAPK.clicked.connect(extractAPK)

    #Check button change to checkbox
    # sAll = QPushButton(window)
    # sAll.setText("全选")
    # sAll.move(0,40)
    # sAll.resize(100, 20)
    # sAll.clicked.connect(selectAllAPK)

    #Another check list item
    # gui2=cusUI(window)
    # gui2.reSize(100,200)
    # gui2.move(200,0)
    # # gui.iniUI()
    # gui2.insetData(["list","HJDG"])
    window.show()
    sys.exit(app.exec_())