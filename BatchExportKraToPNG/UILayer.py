import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QWidget,
    QListWidget,
    QMainWindow,
    QCheckBox,
    QPushButton,
    QMessageBox,
    QLabel,
    QSlider,
    QColorDialog,
    QDialog
)
class DocumentToolsDialog(QDialog):
    def __init__(self, parent=None):
        super(DocumentToolsDialog, self).__init__(parent)

    def closeEvent(self, event):
        event.accept()

class UILayer(object):
    def __init__(self):
        self.main_dialog = DocumentToolsDialog()
        self.main_dialog.setFixedWidth(700)
        self.main_dialog.setFixedHeight(700)
        self.main_dialog.setWindowTitle("Batch Export .kra to .png")

        self.src_folder = QLabel()
        self.dest_folder = QLabel()
        self.main_layout = QVBoxLayout(self.main_dialog)
        self.document_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.document_widget = QListWidget()

        self.browse_src_button = QPushButton("Source Folder")
        self.browse_dest_button = QPushButton("Destination Folder")
        self.save_button = QPushButton("Start Batch Save")

        self.compression_layout = QHBoxLayout()

        self.compression_label = QLabel()
        self.compression_slider = QSlider(Qt.Horizontal)
        self.compression_slider.setRange(1,9)
        self.compression_slider.setSingleStep(1)

        self.compression_layout.addWidget(self.compression_label)
        self.compression_layout.addWidget(self.compression_slider)

        self.indexed_checkbox = QCheckBox()
        self.interlaced_checkbox = QCheckBox()
        self.saveSRGBProfile_checkbox = QCheckBox()
        self.forceSRGB_checkbox = QCheckBox()
        self.alpha_checkbox = QCheckBox()
        self.transpFillcolor_button = QPushButton()
        self.transpFillcolor_dialog = QColorDialog()
        self.transpFillcolor = QColor()

        self.indexed_checkbox.setStyleSheet("\
                QCheckBox::indicator { border: 1px solid; border-color: grey; }\
                QCheckBox::indicator:checked { background-color: green; }\
            ");
        self.interlaced_checkbox.setStyleSheet("\
                QCheckBox::indicator { border: 1px solid; border-color: grey; }\
                QCheckBox::indicator:checked { background-color: green; }\
            ");
        self.saveSRGBProfile_checkbox.setStyleSheet("\
                QCheckBox::indicator { border: 1px solid; border-color: grey; }\
                QCheckBox::indicator:checked { background-color: green; }\
            ");
        self.forceSRGB_checkbox.setStyleSheet("\
                QCheckBox::indicator { border: 1px solid; border-color: grey; }\
                QCheckBox::indicator:checked { background-color: green; }\
            ");
        self.alpha_checkbox.setStyleSheet("\
                QCheckBox::indicator { border: 1px solid; border-color: grey; }\
                QCheckBox::indicator:checked { background-color: green; }\
            ");

    def initialize(self):
        self.form_layout.addRow("Documents : ", self.document_layout)
        self.form_layout.addRow("Source Folder : ", self.src_folder)
        self.form_layout.addRow("Destination Folder : ", self.dest_folder)
        self.form_layout.addRow(self.browse_src_button)
        self.form_layout.addRow(self.browse_dest_button)

        self.form_layout.addRow("Compression (Lossless) ", self.compression_layout)
        self.form_layout.addRow("Save as indexed PNG, if possible ", self.indexed_checkbox)
        self.form_layout.addRow("Interlacing ", self.interlaced_checkbox)
        self.form_layout.addRow("Embed sRGB profile ", self.saveSRGBProfile_checkbox)
        self.form_layout.addRow("Force convert to sRGB ", self.forceSRGB_checkbox)
        self.form_layout.addRow("Store alpha channel (transparency) ", self.alpha_checkbox)
        self.form_layout.addRow("Transparent fill color ", self.transpFillcolor_button)

        self.form_layout.addRow(self.save_button)
        self.document_widget.setLayout(self.form_layout)
        self.main_layout.addWidget(self.document_widget)
        self.main_dialog.show()
        self.update_compression_label()
        self.compression_slider.valueChanged.connect(self.update_compression_label)
        self.transpFillcolor_button.clicked.connect(self.set_transpFillColor)

    def set_transpFillColor(self):
        self.transpFillcolor = self.transpFillcolor_dialog.getColor()
        self.transpFillcolor_button.setStyleSheet("background-color:" + self.transpFillcolor.name());

    def update_compression_label(self):
        self.compression_label.setText(str(self.compression_slider.value()))