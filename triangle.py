from PyQt5 import QtCore, QtGui, QtWidgets
import numpy


class Ui_TriangleWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 900))
        MainWindow.setStyleSheet("margin: 0;\n"
                                 "padding: 0;\n"
                                 "border: none")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
                                         "    background-color: #c0c0c0;\n"
                                         "    color: black;\n"
                                         "    border: none\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton {\n"
                                         "    background-color: LightSlateGray;\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: LightGray;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: grey;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_2.setStyleSheet("background-color: grey")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_23 = QtWidgets.QFrame(self.frame_10)
        self.frame_23.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_21.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_21.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_21.addWidget(self.checkBox)
        self.horizontalLayout_6.addWidget(self.frame_23, 0, QtCore.Qt.AlignLeft)
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_3.setContentsMargins(-1, -1, 30, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_14)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Images/triangle_cl.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_6.addWidget(self.frame_14)
        self.horizontalLayout_4.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_1 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_20 = QtWidgets.QFrame(self.frame_1)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_7.addWidget(self.frame_20, 0, QtCore.Qt.AlignLeft)
        self.frame_21 = QtWidgets.QFrame(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_15.addWidget(self.lineEdit)
        self.horizontalLayout_7.addWidget(self.frame_21)
        self.verticalLayout_5.addWidget(self.frame_1)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_30 = QtWidgets.QFrame(self.frame_16)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.frame_30)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.horizontalLayout_13.addWidget(self.frame_30, 0, QtCore.Qt.AlignLeft)
        self.frame_31 = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_31)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_16.addWidget(self.lineEdit_2)
        self.horizontalLayout_13.addWidget(self.frame_31)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_19 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_32 = QtWidgets.QFrame(self.frame_19)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.horizontalLayout_15.addWidget(self.frame_32, 0, QtCore.Qt.AlignLeft)
        self.frame_33 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_17.addWidget(self.lineEdit_3)
        self.horizontalLayout_15.addWidget(self.frame_33)
        self.verticalLayout_5.addWidget(self.frame_19)
        self.frame_100 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_100.sizePolicy().hasHeightForWidth())
        self.frame_100.setSizePolicy(sizePolicy)
        self.frame_100.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_100.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_100.setObjectName("frame_100")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_100)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_101 = QtWidgets.QFrame(self.frame_100)
        self.frame_101.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_101.setObjectName("frame_101")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_101)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_6 = QtWidgets.QLabel(self.frame_101)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_25.addWidget(self.label_6)
        self.horizontalLayout_23.addWidget(self.frame_101, 0, QtCore.Qt.AlignLeft)
        self.frame_102 = QtWidgets.QFrame(self.frame_100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_102.sizePolicy().hasHeightForWidth())
        self.frame_102.setSizePolicy(sizePolicy)
        self.frame_102.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_102.setObjectName("frame_102")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_102)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_102)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_22.addWidget(self.lineEdit_6)
        self.horizontalLayout_23.addWidget(self.frame_102)
        self.verticalLayout_5.addWidget(self.frame_100)
        self.horizontalLayout_10.addWidget(self.frame_13)
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_200 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_200.sizePolicy().hasHeightForWidth())
        self.frame_200.setSizePolicy(sizePolicy)
        self.frame_200.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_200.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_200.setObjectName("frame_200")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_200)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_201 = QtWidgets.QFrame(self.frame_200)
        self.frame_201.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_201.setObjectName("frame_201")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_201)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_7 = QtWidgets.QLabel(self.frame_201)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_27.addWidget(self.label_7)
        self.horizontalLayout_26.addWidget(self.frame_201, 0, QtCore.Qt.AlignLeft)
        self.frame_202 = QtWidgets.QFrame(self.frame_200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_202.sizePolicy().hasHeightForWidth())
        self.frame_202.setSizePolicy(sizePolicy)
        self.frame_202.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_202.setObjectName("frame_202")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_202)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_202)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_23.addWidget(self.lineEdit_7)
        self.horizontalLayout_26.addWidget(self.frame_202)
        self.verticalLayout_7.addWidget(self.frame_200)
        self.frame_300 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_300.sizePolicy().hasHeightForWidth())
        self.frame_300.setSizePolicy(sizePolicy)
        self.frame_300.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_300.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_300.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_300.setObjectName("frame_300")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_300)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_301 = QtWidgets.QFrame(self.frame_300)
        self.frame_301.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_301.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_301.setObjectName("frame_301")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_301)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_11 = QtWidgets.QLabel(self.frame_301)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_31.addWidget(self.label_11)
        self.horizontalLayout_30.addWidget(self.frame_301, 0, QtCore.Qt.AlignLeft)
        self.frame_302 = QtWidgets.QFrame(self.frame_300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_302.sizePolicy().hasHeightForWidth())
        self.frame_302.setSizePolicy(sizePolicy)
        self.frame_302.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_302.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_302.setObjectName("frame_302")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_302)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_302)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_25.addWidget(self.lineEdit_9)
        self.horizontalLayout_30.addWidget(self.frame_302)
        self.verticalLayout_7.addWidget(self.frame_300)
        self.frame_34 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_35 = QtWidgets.QFrame(self.frame_34)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.frame_35)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.horizontalLayout_17.addWidget(self.frame_35, 0, QtCore.Qt.AlignLeft)
        self.frame_36 = QtWidgets.QFrame(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame_36.setFont(font)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_36)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_18.addWidget(self.lineEdit_4)
        self.horizontalLayout_17.addWidget(self.frame_36)
        self.verticalLayout_7.addWidget(self.frame_34)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMaximumSize(QtCore.QSize(468, 16777215))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_37 = QtWidgets.QFrame(self.frame_17)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_15 = QtWidgets.QLabel(self.frame_37)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_20.addWidget(self.label_15)
        self.horizontalLayout_19.addWidget(self.frame_37, 0, QtCore.Qt.AlignLeft)
        self.frame_38 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_38)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_19.addWidget(self.lineEdit_5)
        self.horizontalLayout_19.addWidget(self.frame_38)
        self.verticalLayout_7.addWidget(self.frame_17)
        self.horizontalLayout_10.addWidget(self.frame_15)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_7)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_12, clicked=lambda: self.result())
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_12, clicked=lambda: self.update())
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 1))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100000, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_12)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_6.addWidget(self.frame_12, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)
        self.triangle = "cl"
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Triangle"))
        self.label.setText(_translate("MainWindow", "Geometric Calculator"))
        self.checkBox_3.setText(_translate("MainWindow", "Right triangle"))
        self.checkBox_2.setText(_translate("MainWindow", "Equilateral triangle"))
        self.checkBox.setText(_translate("MainWindow", "Isosceles triangle"))
        self.label_4.setText(_translate("MainWindow", "a:"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "b:"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "c:"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "h1:"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "h2:"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "h3:"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "S:"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "P:"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "Results"))
        self.pushButton_3.setText(_translate("MainWindow", "Update/Nullify"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))

    # =======================================================================
    def nullify(self):
        self.lineEdit.setText("0")
        self.lineEdit_2.setText("0")
        self.lineEdit_3.setText("0")
        self.lineEdit_4.setText("0")
        self.lineEdit_5.setText("0")
        self.lineEdit_6.setText("0")
        self.lineEdit_7.setText("0")
        self.lineEdit_9.setText("0")

    def update(self):
        self.nullify()
        # включение редактирования
        self.frame_16.show()
        self.frame_19.show()
        self.frame_200.show()
        self.frame_300.show()
        self.pushButton_2.show()
        self.label_6.setText("h1:")

        # р/с и прямоугольный
        if self.checkBox_2.isChecked() and self.checkBox_3.isChecked():
            self.errors()
        # р/б
        elif self.checkBox.isChecked() and not self.checkBox_3.isChecked() and not self.checkBox_2.isChecked():
            self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/triangle_rb.png"))
            self.frame_19.hide()
            self.frame_300.hide()
            self.triangle = "rb"
        # р/с
        elif self.checkBox_2.isChecked():
            self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/triangle_rs.png"))
            self.frame_16.hide()
            self.frame_19.hide()
            self.frame_200.hide()
            self.frame_300.hide()
            self.label_6.setText("h:")
            self.triangle = "rs"
        # пр обычный
        elif self.checkBox_3.isChecked() and not self.checkBox.isChecked():
            self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/triangle_pr.png"))
            self.frame_200.hide()
            self.frame_300.hide()
            self.label_6.setText("h:")
            self.triangle = "pr"
        # пр р/б
        elif self.checkBox_3.isChecked() and self.checkBox.isChecked():
            self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/triangle_rb_pr.png"))
            self.frame_16.hide()
            self.frame_200.hide()
            self.frame_300.hide()
            self.label_6.setText("h:")
            self.triangle = "pr_rb"
        # обычный треугольник
        else:
            self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/triangle_cl.png"))
            self.tiangle = "cl"

    # =======================================================================
    # ERRORS ======================================
    # =======================================================================
    def errors(self):
        self.label_3.setPixmap(QtGui.QPixmap("C:/Coding/Python/PyQt5/Calc/Images/error.png"))
        self.pushButton_2.hide()

    # =============================================
    # Result
    # =============================================

    def result(self):
        a = float(self.lineEdit.text())
        b = float(self.lineEdit_2.text())
        c = float(self.lineEdit_3.text())
        h1 = float(self.lineEdit_6.text())
        h2 = float(self.lineEdit_7.text())
        h3 = float(self.lineEdit_9.text())
        S = float(self.lineEdit_4.text())
        P = float(self.lineEdit_5.text())

        for i in range(10):
            # =======================================
            # Classic
            # =======================================
            if self.triangle == "cl":
                if a and b and P:
                    c = P - a - b
                if c and b and P:
                    a = P - b - c
                if a and c and P:
                    b = P - a - c

                if a != 0 and h1 != 0:
                    S = 0.5 * a * h1
                if b != 0 and h2 != 0:
                    S = 0.5 * b * h2
                if c != 0 and h3 != 0:
                    S = 0.5 * c * h3

                if S != 0 and h1 != 0:
                    a = 2 * S / h1
                if S != 0 and h2 != 0:
                    b = 2 * S / h2
                if S != 0 and h3 != 0:
                    c = 2 * S / h3

                if S != 0 and a != 0:
                    h1 = 2 * S / a
                if S != 0 and b != 0:
                    h2 = 2 * S / b
                if S != 0 and c != 0:
                    h3 = 2 * S / c

                if a != 0 and b != 0 and c != 0:
                    P = a + b + c
                    p = P / 2
                    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                if h1 != 0 and h2 != 0 and h3 != 0:
                    S = (h1 * h2 * h3) ** 2 / (2 * (h1 * h2 * h3) ** 2 * (h1 ** 2 + h2 ** 2 + h3 ** 2) - (
                            h1 ** 4 * h2 ** 4 + h3 ** 4 * h2 ** 4 + h1 ** 4 * h3 ** 4)) ** 0.5
            # =======================================
            # RB
            # =======================================
            if self.triangle == "rb":
                # error
                if 2 * a <= b:
                    self.errors()
                if a and P:
                    b = P - 2 * a
                if b and P:
                    a = (P - b) / 2

                if a != 0 and h1 != 0:
                    S = 0.5 * a * h1
                if b != 0 and h2 != 0:
                    S = 0.5 * b * h2

                if S != 0 and h1 != 0:
                    a = 2 * S / h1
                if S != 0 and h2 != 0:
                    b = 2 * S / h2

                if S != 0 and a != 0:
                    h1 = 2 * S / a
                if S != 0 and b != 0:
                    h2 = 2 * S / b

                if a != 0 and b != 0:
                    P = a + b + a
                    p = P / 2
                    S = (p * (p - a) * (p - b) * (p - a)) ** 0.5

                if h1 != 0 and h2 != 0:
                    S = (h1 * h2 * h1) ** 2 / (2 * (h1 * h2 * h1) ** 2 * (h1 ** 2 + h2 ** 2 + h1 ** 2) - (
                            h1 ** 4 * h2 ** 4 + h1 ** 4 * h2 ** 4 + h1 ** 4 * h1 ** 4)) ** 0.5
            # =======================================
            # RS
            # =======================================
            if self.triangle == "rs":
                if P:
                    a = P / 3
                if a != 0 and h1 != 0:
                    S = 0.5 * a * h1

                if a != 0:
                    P = 3 * a
                    p = P / 2
                    S = (p * (p - a) ** 3) ** 0.5
                    h1 = a * (3 ** 0.5) / 2

                if S != 0 and h1 != 0:
                    a = 2 * S / h1
                if h1 != 0:
                    S = (h1 ** 3) ** 2 / (2 * (h1 ** 3) ** 2 * (3 * h1 ** 2) - (3 * h1 ** 8)) ** 0.5
            # =======================================
            # PR
            # =======================================
            if self.triangle == "pr":
                if a and P:
                    b = (2 * a * P - P ** 2) / (2 * a - 2 * P)
                if b and P:
                    a = (2 * b * P - P ** 2) / (2 * b - 2 * P)
                if c and P:
                    b = - (c - P - (c ** 2 + 2 * c * P - P ** 2) ** 0.5) / 2

                if a != 0 and b != 0 and c != 0:
                    if c ** 2 != a ** 2 + b ** 2:
                        self.errors()
                        return
                    S = a * b / 2
                    P = a + b + c
                    h1 = a * b / c
                if a != 0 and c != 0:
                    b = (c ** 2 - a ** 2) ** 0.5
                if a != 0 and b != 0:
                    c = (b ** 2 + a ** 2) ** 0.5
                if b != 0 and c != 0:
                    a = (c ** 2 - b ** 2) ** 0.5

                if h1 != 0 and c != 0:
                    S = 0.5 * c * h1
                if c != 0 and S != 0:
                    h1 = 2 * S / c
                if h1 != 0 and S != 0:
                    c = 2 * S / h1
            # =======================================
            # PR_RB
            # =======================================
            if self.triangle == "pr_rb":
                if a != 0 and c != 0:
                    if c ** 2 != a ** 2 + a ** 2:
                        self.errors()
                        return
                    S = a * a / 2
                    P = a + a + c
                    h1 = a * a / c

                if a != 0:
                    c = (a ** 2 + a ** 2) ** 0.5
                if c != 0:
                    a = (0.5 * c ** 2) ** 0.5

                if h1 != 0 and c != 0:
                    S = 0.5 * c * h1
                if c != 0 and S != 0:
                    h1 = 2 * S / c
                if h1 != 0 and S != 0:
                    c = 2 * S / h1

            # =======================================
            # ROUND
            # =======================================
            a = round(a, 4)
            b = round(b, 4)
            c = round(c, 4)
            h1 = round(h1, 4)
            h2 = round(h2, 4)
            h3 = round(h3, 4)
            S = round(S, 4)
            P = round(P, 4)
        # =======================================
        # ERRORS
        # =======================================

        fl_a = a != float(self.lineEdit.text()) and float(self.lineEdit.text()) != 0
        fl_b = b != float(self.lineEdit_2.text()) and float(self.lineEdit_2.text()) != 0
        fl_c = c != float(self.lineEdit_3.text()) and float(self.lineEdit_3.text()) != 0
        fl_h1 = h1 != float(self.lineEdit_6.text()) and float(self.lineEdit_6.text()) != 0
        fl_h2 = h2 != float(self.lineEdit_7.text()) and float(self.lineEdit_7.text()) != 0
        fl_h3 = h3 != float(self.lineEdit_9.text()) and float(self.lineEdit_9.text()) != 0
        fl_S = S != float(self.lineEdit_4.text()) and float(self.lineEdit_4.text()) != 0
        fl_P = P != float(self.lineEdit_5.text()) and float(self.lineEdit_5.text()) != 0
        if (a + b <= c or c + a <= b or b + c <= a) and a != 0 and b != 0 and c != 0:
            self.errors()
            return
        elif fl_a or fl_b or fl_c or fl_h1 or fl_h2 or fl_h3 or fl_P or fl_S:
            self.errors()
            return
        self.lineEdit.setText(str(round(a, 4)))
        self.lineEdit_2.setText(str(round(b, 4)))
        self.lineEdit_3.setText(str(round(c, 4)))
        self.lineEdit_4.setText(str(round(S, 4)))
        self.lineEdit_5.setText(str(round(P, 4)))
        self.lineEdit_6.setText(str(round(h1, 4)))
        self.lineEdit_7.setText(str(round(h2, 4)))
        self.lineEdit_9.setText(str(round(h3, 4)))

    # ================================================
