import sys
import os
import time
import glob
from PIL import Image
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QCheckBox, QMessageBox,QProgressBar
from ImageProcessor import ImageProcessor
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from ImageProcessingThread import ImageProcessingThread


class ImageProcessingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Processing App")
        self.resize(800, 300)

        self.input_folder = os.path.join("D:\garbage-20230421T030613Z-001\garbage")
        self.filter_list = "_ch,promo_,b."
        self.output_folder = "D:\garbage-20230421T030613Z-001\garbage_dataset"
        self.size = 500
        self.split_ratio = 0.99
        self.cleanup_process = False
        self.image_processing_thread = None
        
        self.input_folder_label = QLabel("Input Folder:")
        self.input_folder_edit = QLineEdit()
        self.input_folder_button = QPushButton("Browse")
        self.input_folder_button.clicked.connect(self.browse_input_folder)
        
        self.filter_list_label = QLabel("Unwanted List:")
        self.filter_list_edit = QLineEdit(str(self.filter_list))
        
        self.output_folder_label = QLabel("Output Folder:")
        self.output_folder_edit = QLineEdit()
        self.output_folder_button = QPushButton("Browse")
        self.output_folder_button.clicked.connect(self.browse_output_folder)

        self.size_label = QLabel("Desired Size:")
        self.size_edit = QLineEdit(str(self.size))

        self.split_ratio_label = QLabel("Split Ratio:")
        self.split_ratio_edit = QLineEdit(str(self.split_ratio))

        self.cleanup_checkbox = QCheckBox("Cleanup")
        self.cleanup_checkbox.setChecked(False)

        self.process_button = QPushButton("Process Images")
        self.process_button.clicked.connect(self.process_images)

        # Create progress bars for resize, sketch, combine, and split processes
        self.progress_filter_bar = QProgressBar(self)
        self.progress_filter_bar.setAlignment(Qt.AlignCenter)
        self.progress_resize_bar = QProgressBar(self)
        self.progress_resize_bar.setAlignment(Qt.AlignCenter)
        self.progress_sketch_bar = QProgressBar(self)
        self.progress_sketch_bar.setAlignment(Qt.AlignCenter)
        self.progress_combine_bar = QProgressBar(self)
        self.progress_combine_bar.setAlignment(Qt.AlignCenter)
        self.progress_split_bar = QProgressBar(self)
        self.progress_split_bar.setAlignment(Qt.AlignCenter)
        self.process_state_label = QLabel("State:")


        # Create a vertical layout and add the labels, line edits, and buttons
        layout = QVBoxLayout()
        layout.addWidget(self.input_folder_label)
        layout.addWidget(self.input_folder_edit)
        layout.addWidget(self.input_folder_button)
        layout.addWidget(self.filter_list_label)
        layout.addWidget(self.filter_list_edit)
        layout.addWidget(self.output_folder_label)
        layout.addWidget(self.output_folder_edit)
        layout.addWidget(self.output_folder_button)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_edit)
        layout.addWidget(self.split_ratio_label)
        layout.addWidget(self.split_ratio_edit)
        layout.addWidget(self.cleanup_checkbox)
        layout.addWidget(self.process_button)
        layout.addWidget(self.progress_filter_bar)
        layout.addWidget(self.progress_resize_bar)
        layout.addWidget(self.progress_sketch_bar)
        layout.addWidget(self.progress_combine_bar)
        layout.addWidget(self.progress_split_bar)
        layout.addWidget(self.process_state_label)

        
        self.setLayout(layout)

    def browse_input_folder(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(self, "Select Input Folder")
        self.input_folder_edit.setText(folder_path)

    def browse_output_folder(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(self, "Select Output Folder")
        self.output_folder_edit.setText(folder_path)
        
    def process_images(self):
        self.input_folder = self.input_folder_edit.text()
        self.filter_list = self.filter_list_edit.text().split(",")
        self.output_folder = self.output_folder_edit.text()
        self.size = int(self.size_edit.text())
        self.split_ratio = float(self.split_ratio_edit.text())
        self.cleanup_process = self.cleanup_checkbox.isChecked()

        self.image_processing_thread = ImageProcessingThread(
            input_folder=self.input_folder,
            filter_list=self.filter_list,
            output_folder=self.output_folder,
            size=self.size,
            split_ratio=self.split_ratio,
            cleanup_process=self.cleanup_process
        )

        # Connect the progress signals to the corresponding progress bars
        self.image_processing_thread.progress_filter.connect(self.progress_filter_bar.setValue)
        self.image_processing_thread.progress_resize.connect(self.progress_resize_bar.setValue)
        self.image_processing_thread.progress_sketch.connect(self.progress_sketch_bar.setValue)
        self.image_processing_thread.progress_combine.connect(self.progress_combine_bar.setValue)
        self.image_processing_thread.progress_split.connect(self.progress_split_bar.setValue)

        # Start the image processing thread
        self.image_processing_thread.start()

    def closeEvent(self, event):
        if self.image_processing_thread is not None and self.image_processing_thread.running:
            self.image_processing_thread.stop()
            self.image_processing_thread.wait()
        event.accept()

    def run(self):
        # Execute the application
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    # Create an instance of the ImageProcessingApp
    app = QApplication([])
    image_app = ImageProcessingApp()

    # Run the application
    image_app.run()
