import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow
from ImageProcessingApp import ImageProcessingApp


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("MultiTool")
    window.setGeometry(100, 100, 800, 600)

    # Create the MDI area
    mdi_area = QMdiArea()
    window.setCentralWidget(mdi_area)

    # Create the ImageProcessingApp widget
    image_processing_widget = ImageProcessingApp()

    # Create an MDI subwindow for the ImageProcessingApp widget
    sub_window = QMdiSubWindow()
    sub_window.setWidget(image_processing_widget)

    # Add the subwindow to the MDI area
    mdi_area.addSubWindow(sub_window)

    # Show the main window
    window.show()

    # Execute the application
    sys.exit(app.exec_())

