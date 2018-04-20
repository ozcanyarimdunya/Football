# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(object):
    def setup_ui(self, parent):
        parent.resize(711, 463)
        parent.setWindowTitle("Main Window")
        self.centralwidget = QtWidgets.QWidget(parent)
        parent.setCentralWidget(self.centralwidget)

        self.left_navigation(parent)
        self.right_navigation()
        QtCore.QMetaObject.connectSlotsByName(parent)

    def right_navigation(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        # Stacked Layout
        self.main_layout = QtWidgets.QStackedWidget(self.centralwidget)
        self.horizontalLayout.addWidget(self.main_layout)

        # Loading label
        self.label_loading = QtWidgets.QLabel(self.centralwidget)
        self.label_loading.setText("Loading ...")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)

        # Table widget
        self.main_table = QtWidgets.QTableWidget(self.centralwidget)
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.main_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.main_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Add Loading label and Table widget to Stacked layout
        self.main_layout.addWidget(self.label_loading)
        self.main_layout.addWidget(self.main_table)

        # (Optional) Set current index to 0 for main layout
        self.main_layout.setCurrentIndex(0)

    def left_navigation(self, parent):
        # Left Docket Widget
        self.dockWidget_Left = QtWidgets.QDockWidget(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_Left.sizePolicy().hasHeightForWidth())
        self.dockWidget_Left.setSizePolicy(sizePolicy)
        self.dockWidget_Left.setMinimumSize(QtCore.QSize(250, 500))
        self.dockWidget_Left.setMaximumSize(QtCore.QSize(250, 524287))
        self.dockWidget_Left.setSizeIncrement(QtCore.QSize(0, 0))
        self.dockWidget_Left.setFloating(False)
        self.dockWidget_Left.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_Left.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)

        # Left Docket Widget Content
        self.dockWidgetContents = QtWidgets.QWidget()

        # Vertical layout inside Left Docket Widget Content
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # Title label
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setText("Tournaments")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # List widget
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)

        # Add label and list widget to vertical
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.listWidget)
        self.dockWidget_Left.setWidget(self.dockWidgetContents)
        parent.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Left)
