import os, sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea
import random

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.vvbox = QVBoxLayout(self)
        self.scrollarea = QScrollArea()
        self.scrollarea.setStyleSheet("""
                                                QScrollBar:vertical {
                                                    width: 14px;
                                                    margin: 16px 2px 16px 2px;
                                                    border: 1px solid #f09ea3;
                                                    border-radius: 4px;
                                                }


                                                QScrollBar::handle:vertical {
                                                    background-color: #f1c1bf;
                                                    border: 0px solid #31363B;
                                                    min-height: 8px;
                                                    border-radius: 4px;
                                                }

                                                QScrollBar::handle:vertical:hover {
                                                    background-color: #f4726e;
                                                    border: 0px solid #179AE0;
                                                    border-radius: 4px;
                                                    min-height: 8px;
                                                }

                                                QScrollBar::sub-line:vertical {
                                                    margin: 3px 0px 3px 0px;
                                                    border-image: url(icons/up_arrow_disabled.png);
                                                    height: 10px;
                                                    width: 10px;
                                                    subcontrol-position: top;
                                                    subcontrol-origin: margin;
                                                }

                                                QScrollBar::add-line:vertical {
                                                    margin: 3px 0px 3px 0px;
                                                    border-image: url(icons/down_arrow_disabled.png);
                                                    height: 10px;
                                                    width: 10px;
                                                    subcontrol-position: bottom;
                                                    subcontrol-origin: margin;
                                                }

                                                QScrollBar::sub-line:vertical:hover,
                                                QScrollBar::sub-line:vertical:on {
                                                    border-image: url(icons/up_arrow.png);
                                                    height: 10px;
                                                    width: 10px;
                                                    subcontrol-position: top;
                                                    subcontrol-origin: margin;
                                                }

                                                QScrollBar::add-line:vertical:hover,
                                                QScrollBar::add-line:vertical:on {
                                                    border-image: url(/icons/down_arrow.png);
                                                    height: 10px;
                                                    width: 10px;
                                                    subcontrol-position: bottom;
                                                    subcontrol-origin: margin;
                                                }

                                                QScrollBar::up-arrow:vertical,
                                                QScrollBar::down-arrow:vertical {
                                                    background: none;
                                                }

                                                QScrollBar::add-page:vertical,
                                                QScrollBar::sub-page:vertical {
                                                    background: none;
                                                }
                                            """)
        self.scrollarea.setFixedWidth(300)
        self.area = QWidget()
        self.label_box = QVBoxLayout()
        self.label_box.addStretch(-1)

        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setFixedSize(self.scrollarea.width(), 30)
        self.textBrowser.setReadOnly(False)

        self.area.setLayout(self.label_box)
        self.scrollarea.setWidget(self.area)
        self.scrollarea.setWidgetResizable(True)
        self.vvbox.addWidget(self.scrollarea)
        self.vvbox.addWidget(self.textBrowser)


        self.resize(300, 500)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.create_label()


    def create_label(self):
        label = QLabel()
        label.setFixedWidth(self.area.width() - 60)
        label.setText(str(random.random()))
        label.setStyleSheet('''
                        font: 13pt "Montserrat Alternates";
                        background-color: #414547;
                        color: #efe2cd;
                        padding: 5;
                        border: 1px solid #f09ea3;
                        border-radius: 10px;
                            ''')
        self.label_box.addWidget(label)
        self.scrollarea.verticalScrollBar().setSliderPosition(self.scrollarea.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
