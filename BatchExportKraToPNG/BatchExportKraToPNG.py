from krita import *
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QAction,
    QCheckBox,
    QLabel,
    QListWidget,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QPushButton,
    QMessageBox,
    QFileDialog
)
from PyQt5.QtGui import QImage
import os

class BatchExportKraToPNG(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def query_directory_path(self):
        self.src_folder.setText(QFileDialog.getExistingDirectory(None, i18n("Select a folder containing .kra files"), "", QFileDialog.ShowDirsOnly))
        for file in os.listdir(self.src_folder.text()):
            filename = os.fsdecode(file)
            if filename.endswith(".kra") and not filename in self.directoryList: 
                self.directoryList.append(filename)
                self.document_layout.addWidget(QLabel(filename))
            else:
                continue

    def set_destination_Folder(self):
        self.dest_folder.setText(QFileDialog.getExistingDirectory(None, i18n("Select a folder .png files will be saved"), "", QFileDialog.ShowDirsOnly))

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
        progress_message.setText("Files will be copied to .png files. Continue?");
        progress_message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        progress_message.setIcon(QMessageBox.Information)
        return_val = progress_message.exec()
        if(return_val == QMessageBox.Cancel):
            return False
        return True

    def message_conversion_finish(self):
        done_message = QMessageBox()
        done_message.setWindowTitle('Conversion is done!')
        done_message.setText("Files were saved to \n" + self.dest_folder.text());
        done_message.setStandardButtons(QMessageBox.Close)
        done_message.setIcon(QMessageBox.Information)
        done_message.exec()

    def convert_kra_to_png(self):
        for filename in self.directoryList:
            currentDocument = Krita.instance().openDocument(self.src_folder.text() + "/" + filename)
            currentDocument.setBatchmode(True)
            exportParameters = InfoObject()
            exportParameters.setProperty("compression", 9) # 0-9
            save_directory = self.dest_folder.text() + "/" + filename.rstrip(".kra") + ".png"
            currentDocument.exportImage(save_directory, exportParameters)

    def batch_save_kra_files(self):
        if(self.src_folder.text() == ""):
            self.warning_src_folder_null()
            return
        if(self.dest_folder.text() == ""):
            self.warning_dest_folder_null()
            return
        if self.message_conversion_confirm():
            self.convert_kra_to_png()
            self.message_conversion_finish()

    def initialize(self):
        self.directoryList = []

        self.src_folder = QLabel()
        self.dest_folder = QLabel()
        self.form_layout = QFormLayout()
        self.document_layout = QVBoxLayout()
        self.widget_documents = QListWidget()

        self.browse_src_button = QPushButton("Source Folder")
        self.browse_dest_button = QPushButton("Destination Folder")
        self.save_button = QPushButton("Start Batch Save")

        self.browse_src_button.clicked.connect(self.query_directory_path)
        self.browse_dest_button.clicked.connect(self.set_destination_Folder)
        self.save_button.clicked.connect(self.batch_save_kra_files)

        self.form_layout.addRow("Documents : ", self.document_layout)
        self.form_layout.addRow("Source Folder : ", self.src_folder)
        self.form_layout.addRow("Destination Folder : ", self.dest_folder)
        self.form_layout.addRow(self.browse_src_button)
        self.form_layout.addRow(self.browse_dest_button)
        self.form_layout.addRow(self.save_button)
        self.widget_documents.setLayout(self.form_layout)

        self.widget_documents.show()

    def createActions(self, window):
        action = window.createAction("", "Batch Export .kra to .png", "tools/scripts")
        action.triggered.connect(self.initialize)

Krita.instance().addExtension(BatchExportKraToPNG(Krita.instance()))