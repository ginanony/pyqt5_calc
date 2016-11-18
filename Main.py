# -*- coding:utf-8 -*-
import sys,math

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class MainWindows(QtWidgets.QWidget):
    """主窗口程序"""
    def __init__(self):
        QWidget.__init__(self)

        self.m_DragPosition = self.pos()

        self.resize(800,600)
        self.setWindowFlags(Qt.FramelessWindowHint |Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet("")
