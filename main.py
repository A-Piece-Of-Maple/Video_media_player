import numpy as np

import tracker
from detector import Detector
# from cv2 import cv2
import cv2
# import time
import sys
import threading
import datetime
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(1035, 663)
        Widget.setWindowOpacity(2.0)
        self.label1 = QtWidgets.QLabel(Widget)
        self.label1.setGeometry(QtCore.QRect(60, 130, 241, 371))
        self.label1.setStyleSheet("border-radius: 20px;  border: 2px groove balck;\n"
"background-color:rgb(255,245,204)")
        self.label1.setFrameShape(QtWidgets.QFrame.Box)
        self.label1.setLineWidth(1)
        self.label1.setText("")
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setObjectName("label1")
        self.CurrentTimeLabel = QtWidgets.QLabel(Widget)
        self.CurrentTimeLabel.setGeometry(QtCore.QRect(130, 140, 101, 41))
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
        self.CurrentTimeDate.setGeometry(QtCore.QRect(70, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentTimeDate.setFont(font)
        self.CurrentTimeDate.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTimeDate.setObjectName("CurrentTimeDate")
        self.CurrentTimeClock = QtWidgets.QLabel(Widget)
        self.CurrentTimeClock.setGeometry(QtCore.QRect(70, 220, 221, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentTimeClock.setFont(font)
        self.CurrentTimeClock.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTimeClock.setObjectName("CurrentTimeClock")
        self.CurrentRoadLabel = QtWidgets.QLabel(Widget)
        self.CurrentRoadLabel.setGeometry(QtCore.QRect(100, 260, 161, 41))
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
        self.CurrentRoadText.setGeometry(QtCore.QRect(70, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrentRoadText.setFont(font)
        self.CurrentRoadText.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentRoadText.setObjectName("CurrentRoadText")
        self.CurrenTrafficFlowLabel = QtWidgets.QLabel(Widget)
        self.CurrenTrafficFlowLabel.setGeometry(QtCore.QRect(120, 350, 131, 41))
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
        self.CurrenTrafficFlowText.setGeometry(QtCore.QRect(70, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        self.CurrenTrafficFlowText.setFont(font)
        self.CurrenTrafficFlowText.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrenTrafficFlowText.setObjectName("CurrenTrafficFlowText")
        self.Label = QtWidgets.QLabel(Widget)
        self.Label.setGeometry(QtCore.QRect(250, 40, 571, 61))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(20)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.label2 = QtWidgets.QLabel(Widget)
        self.label2.setGeometry(QtCore.QRect(360, 140, 611, 361))
        self.label2.setFrameShape(QtWidgets.QFrame.Box)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.StartButton = QtWidgets.QPushButton(Widget)
        self.StartButton.setEnabled(True)
        self.StartButton.setGeometry(QtCore.QRect(330, 530, 70, 70))
        font = QtGui.QFont()
        font.setKerning(True)
        self.StartButton.setFont(font)
        self.StartButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.StartButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.StartButton.setToolTipDuration(-1)
        self.StartButton.setStyleSheet("background-color:rgb(0,0,0,0)")
        self.StartButton.setText("")
        self.StartButton.setIconSize(QtCore.QSize(70, 70))
        self.StartButton.setFlat(True)
        self.StartButton.setObjectName("StartButton")
        self.PauseButton = QtWidgets.QPushButton(Widget)
        self.PauseButton.setEnabled(True)
        self.PauseButton.setGeometry(QtCore.QRect(650, 530, 70, 70))
        font = QtGui.QFont()
        font.setKerning(True)
        self.PauseButton.setFont(font)
        self.PauseButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PauseButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PauseButton.setToolTipDuration(-1)
        self.PauseButton.setStyleSheet("background-color:rgb(0,0,0,0)")
        self.PauseButton.setText("")
        self.PauseButton.setIconSize(QtCore.QSize(70, 70))
        self.PauseButton.setFlat(True)
        self.PauseButton.setObjectName("PauseButton")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(330, 600, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(650, 600, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label2.setScaledContents(True)  # 屏幕自适应
        Widget.setFixedSize(Widget.width(), Widget.height())  # 固定大小

        self.retranslateUi(Widget)

        self.StartButton.clicked.connect(self.StartButton_click)
        self.PauseButton.clicked.connect(self.PauseButton_click)

        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.CurrentTimeLabel.setText(_translate("Widget", "当前时间"))
        self.CurrentTimeDate.setText(_translate("Widget", "2022-11-21 星期二"))
        self.CurrentTimeClock.setText(_translate("Widget", "19：21：00"))
        self.CurrentRoadLabel.setText(_translate("Widget", "当前检测车道"))
        self.CurrentRoadText.setText(_translate("Widget", "北三环中路"))
        self.CurrenTrafficFlowLabel.setText(_translate("Widget", "当前车流量"))
        self.CurrenTrafficFlowText.setText(_translate("Widget", "20辆/分"))
        self.Label.setText(_translate("Widget", "视频公路车流量检测系统"))
        self.label.setText(_translate("Widget", "实时画面"))
        self.label_2.setText(_translate("Widget", "截取画面"))
        self.StartButton.setIcon(QtGui.QIcon("./play.png"))
        self.PauseButton.setIcon(QtGui.QIcon("./pause.png"))

        self.currentflg = True

    def StartButton_click(self):
        self.currentflg = True
        print(1)

    def PauseButton_click(self):
        self.currentflg = False
        print(2)


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
    ui = Ui_Widget()  # 类
    ui.setupUi(Widget)
    Widget.show()

    WeekTurn = ['天', '一', '二', '三', '四', '五', '六']  # 五

    timer = threading.Timer(0.01, CurrentTimeDateAndClockChange)  # 不可以马上运行，Qt界面还没有渲染出来
    timer.start()

    img_root = 'imgs2video/'  # 是图片序列的位置
    fps = 60  # 可以随意调整视频的帧速率

    # 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter('TestVideo.avi', fourcc, fps, (854, 480), True)  # 最后一个是保存图片的尺寸

    # 根据视频尺寸，填充一个polygon，供撞线计算使用
    mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)

    # 初始化2个撞线polygon
    list_pts_blue = [[204, 305], [227, 431], [605, 522], [1101, 464], [1900, 601], [1902, 495], [1125, 379], [604, 437],
                     [299, 375], [267, 289]]
    ndarray_pts_blue = np.array(list_pts_blue, np.int32)
    polygon_blue_value_1 = cv2.fillPoly(mask_image_temp, [ndarray_pts_blue], color=1)
    polygon_blue_value_1 = polygon_blue_value_1[:, :, np.newaxis]

    # 填充第二个polygon
    mask_image_temp = np.zeros((1080, 1920), dtype=np.uint8)
    list_pts_yellow = [[181, 305], [207, 442], [603, 544], [1107, 485], [1898, 625], [1893, 701], [1101, 568],
                       [594, 637], [118, 483], [109, 303]]
    ndarray_pts_yellow = np.array(list_pts_yellow, np.int32)
    polygon_yellow_value_2 = cv2.fillPoly(mask_image_temp, [ndarray_pts_yellow], color=2)
    polygon_yellow_value_2 = polygon_yellow_value_2[:, :, np.newaxis]

    # 撞线检测用mask，包含2个polygon，（值范围 0、1、2），供撞线计算使用
    polygon_mask_blue_and_yellow = polygon_blue_value_1 + polygon_yellow_value_2

    # 缩小尺寸，1920x1080->960x540
    polygon_mask_blue_and_yellow = cv2.resize(polygon_mask_blue_and_yellow, (960, 540))

    # 蓝 色盘 b,g,r
    blue_color_plate = [255, 0, 0]
    # 蓝 polygon图片
    blue_image = np.array(polygon_blue_value_1 * blue_color_plate, np.uint8)

    # 黄 色盘
    yellow_color_plate = [0, 255, 255]
    # 黄 polygon图片
    yellow_image = np.array(polygon_yellow_value_2 * yellow_color_plate, np.uint8)

    # 彩色图片（值范围 0-255）
    color_polygons_image = blue_image + yellow_image
    # 缩小尺寸，1920x1080->960x540
    color_polygons_image = cv2.resize(color_polygons_image, (960, 540))

    # list 与蓝色polygon重叠
    list_overlapping_blue_polygon = []

    # list 与黄色polygon重叠
    list_overlapping_yellow_polygon = []

    # 进入数量
    down_count = 0
    # 离开数量
    up_count = 0

    font_draw_number = cv2.FONT_HERSHEY_SIMPLEX
    draw_text_postion = (int(960 * 0.01), int(540 * 0.05))

    # 初始化 yolov5
    detector = Detector()

    # 打开视频
    capture = cv2.VideoCapture('short_test.mp4')
    # capture = cv2.VideoCapture('TownCentreXVID.avi')

    while True:
        # time1 = time.time()
        # 读取每帧图片
        _, im = capture.read()
        if im is None:
            break

        # 缩小尺寸，1920x1080->960x540
        im = cv2.resize(im, (960, 540))

        list_bboxs = []
        bboxes = detector.detect(im)

        # 如果画面中 有bbox
        if len(bboxes) > 0:
            list_bboxs = tracker.update(bboxes, im)

            # 画框
            # 撞线检测点，(x1，y1)，y方向偏移比例 0.0~1.0
            output_image_frame = tracker.draw_bboxes(im, list_bboxs, line_thickness=None)
            pass
        else:
            # 如果画面中 没有bbox
            output_image_frame = im
        pass

        # 输出图片
        output_image_frame = cv2.add(output_image_frame, color_polygons_image)

        if len(list_bboxs) > 0:
            # ----------------------判断撞线----------------------
            for item_bbox in list_bboxs:
                x1, y1, x2, y2, label, track_id = item_bbox

                # 撞线检测点，(x1，y1)，y方向偏移比例 0.0~1.0
                y1_offset = int(y1 + ((y2 - y1) * 0.6))

                # 撞线的点
                y = y1_offset
                x = x1

                if polygon_mask_blue_and_yellow[y, x] == 1:
                    # 如果撞 蓝polygon
                    if track_id not in list_overlapping_blue_polygon:
                        list_overlapping_blue_polygon.append(track_id)
                    pass

                    # 判断 黄polygon list 里是否有此 track_id
                    # 有此 track_id，则 认为是 外出方向
                    if track_id in list_overlapping_yellow_polygon:
                        # 外出+1
                        up_count += 1

                        print(
                            f'类别: {label} | id: {track_id} | 上行撞线 | 上行撞线总数: {up_count} | 上行id列表: {list_overlapping_yellow_polygon}')

                        # 删除 黄polygon list 中的此id
                        list_overlapping_yellow_polygon.remove(track_id)

                        pass
                    else:
                        # 无此 track_id，不做其他操作
                        pass

                elif polygon_mask_blue_and_yellow[y, x] == 2:
                    # 如果撞 黄polygon
                    if track_id not in list_overlapping_yellow_polygon:
                        list_overlapping_yellow_polygon.append(track_id)
                    pass

                    # 判断 蓝polygon list 里是否有此 track_id
                    # 有此 track_id，则 认为是 进入方向
                    if track_id in list_overlapping_blue_polygon:
                        # 进入+1
                        down_count += 1

                        print(
                            f'类别: {label} | id: {track_id} | 下行撞线 | 下行撞线总数: {down_count} | 下行id列表: {list_overlapping_blue_polygon}')

                        # 删除 蓝polygon list 中的此id
                        list_overlapping_blue_polygon.remove(track_id)

                        pass
                    else:
                        # 无此 track_id，不做其他操作
                        pass
                    pass
                else:
                    pass
                pass

            pass

            # ----------------------清除无用id----------------------
            list_overlapping_all = list_overlapping_yellow_polygon + list_overlapping_blue_polygon
            for id1 in list_overlapping_all:
                is_found = False
                for _, _, _, _, _, bbox_id in list_bboxs:
                    if bbox_id == id1:
                        is_found = True
                        break
                    pass
                pass

                if not is_found:
                    # 如果没找到，删除id
                    if id1 in list_overlapping_yellow_polygon:
                        list_overlapping_yellow_polygon.remove(id1)
                    pass
                    if id1 in list_overlapping_blue_polygon:
                        list_overlapping_blue_polygon.remove(id1)
                    pass
                pass
            list_overlapping_all.clear()
            pass

            # 清空list
            list_bboxs.clear()

            pass
        else:
            # 如果图像中没有任何的bbox，则清空list
            list_overlapping_blue_polygon.clear()
            list_overlapping_yellow_polygon.clear()
            pass
        pass

        text_draw = 'DOWN: ' + str(down_count) + \
                    ' , UP: ' + str(up_count)
        output_image_frame = cv2.putText(img=output_image_frame, text=text_draw,
                                         org=draw_text_postion,
                                         fontFace=font_draw_number,
                                         fontScale=1, color=(255, 255, 255), thickness=1)

        # cv2.imshow('demo', output_image_frame)
        if(ui.currentflg):
            img = cv2.cvtColor(output_image_frame, cv2.COLOR_BGR2RGB)  # BRG转为RGB
            img = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3
                                       , QtGui.QImage.Format_RGB888)  # 图像格式转换
            ui.label2.setPixmap(QtGui.QPixmap.fromImage(img))  # 显示一帧的图像

        # time2 = time.time()
        #
        # print('该帧处理时间为：', end='')
        # print(time2-time1)



        videoWriter.write(output_image_frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        cv2.waitKey(1)

        pass
    pass

    capture.release()
    videoWriter.release()
    cv2.destroyAllWindows()

    sys.exit(app.exec_())
