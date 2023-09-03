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

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QSlider
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt

class GridLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        self.slider = QSlider(Qt.Vertical)
        self.slider.setMinimum(1)
        self.slider.setMaximum(16)
        self.slider.setValue(16)
        self.slider.valueChanged.connect(self.updateButtons)

        main_layout.addWidget(self.slider)

        # Create 16 buttons by default
        self.createButtons(20)

        self.setWindowTitle('PySide2 GridLayout Example')
        self.setGeometry(100, 100, 800, 800)

    def createButtons(self, num_buttons):
        # Clear existing buttons from the grid layout
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Create buttons and add them to the grid layout
        for row in range(4):
            for col in range(4):
                button_num = row * 4 + col + 1
                if button_num <= num_buttons:
                    button = QPushButton()
                    button.setFixedSize(200, 200)
                    icon_path = f'path_to_icon/icon_{button_num}.png'
                    icon = QIcon(QPixmap(icon_path))
                    button.setIcon(icon)
                    button.setIconSize(button.size())
                    self.grid_layout.addWidget(button, row, col)

    def updateButtons(self):
        num_buttons = self.slider.value()
        self.createButtons(num_buttons)

def main():
    app = QApplication(sys.argv)
    window = GridLayoutExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


