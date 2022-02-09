
from PyQt5.QtWidgets import QMainWindow,QListWidget,QListWidgetItem,QCheckBox,QApplication,QWidget,QPushButton
import sys

# boolen allChecked
list=["A","R","EEE","I","A"]
class CheckListWidget():
    def __init__(self,*__args):
        self.listWidget = QListWidget(*__args);
    def iniUI(self):
        self.listWidget.resize(200,500)
        # self.resize(200,400)
    def insetData(self,dataList):
        for d in dataList:
            print(d)
            box=QCheckBox(d)
            item=QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,box)

    def getChoised(self):
        count=self.listWidget.count()
        list=[self.listWidget.itemWidget(self.listWidget.item(i))
        for i in range(count)]
        choosed=[]
        for c in list:
            if(c.isChecked()):
                # print("Checked")
                # print(c.text())
                choosed.append(c.text())
            # else:
            #     print("Not Checked")
            #     print(c.text())
        return choosed
    def reSize(self,x,y):
        self.listWidget.resize(x, y)
    def move(self,x,y):
        self.listWidget.move(x, y)
    def checkAll(self):
        count=self.listWidget.count()
        list=[self.listWidget.itemWidget(self.listWidget.item(i))
        for i in range(count)]
        choosed=[]
        for c in list:
            c.setChecked(True)
    def uncheckAll(self):
        count=self.listWidget.count()
        list=[self.listWidget.itemWidget(self.listWidget.item(i))
        for i in range(count)]
        choosed=[]
        for c in list:
            c.setChecked(False)


def pData():
    l=gui.getChoised()
    for i in l:
        print(i)
    gui.checkAll()
if __name__ == "__main__":
    app=QApplication(sys.argv)

    window=QMainWindow()
    window.setWindowTitle("ARIA")
    window.resize(400,400)
    gui=cusUI(window)
    gui.reSize(100,200)
    gui.move(100,0)
    # gui.iniUI()
    gui.insetData(list)


    Abs = QPushButton(window)
    Abs.setText("A不是")
    Abs.clicked.connect(pData)


    # gui2=cusUI(window)
    # gui2.reSize(100,200)
    # gui2.move(200,0)
    # # gui.iniUI()
    # gui2.insetData(["list","HJDG"])
    window.show()
    sys.exit(app.exec_())