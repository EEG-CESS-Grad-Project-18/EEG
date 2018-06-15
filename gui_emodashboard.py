from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import numpy as np

class Ui_emoBoard_dialog(object):
    def setupUi(self, emoBoard_dialog):
        emoBoard_dialog.setObjectName("emoBoard_dialog")
        emoBoard_dialog.resize(911, 680)
        self.channel_list = QtWidgets.QComboBox(emoBoard_dialog)
        self.channel_list.setGeometry(QtCore.QRect(620, 570, 73, 22))
        self.channel_list.setObjectName("channel_list")
        self.channel_label = QtWidgets.QLabel(emoBoard_dialog)
        self.channel_label.setGeometry(QtCore.QRect(550, 570, 55, 16))
        self.channel_label.setObjectName("channel_label")
        self.start_btn = QtWidgets.QPushButton(emoBoard_dialog)
        self.start_btn.setGeometry(QtCore.QRect(550, 620, 93, 28))
        self.start_btn.setObjectName("start_btn")
        self.pause_btn = QtWidgets.QPushButton(emoBoard_dialog)
        self.pause_btn.setGeometry(QtCore.QRect(650, 620, 93, 28))
        self.pause_btn.setObjectName("pause_btn")
        self.exit_btn = QtWidgets.QPushButton(emoBoard_dialog)
        self.exit_btn.setGeometry(QtCore.QRect(750, 620, 93, 28))
        self.exit_btn.setObjectName("exit_btn")
        self.alpha_label = QtWidgets.QLabel(emoBoard_dialog)
        self.alpha_label.setGeometry(QtCore.QRect(50, 570, 55, 16))
        self.alpha_label.setObjectName("alpha_label")
        self.beta_label = QtWidgets.QLabel(emoBoard_dialog)
        self.beta_label.setGeometry(QtCore.QRect(110, 570, 55, 16))
        self.beta_label.setObjectName("beta_label")
        self.delta_label = QtWidgets.QLabel(emoBoard_dialog)
        self.delta_label.setGeometry(QtCore.QRect(180, 570, 55, 16))
        self.delta_label.setObjectName("delta_label")
        self.gamma_label = QtWidgets.QLabel(emoBoard_dialog)
        self.gamma_label.setGeometry(QtCore.QRect(240, 570, 55, 16))
        self.gamma_label.setObjectName("gamma_label")
        self.theta_label = QtWidgets.QLabel(emoBoard_dialog)
        self.theta_label.setGeometry(QtCore.QRect(320, 570, 55, 16))
        self.theta_label.setObjectName("theta_label")
        self.signal_tabs = QtWidgets.QTabWidget(emoBoard_dialog)
        self.signal_tabs.setGeometry(QtCore.QRect(20, 70, 851, 441))
        self.signal_tabs.setObjectName("signal_tabs")
        self.tab_F34 = QtWidgets.QWidget()
        self.tab_F34.setObjectName("tab_F34")
        self.plot_widget_F34 = PlotWidget(self.tab_F34)
        self.plot_widget_F34.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_F34.sizePolicy().hasHeightForWidth())
        self.plot_widget_F34.setSizePolicy(sizePolicy)
        self.plot_widget_F34.setInteractive(True)
        self.plot_widget_F34.setObjectName("plot_widget_F34")
        self.signal_tabs.addTab(self.tab_F34, "F3-F4")
        self.tab_FC56 = QtWidgets.QWidget()
        self.tab_FC56.setObjectName("tab_FC56")
        self.plot_widget_FC56 = PlotWidget(self.tab_FC56)
        self.plot_widget_FC56.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_FC56.sizePolicy().hasHeightForWidth())
        self.plot_widget_FC56.setSizePolicy(sizePolicy)
        self.plot_widget_FC56.setInteractive(True)
        self.plot_widget_FC56.setObjectName("plot_widget_FC56")
        self.signal_tabs.addTab(self.tab_FC56, "FC5-FC6")
        self.tab_AF34 = QtWidgets.QWidget()
        self.tab_AF34.setObjectName("tab_AF34")
        self.plot_widget_AF34 = PlotWidget(self.tab_AF34)
        self.plot_widget_AF34.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_AF34.sizePolicy().hasHeightForWidth())
        self.plot_widget_AF34.setSizePolicy(sizePolicy)
        self.plot_widget_AF34.setInteractive(True)
        self.plot_widget_AF34.setObjectName("plot_widget_AF34")
        self.signal_tabs.addTab(self.tab_AF34, "AF3-AF4")
        self.tab_F78 = QtWidgets.QWidget()
        self.tab_F78.setObjectName("tab_F78")
        self.plot_widget_F78 = PlotWidget(self.tab_F78)
        self.plot_widget_F78.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_F78.sizePolicy().hasHeightForWidth())
        self.plot_widget_F78.setSizePolicy(sizePolicy)
        self.plot_widget_F78.setInteractive(True)
        self.plot_widget_F78.setObjectName("plot_widget_F78")
        self.signal_tabs.addTab(self.tab_F78, "F7-F8")
        self.tab_T78 = QtWidgets.QWidget()
        self.tab_T78.setObjectName("tab_T78")
        self.plot_widget_T78 = PlotWidget(self.tab_T78)
        self.plot_widget_T78.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_T78.sizePolicy().hasHeightForWidth())
        self.plot_widget_T78.setSizePolicy(sizePolicy)
        self.plot_widget_T78.setInteractive(True)
        self.plot_widget_T78.setObjectName("plot_widget_T78")
        self.signal_tabs.addTab(self.tab_T78, "T7-T8")
        self.tab_P78 = QtWidgets.QWidget()
        self.tab_P78.setObjectName("tab_P78")
        self.plot_widget_P78 = PlotWidget(self.tab_P78)
        self.plot_widget_P78.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_P78.sizePolicy().hasHeightForWidth())
        self.plot_widget_P78.setSizePolicy(sizePolicy)
        self.plot_widget_P78.setInteractive(True)
        self.plot_widget_P78.setObjectName("plot_widget_P78")
        self.signal_tabs.addTab(self.tab_P78, "P7-P8")
        self.tab_O12 = QtWidgets.QWidget()
        self.tab_O12.setObjectName("tab_O12")
        self.plot_widget_O12 = PlotWidget(self.tab_O12)
        self.plot_widget_O12.setGeometry(QtCore.QRect(10, 10, 821, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget_O12.sizePolicy().hasHeightForWidth())
        self.plot_widget_O12.setSizePolicy(sizePolicy)
        self.plot_widget_O12.setInteractive(True)
        self.plot_widget_O12.setObjectName("plot_widget_O12")
        self.signal_tabs.addTab(self.tab_O12, "O1-O2")

        """Remove curve and data to seperate class"""
        self.curve1 = self.plot_widget_F34.plot(pen='r')
        self.curve2 = self.plot_widget_F34.plot(pen='g')
        self.data = [0]

        self.retranslateUi(emoBoard_dialog)
        self.signal_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(emoBoard_dialog)

    def retranslateUi(self, emoBoard_dialog):
        _translate = QtCore.QCoreApplication.translate
        emoBoard_dialog.setWindowTitle(_translate("emoBoard_dialog", "EmoDashboard"))
        self.channel_list.setToolTip(_translate("emoBoard_dialog", "<html><head/><body><p>F3</p><p>FC5 </p><p>AF3 </p><p>F7 </p><p>T7 </p><p>P7 </p><p>O1</p><p>F4 </p><p>FC6 </p><p>AF4 </p><p>F8 </p><p>T8 </p><p>P8 </p><p>O2</p></body></html>"))
        self.channel_label.setText(_translate("emoBoard_dialog", "Channel"))
        self.start_btn.setText(_translate("emoBoard_dialog", "Start"))
        self.pause_btn.setText(_translate("emoBoard_dialog", "Stop"))
        self.exit_btn.setText(_translate("emoBoard_dialog", "Exit"))
        self.alpha_label.setText(_translate("emoBoard_dialog", "Alpha"))
        self.beta_label.setText(_translate("emoBoard_dialog", "Beta"))
        self.delta_label.setText(_translate("emoBoard_dialog", "Delta"))
        self.gamma_label.setText(_translate("emoBoard_dialog", "Gamma"))
        self.theta_label.setText(_translate("emoBoard_dialog", "Theta"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_F34), _translate("emoBoard_dialog", "F3-F4"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_FC56), _translate("emoBoard_dialog", "FC5-FC6"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_AF34), _translate("emoBoard_dialog", "AF3-AF4"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_F78), _translate("emoBoard_dialog", "F7-F8"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_T78), _translate("emoBoard_dialog", "T7-T8"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_P78), _translate("emoBoard_dialog", "P7-P8"))
        self.signal_tabs.setTabText(self.signal_tabs.indexOf(self.tab_O12), _translate("emoBoard_dialog", "O1-O2"))

    def draw(self):
        line = '56'
        self.data.append(int(line))
        xdata1 = np.array(self.data, dtype='float64')
        line = '6'
        self.data.append(int(line))
        xdata2 = np.array(self.data, dtype='float64')
        self.curve1.setData(xdata1)
        self.curve2.setData(xdata2)
        sleep(0.5)
        app.processEvents()
        

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emoBoard_dialog = QtWidgets.QDialog()
    ui = Ui_emoBoard_dialog()
    ui.setupUi(emoBoard_dialog)
    emoBoard_dialog.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.draw)
    timer.start(0)
    sys.exit(app.exec_())
