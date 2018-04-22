# -*- coding: utf-8 -*-
from PyQt5.QtCore import QMetaObject, Qt, QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QStackedWidget, QLabel, QTableWidget, QDockWidget, QSizePolicy, \
    QVBoxLayout, QListWidget


class MainWindow(object):
    def setup_ui(self, parent):
        parent.resize(711, 463)
        parent.setWindowTitle("Main Window")
        self.centralwidget = QWidget(parent)
        parent.setCentralWidget(self.centralwidget)

        self.left_navigation(parent)
        self.right_navigation()
        QMetaObject.connectSlotsByName(parent)

    def right_navigation(self):
        self.horizontalLayout = QHBoxLayout(self.centralwidget)

        # Stacked Layout
        self.main_layout = QStackedWidget(self.centralwidget)
        self.horizontalLayout.addWidget(self.main_layout)

        # Loading label
        self.label_loading = QLabel(self.centralwidget)
        self.label_loading.setText("Loading ...")
        self.label_loading.setAlignment(Qt.AlignCenter)

        # Table widget
        self.main_table = QTableWidget(self.centralwidget)
        self.main_table.setColumnCount(0)
        self.main_table.setRowCount(0)
        self.main_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.main_table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Add Loading label and Table widget to Stacked layout
        self.main_layout.addWidget(self.label_loading)
        self.main_layout.addWidget(self.main_table)

        # (Optional) Set current index to 0 for main layout
        self.main_layout.setCurrentIndex(0)

    def left_navigation(self, parent):
        # Left Docket Widget
        self.dockWidget_Left = QDockWidget(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_Left.sizePolicy().hasHeightForWidth())
        self.dockWidget_Left.setSizePolicy(sizePolicy)
        self.dockWidget_Left.setMinimumSize(QSize(250, 500))
        self.dockWidget_Left.setMaximumSize(QSize(250, 524287))
        self.dockWidget_Left.setSizeIncrement(QSize(0, 0))
        self.dockWidget_Left.setFloating(False)
        self.dockWidget_Left.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_Left.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # Left Docket Widget Content
        self.dockWidgetContents = QWidget()

        # Vertical layout inside Left Docket Widget Content
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # Title label
        self.label = QLabel(self.dockWidgetContents)
        self.label.setText("Tournaments")
        self.label.setAlignment(Qt.AlignCenter)

        # List widget
        self.listWidget = QListWidget(self.dockWidgetContents)

        # Add label and list widget to vertical
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.listWidget)
        self.dockWidget_Left.setWidget(self.dockWidgetContents)
        parent.addDockWidget(Qt.DockWidgetArea(1), self.dockWidget_Left)
