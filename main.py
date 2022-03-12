import cv2 as cv
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
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
        self.label.setScaledContents(1)#屏幕自适应
        # self.label.setPixmap(QtGui.QPixmap("C:/a.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.StartButton.setText(_translate("Widget", "播放"))
        self.PauseButton.setText(_translate("Widget", "暂停"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()#类
    ui.setupUi(Widget)
    #ui.label.setPixmap(QtGui.QPixmap("C:/a.png"))
    # Widget.show()

    capture = cv.VideoCapture("C:\\a.flv")
    Widget.show()

    ret, img = capture.read()
    # cv.imshow('video', fram)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
    ui.label.setPixmap(QtGui.QPixmap.fromImage(img))

    # while(True):

    sys.exit(app.exec_())

    #假设下面的代码已经实现帧处理
    #需要处理的问题就是如何在Qt界面上显示这个视频
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




