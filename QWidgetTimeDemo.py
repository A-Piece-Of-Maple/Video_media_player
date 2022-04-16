import cv2

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import threading
import datetime

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(952, 594)
        self.StartButton = QtWidgets.QPushButton(Widget)
        self.StartButton.setGeometry(QtCore.QRect(230, 530, 141, 51))
        self.StartButton.setStyleSheet("background-color: rgb(224,230,252);\n"
"color: balck;  \n"
"border-radius: 20px;  border: 3px groove gray;\n"
"border-style: outset;")
        self.StartButton.setObjectName("StartButton")
        self.PauseButton = QtWidgets.QPushButton(Widget)
        self.PauseButton.setGeometry(QtCore.QRect(570, 530, 141, 51))
        self.PauseButton.setStyleSheet("background-color: rgb(224,230,252);\n"
"color: balck;  \n"
"border-radius: 20px;  border: 3px groove gray;\n"
"border-style: outset;")
        self.PauseButton.setObjectName("PauseButton")
        self.label1 = QtWidgets.QLabel(Widget)
        self.label1.setGeometry(QtCore.QRect(20, 130, 241, 371))
        self.label1.setStyleSheet("border-radius: 20px;  border: 2px groove balck;\n"
"background-color:rgb(255,245,204)")
        self.label1.setFrameShape(QtWidgets.QFrame.Box)
        self.label1.setLineWidth(1)
        self.label1.setText("")
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setObjectName("label1")
        self.CurrentTimeLabel = QtWidgets.QLabel(Widget)
        self.CurrentTimeLabel.setGeometry(QtCore.QRect(90, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.CurrentTimeLabel.setFont(font)
        self.CurrentTimeLabel.setLineWidth(2)
        self.CurrentTimeLabel.setTextFormat(QtCore.Qt.PlainText)
        self.CurrentTimeLabel.setScaledContents(False)
        self.CurrentTimeLabel.setWordWrap(False)
        self.CurrentTimeLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.CurrentTimeLabel.setObjectName("CurrentTimeLabel")
        self.CurrentTimeDate = QtWidgets.QLabel(Widget)
        self.CurrentTimeDate.setGeometry(QtCore.QRect(30, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentTimeDate.setFont(font)
        self.CurrentTimeDate.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTimeDate.setObjectName("CurrentTimeDate")
        self.CurrentTimeClock = QtWidgets.QLabel(Widget)
        self.CurrentTimeClock.setGeometry(QtCore.QRect(30, 220, 221, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentTimeClock.setFont(font)
        self.CurrentTimeClock.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTimeClock.setObjectName("CurrentTimeClock")
        self.CurrentRoadLabel = QtWidgets.QLabel(Widget)
        self.CurrentRoadLabel.setGeometry(QtCore.QRect(60, 260, 161, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.CurrentRoadLabel.setFont(font)
        self.CurrentRoadLabel.setLineWidth(2)
        self.CurrentRoadLabel.setTextFormat(QtCore.Qt.PlainText)
        self.CurrentRoadLabel.setScaledContents(False)
        self.CurrentRoadLabel.setWordWrap(False)
        self.CurrentRoadLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.CurrentRoadLabel.setObjectName("CurrentRoadLabel")
        self.CurrentRoadText = QtWidgets.QLabel(Widget)
        self.CurrentRoadText.setGeometry(QtCore.QRect(30, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentRoadText.setFont(font)
        self.CurrentRoadText.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentRoadText.setObjectName("CurrentRoadText")
        self.CurrenTrafficFlowLabel = QtWidgets.QLabel(Widget)
        self.CurrenTrafficFlowLabel.setGeometry(QtCore.QRect(80, 350, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.CurrenTrafficFlowLabel.setFont(font)
        self.CurrenTrafficFlowLabel.setLineWidth(2)
        self.CurrenTrafficFlowLabel.setTextFormat(QtCore.Qt.PlainText)
        self.CurrenTrafficFlowLabel.setScaledContents(False)
        self.CurrenTrafficFlowLabel.setWordWrap(False)
        self.CurrenTrafficFlowLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.CurrenTrafficFlowLabel.setObjectName("CurrenTrafficFlowLabel")
        self.CurrenTrafficFlowText = QtWidgets.QLabel(Widget)
        self.CurrenTrafficFlowText.setGeometry(QtCore.QRect(30, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrenTrafficFlowText.setFont(font)
        self.CurrenTrafficFlowText.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrenTrafficFlowText.setObjectName("CurrenTrafficFlowText")
        self.Label = QtWidgets.QLabel(Widget)
        self.Label.setGeometry(QtCore.QRect(190, 40, 571, 61))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(20)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.label2 = QtWidgets.QLabel(Widget)
        self.label2.setGeometry(QtCore.QRect(300, 140, 611, 361))
        self.label2.setFrameShape(QtWidgets.QFrame.Box)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label2.setScaledContents(True)  # 屏幕自适应

        Widget.setFixedSize(Widget.width(),Widget.height())#固定大小

        self.StartButton.clicked.connect(self.StartButton_click)
        self.PauseButton.clicked.connect(self.PauseButton_click)

        self.timer = QTimer()  # 设置定时器
        self.timer.timeout.connect(self.operate)  # 定时器连接槽函数
        self.timer.start(20)  # 3s调用一次

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "流量监测系统"))#标题
        Widget.setWindowIcon(QtGui.QIcon("./monitor.png"))#左上角图标
        self.StartButton.setText(_translate("Widget", "实时画面"))#实时画面
        # self.StartButton.setIcon(QtGui.QIcon("./monitor.png"))
        self.PauseButton.setText(_translate("Widget", "暂停画面"))
        self.CurrentTimeLabel.setText(_translate("Widget", "当前时间"))
        self.CurrentTimeDate.setText(_translate("Widget", ""))
        self.CurrentTimeClock.setText(_translate("Widget", ""))
        self.CurrentRoadLabel.setText(_translate("Widget", "当前检测车道"))
        self.CurrentRoadText.setText(_translate("Widget", "北三环中路"))
        self.CurrenTrafficFlowLabel.setText(_translate("Widget", "当前车流量"))
        self.CurrenTrafficFlowText.setText(_translate("Widget", "20辆/分"))
        self.Label.setText(_translate("Widget", "视频公路车流量检测系统"))

        self.currentflg=True

    def StartButton_click(self):
        self.currentflg=True
        print(1)

    def PauseButton_click(self):
        self.currentflg=False

    def operate(self):#定时器调用函数
        ret, img = capture.read()  # 读取一帧数据
        if(self.currentflg):
            # img = cv.flip(img, 1)#画面翻转
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#BRG转为RGB
            img = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1]*3
                               ,QtGui.QImage.Format_RGB888)#图像格式转换
            ui.label2.setPixmap(QtGui.QPixmap.fromImage(img))#显示一帧的图像

def CurrentTimeDateAndClockChange():
    CurrentTimeDateFront = datetime.datetime.now().strftime('%Y-%m-%d')  # 2022-04-01
    CurrentTimeClock = datetime.datetime.now().strftime('%H:%M:%S')  # 16:12:24
    CurrentTimeDateBack = datetime.datetime.now().strftime('%w')  # 5
    CurrentTimeDateText = CurrentTimeDateFront + ' 星期' + WeekTurn[int(CurrentTimeDateBack)]  # 2022-04-01 星期五
    ui.CurrentTimeDate.setText(CurrentTimeDateText) # 2022-04-01 星期五
    ui.CurrentTimeClock.setText(CurrentTimeClock)# 16:12:24
    #这里需要让车流量实现实时的显示
    global timer
    timer = threading.Timer(1, CurrentTimeDateAndClockChange)
    timer.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()#类

    WeekTurn = ['天', '一', '二', '三', '四', '五', '六']  # 五

    timer = threading.Timer(0.01, CurrentTimeDateAndClockChange)#不可以马上运行，Qt界面还没有渲染出来
    timer.start()

    ui.setupUi(Widget)
    Widget.show()

    capture = cv2.VideoCapture("C:\\test3.mp4")
    ret, img = capture.read()  # 读取一帧数据
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  ##cv读进来是BGR形式的，需要转换成RGB形式

    temp_imgSrc = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1]*3, QtGui.QImage.Format_RGB888)

    image3 = QtGui.QPixmap(temp_imgSrc)  ##QImage类型图像放入QPixmap

    ui.label2.setPixmap(image3)

    sys.exit(app.exec_())



