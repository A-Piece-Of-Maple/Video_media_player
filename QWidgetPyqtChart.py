import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 658)
        Form.setWindowOpacity(1.0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 100, 581, 371))
        self.label.setStyleSheet("background:rgb(36,61,91)") # QLabel背景颜色

        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        # self.timer = QTimer()  # 设置定时器
        # self.timer.timeout.connect(self.test)  # 定时器连接槽函数
        # self.timer.start(20)  # 20ms调用一次

        # QLineSeries为点，QPen为线，QChart与QChartView为面
        #QLineSeries-------------------------------------------------------
        self.series_1 = QLineSeries()  # 定义LineSerise，将类QLineSeries实例化
        self._1_point_0 = QPointF(0.00, 0.00)  # 定义折线坐标点
        self._1_point_1 = QPointF(1.00, 6.00)
        self._1_point_2 = QPointF(2.00, 2.00)
        self._1_point_3 = QPointF(4.00, 3.00)
        self._1_point_4 = QPointF(1.50, 3.00)
        self._1_point_5 = QPointF(5.00, 3.00)
        self._1_point_list = [self._1_point_0, self._1_point_1, self._1_point_4, self._1_point_2, self._1_point_3,
                              self._1_point_5]  # 定义折线点清单
        #QLineSeries-------------------------------------------------------
        # QPen-------------------------------------------------------------
        pen=QPen()
        pen.setWidth(3) # 画笔粗细
        pen.setColor(QtGui.QColor(37,167,162)) # 画笔颜色

        self.series_1.setPen(pen)
        self.series_1.append(self._1_point_list)  # 折线添加坐标点清单
        self.series_1.setName("折线一")  # 折线命名
        # self.series_1.setColor(QtGui.QColor(37,167,162)) # 同样可以设置画笔颜色
        # self.series_1.hide() # 隐藏线条
        # QPen-------------------------------------------------------------
        # QChart-------------------------------------------------------------
        self.charView = QChartView(self.label)  # 定义charView，父窗体类型为 Window

        self.chart=QChart()
        # self.chart.setTitle("123")
        self.charView.setChart(self.chart)

        self.chart.legend().hide() # 隐藏图例

        self.chart.setBackgroundVisible(False) # 隐藏自带背景
        self.charView.setGeometry(0, 0, self.label.width(), self.label.height())  # 设置charView位置、大小

        self.charView.chart().addSeries(self.series_1)  # 添加折线

        self.charView.chart().createDefaultAxes()  # 使用默认坐标系

        self.charView.chart().axisX().setTickCount(6)  # 设置x轴坐标轴节点个数
        self.charView.chart().axisX().setRange(0.00, 10.00)  # 设置默认x轴量程

        self.charView.chart().axisX().setGridLineColor(QtGui.QColor(75,148,193)) # 设置网格线条颜色
        self.charView.chart().axisY().setGridLineColor(QtGui.QColor(75, 148, 193)) # 设置网格线条颜色
        self.charView.chart().axisX().setLabelsColor(QtGui.QColor(75,148,193)) # 设置坐标标签颜色
        self.charView.chart().axisY().setLabelsColor(QtGui.QColor(75, 148, 193)) # 设置坐标标签颜色
        self.charView.chart().axisX().setLinePenColor(QtGui.QColor(75, 148, 193)) # 设置坐标线条颜色
        self.charView.chart().axisY().setLinePenColor(QtGui.QColor(75, 148, 193)) # 设置坐标线条颜色

        # self.charView.chart().axisX().setMinorTickCount(2)  # 设置单元格刻度线
        # self.charView.chart().axisX().setLabelFormat("%0.2f")  # 设置坐标轴精确度

        # self.charView.chart().setTitleBrush(QBrush(Qt.cyan))  # 设置标题笔刷
        # self.charView.chart().setTitle("车流量显示")  # 设置标题
        # self.charView.chart().setTitleBrush(QtGui.QColor(75, 148, 193))# 设置标题颜色

        self.charView.show()  # 显示charView
        # QChart-------------------------------------------------------------

        self.test()

    def test(self):
        self.series_1.append(QPointF(8.50, 6.00)) # 添加点
        self.series_1.remove(0) # 移除点
        self.charView.chart().axisX().setRange(1.00, 11.00)  # 设置默认x轴量程

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Form()#类

    ui.setupUi(Widget)
    Widget.show()

    sys.exit(app.exec_())
