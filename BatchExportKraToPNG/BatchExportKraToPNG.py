from krita import *
from PyQt5.QtWidgets import (
    QApplication, 
    QAction,
    QFileDialog
)
from . import UILayer
from PyQt5.QtGui import QImage
import os

class BatchExportKraToPNG(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def query_directory_path(self):
        self.ui_layer.src_folder.setText(QFileDialog.getExistingDirectory(None, i18n("Select a folder containing .kra files"), "", QFileDialog.ShowDirsOnly))
        for file in os.listdir(self.ui_layer.src_folder.text()):
            filename = os.fsdecode(file)
            if filename.endswith(".kra") and not filename in self.directoryList: 
                self.directoryList.append(filename)
                self.ui_layer.document_layout.addWidget(QLabel(filename))
            else:
                continue

    def set_destination_Folder(self):
        self.ui_layer.dest_folder.setText(QFileDialog.getExistingDirectory(None, i18n("Select a folder .png files will be saved"), "", QFileDialog.ShowDirsOnly))

    def warning_src_folder_null(self):
        src_null_warning = QMessageBox()
        src_null_warning.setWindowTitle('Source folder path null')
        src_null_warning.setText("Please set the source folder path");
        src_null_warning.setStandardButtons(QMessageBox.Close)
        src_null_warning.setIcon(QMessageBox.Information)
        src_null_warning.exec()

    def warning_dest_folder_null(self):
        dest_null_warning = QMessageBox()
        dest_null_warning.setWindowTitle('Destination folder path null')
        dest_null_warning.setText("Please set the destination folder path");
        dest_null_warning.setStandardButtons(QMessageBox.Close)
        dest_null_warning.setIcon(QMessageBox.Information)
        dest_null_warning.exec()

    def message_conversion_confirm(self):
        progress_message = QMessageBox()
        progress_message.setWindowTitle('Confirm')
        progress_message.setText("Files will be exported to .png files. Continue?");
        progress_message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        progress_message.setIcon(QMessageBox.Information)
        return_val = progress_message.exec()
        if(return_val == QMessageBox.Cancel):
            return False
        return True

    def message_conversion_finish(self):
        done_message = QMessageBox()
        done_message.setWindowTitle('Conversion is done!')
        done_message.setText("Files were saved to \n" + self.ui_layer.dest_folder.text());
        done_message.setStandardButtons(QMessageBox.Close)
        done_message.setIcon(QMessageBox.Information)
        done_message.exec()

    """
    compression: int (1 to 9)
    indexed: bool (True or False)
    interlaced: bool (True or False)
    saveSRGBProfile: bool (True or False)
    forceSRGB: bool (True or False)
    alpha: bool (True or False)
    transparencyFillcolor: rgb (Ex:[255,255,255])
    """
    def get_export_parameters(self):
        exportParameters = InfoObject()
        compression_int = self.ui_layer.compression_slider.value
        indexed_bool = self.ui_layer.indexed_checkbox.isChecked()
        interlaced_bool = self.ui_layer.interlaced_checkbox.isChecked()
        saveSRGBProfile_bool = self.ui_layer.saveSRGBProfile_checkbox.isChecked()
        forceSRGB_bool = self.ui_layer.forceSRGB_checkbox.isChecked()
        alpha_bool = self.ui_layer.alpha_checkbox.isChecked()
        transpFillcolor_color = self.ui_layer.transpFillcolor

        exportParameters.setProperty("compression", compression_int)
        exportParameters.setProperty("indexed", indexed_bool)
        exportParameters.setProperty("interlaced", interlaced_bool)
        exportParameters.setProperty("saveSRGBProfile", saveSRGBProfile_bool)
        exportParameters.setProperty("forceSRGB", forceSRGB_bool)
        exportParameters.setProperty("alpha", alpha_bool)
        exportParameters.setProperty("transparencyFillcolor", transpFillcolor_color)

        return exportParameters

    def convert_kra_to_png(self):
        exportParameters = self.get_export_parameters()
        for filename in self.directoryList:
            currentDocument = Krita.instance().openDocument(self.ui_layer.src_folder.text() + "/" + filename)
            currentDocument.setBatchmode(True)
            save_directory = self.ui_layer.dest_folder.text() + "/" + filename.rstrip(".kra") + ".png"
            currentDocument.exportImage(save_directory, exportParameters)

    def batch_save_kra_files(self):
        if(self.ui_layer.src_folder.text() == ""):
            self.warning_src_folder_null()
            return
        if(self.ui_layer.dest_folder.text() == ""):
            self.warning_dest_folder_null()
            return
        if self.message_conversion_confirm():
            self.convert_kra_to_png()
            self.message_conversion_finish()

    def initialize(self):
        self.directoryList = []
        self.ui_layer = UILayer.UILayer()
        self.ui_layer.initialize()

        self.ui_layer.browse_src_button.clicked.connect(self.query_directory_path)
        self.ui_layer.browse_dest_button.clicked.connect(self.set_destination_Folder)
        self.ui_layer.save_button.clicked.connect(self.batch_save_kra_files)

    def createActions(self, window):
        action = window.createAction("", "Batch Export .kra to .png", "tools/scripts")
        action.triggered.connect(self.initialize)

Krita.instance().addExtension(BatchExportKraToPNG(Krita.instance()))