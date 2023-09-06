# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem


# import cv2
# import os

# class ImageSequencePlayer:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.image_files = sorted([f for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg", ".bmp"))])
#         self.current_frame_index = 0
#         self.drawing = False
#         self.annotation = ""

#         cv2.namedWindow("Image Sequence Player")
#         cv2.setMouseCallback("Image Sequence Player", self.on_mouse_event)

#     def on_mouse_event(self, event, x, y, flags, param):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             self.drawing = True
#         elif event == cv2.EVENT_LBUTTONUP:
#             self.drawing = False
#         elif event == cv2.EVENT_MOUSEMOVE:
#             if self.drawing:
#                 cv2.circle(self.image, (x, y), 5, (0, 255, 0), -1)

#     def play(self):
#         for image_file in self.image_files:
#             image_path = os.path.join(self.folder_path, image_file)
#             self.image = cv2.imread(image_path)

#             if self.image is not None:
#                 self.show_frame()
#                 key = cv2.waitKey(0) & 0xFF

#                 # Save annotated frame if 's' key is pressed
#                 if key == ord('s'):
#                     output_file = os.path.splitext(image_file)[0] + "_annotated.jpg"
#                     output_path = os.path.join(self.folder_path, output_file)
#                     cv2.imwrite(output_path, self.image)

#                 # Quit if 'q' key is pressed
#                 if key == ord('q'):
#                     break

#         cv2.destroyAllWindows()

#     def show_frame(self):
#         cv2.putText(self.image, "Press 's' to save, 'q' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
#         cv2.imshow("Image Sequence Player", self.image)

# if __name__ == "__main__":
#     folder_path = "D:/test_seq/v002"
#     player = ImageSequencePlayer(folder_path)
#     player.play()

# os.system("Houdini")


# import sys
# from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QSlider
# from PySide2.QtGui import QIcon, QPixmap
# from PySide2.QtCore import Qt

# class GridLayoutExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         main_layout = QVBoxLayout()
#         central_widget.setLayout(main_layout)

#         self.grid_layout = QGridLayout()
#         main_layout.addLayout(self.grid_layout)

#         self.slider = QSlider(Qt.Vertical)
#         self.slider.setMinimum(1)
#         self.slider.setMaximum(16)
#         self.slider.setValue(16)
#         self.slider.valueChanged.connect(self.updateButtons)

#         main_layout.addWidget(self.slider)

#         # Create 16 buttons by default
#         self.createButtons(25)

#         self.setWindowTitle('PySide2 GridLayout Example')
#         self.setGeometry(100, 100, 800, 800)

#     def createButtons(self, num_buttons):
#         # Clear existing buttons from the grid layout
#         for i in reversed(range(self.grid_layout.count())):
#             widget = self.grid_layout.itemAt(i).widget()
#             if widget is not None:
#                 widget.deleteLater()

#         # Create buttons and add them to the grid layout
#         for row in range(4):
#             for col in range(4):
#                 button_num = row * 4 + col + 1
#                 if button_num <= num_buttons:
#                     button = QPushButton()
#                     button.setFixedSize(200, 200)
#                     icon_path = f'path_to_icon/icon_{button_num}.png'
#                     icon = QIcon(QPixmap(icon_path))
#                     button.setIcon(icon)
#                     button.setIconSize(button.size())
#                     self.grid_layout.addWidget(button, row, col)

#     def updateButtons(self):
#         num_buttons = self.slider.value()
#         self.createButtons(num_buttons)

# def main():
#     app = QApplication(sys.argv)
#     window = GridLayoutExample()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QSlider, QVBoxLayout
from PySide2.QtGui import QIcon, QPixmap
from PySide2 import QtUiTools

class GridLayoutExample(QMainWindow):
    def __init__(self, ui_file):
        super().__init__()

        # Load the UI file created with Qt Designer
        loader = QtUiTools.QUiLoader()
        self.central_widget = loader.load(ui_file)
        self.setCentralWidget(self.central_widget)

        # Access the QWidget where you want to add the grid layout
        self.grid_widget = self.central_widget.findChild(QWidget, 'gridWidget')

        # Initialize button count and slider position
        self.button_count = 16
        self.slider = self.central_widget.findChild(QSlider, 'slider')
        self.slider.setRange(0, self.button_count - 1)
        self.slider.valueChanged.connect(self.onSliderValueChanged)

        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout to hold the grid layout and slider
        layout = QVBoxLayout()
        self.grid_widget.setLayout(layout)

        # Create the grid layout
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.buttons = []

        # Create 4x4 grid of push buttons
        for row in range(4):
            for col in range(4):
                button_number = row * 4 + col + 1
                if button_number <= self.button_count:
                    button = QPushButton()
                    button.setFixedSize(200, 200)  # Set button size to 200x200 pixels

                    # Add an image or GIF icon to the button
                    icon_path = f'path_to_icon/icon_{button_number}.png'  # Replace with your icon file path
                    icon = QIcon(QPixmap(icon_path))
                    button.setIcon(icon)
                    button.setIconSize(button.size())  # Make the icon fit the button size

                    grid_layout.addWidget(button, row, col)
                    self.buttons.append(button)

        self.setWindowTitle('PySide2 GridLayout Example')
        self.setGeometry(100, 100, 800, 800)

    def onSliderValueChanged(self, value):
        # Handle slider value change to scroll through buttons
        for button in self.buttons:
            button.setVisible(False)

        for i in range(value, min(value + 16, self.button_count)):
            self.buttons[i].setVisible(True)

def main():
    app = QApplication(sys.argv)
    # ui_file = 'your_ui_file.ui'  # Replace with the path to your UI file
    ui_file = "E:\Work\python_dev\QT_project_launcher\qt_ui_files\hou_tools_ui\crowd_preview.ui"

    window = GridLayoutExample(ui_file)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
