from PyQt5.QtCore import QThread, pyqtSignal
from ImageProcessor import ImageProcessor

class ImageProcessingThread(QThread):
    progress_filter = pyqtSignal(int)
    progress_resize = pyqtSignal(int)
    progress_sketch = pyqtSignal(int)
    progress_combine = pyqtSignal(int)
    progress_split = pyqtSignal(int)

    def __init__(self, input_folder, filter_list, output_folder, size, split_ratio, cleanup_process):
        super().__init__()
        self.input_folder = input_folder
        self.filter_list = filter_list
        self.output_folder = output_folder
        self.size = size
        self.split_ratio = split_ratio
        self.cleanup_process = cleanup_process
        self.running = False

    def run(self):
        self.running = True

        processor = ImageProcessor(
            color_folder=self.input_folder,
            filter_list = self.filter_list,
            output_folder=self.output_folder,
            size=self.size,
            split_ratio=self.split_ratio,
            remove_process_files=self.cleanup_process
        )

        # Connect the progress signals to the corresponding progress bars
        processor.progress_filter.connect(self.progress_filter.emit)
        processor.progress_resize.connect(self.progress_resize.emit)
        processor.progress_sketch.connect(self.progress_sketch.emit)
        processor.progress_combine.connect(self.progress_combine.emit)
        processor.progress_split.connect(self.progress_split.emit)

        # Execute the image processing operations
        processor.run()

        self.running = False

    def stop(self):
        self.running = False

    def __del__(self):
        self.wait()
