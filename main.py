import cv2 as cv
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,Qt
from PIL import Image
import numpy as np


class Ui_Widget(object):
    def setupUi(self, Widget):#定义界面以及窗口大小
        super(Ui_Widget, self).__init__()

        Widget.setObjectName("Widget")
        Widget.resize(767, 529)

        self.StartButton = QtWidgets.QPushButton(Widget)
        self.StartButton.setGeometry(QtCore.QRect(60, 450, 93, 28))
        self.StartButton.setObjectName("StartButton")
        self.PauseButton = QtWidgets.QPushButton(Widget)
        self.PauseButton.setGeometry(QtCore.QRect(180, 450, 93, 28))
        self.PauseButton.setObjectName("PauseButton")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(40, 40, 671, 351))
        self.label.setText("")
        self.label.setScaledContents(True)#屏幕自适应
        self.label.setObjectName("label")

        #self.timer=QTimer()#设置定时器
        #self.timer.timeout.connect(self.operate)#定时器连接槽函数
        #self.timer.start(3000)#3s调用一次

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):#定义控件和控件文本
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.StartButton.setText(_translate("Widget", "播放"))
        self.PauseButton.setText(_translate("Widget", "暂停"))

    # def operate(self):#定时器调用函数
    #     ret, img = capture.read()#读取一帧数据
    #     img = cv.flip(img, 1)#画面翻转
    #     img = cv.cvtColor(img, cv.COLOR_BGR2RGB)#数据格式转换
    #     img = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)#数据格式转换
    #     ui.label.setPixmap(QtGui.QPixmap.fromImage(img))#显示一帧的图像


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()#类
    ui.setupUi(Widget)


    capture = cv.VideoCapture("C:\\test3.mp4")
    ret, img = capture.read()  # 读取一帧数据
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  ##cv读进来是BGR形式的，需要转换成RGB形式
    # blue = cv.split(img)[0]  ##得到图像蓝色通道灰度图

    # ui.operate()#初始的第一帧图像显示

    temp_imgSrc = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1]*3, QtGui.QImage.Format_RGB888)
    image3 = QtGui.QPixmap(temp_imgSrc)  ##QImage类型图像放入QPixmap
    # 将图片转换为QPixmap方便显示
    # pixmap_imgSrc = QtGui.QPixmap.fromImage(temp_imgSrc)

    ui.label.setPixmap(image3)

    Widget.show()

    sys.exit(app.exec_())

#下为用于测试的代码
# capture=cv.VideoCapture("C:\\a.flv")
# while (True):
#     ret, fram = capture.read()  # 如果有视频,ret返回一个True,否则,返回False;fram为返回的内容
#     fram = cv.flip(fram, 1)  # 由于打开的是摄像头,内容与拍摄相反,需要进行翻转,1为左右翻转,-1为上下翻转
#     print(type(fram))
#
#     cv.imshow('video', fram)  # 展示fram内容
#     c = cv.waitKey(50)  # 等待用户50毫秒,即50毫秒每帧
#     if c == 27:  # 27为esc的键码
#         cv.destroyAllWindoes()  # 关闭窗口
#         break

# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
# class QpixmapDemo(QWidget):
#     def __init__(self,parent=None):
#         super(QpixmapDemo, self).__init__(parent)
#         self.setWindowTitle('QPixmap例子')
#
#         layout=QVBoxLayout()
#
#         lab1=QLabel()
#         # QPixmap.load(":/image/a.jpg")
#         lab1.setPixmap(QPixmap("C:/a.png"))
#         layout.addWidget(lab1)
#
#         self.setLayout(layout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo =QpixmapDemo()
#     demo.show()
#     sys.exit(app.exec_())




