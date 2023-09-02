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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap

class GridLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # Create 4x4 grid of push buttons
        for row in range(4):
            for col in range(4):
                button = QPushButton()
                button.setFixedSize(200, 200)  # Set button size to 200x200 pixels

                # Add an image or GIF icon to the button
                icon_path = f'path_to_icon/icon_{row * 4 + col + 1}.png'  # Replace with your icon file path
                icon = QIcon(QPixmap(icon_path))
                button.setIcon(icon)
                button.setIconSize(button.size())  # Make the icon fit the button size

                grid_layout.addWidget(button, row, col)

        self.setWindowTitle('PySide2 GridLayout Example')
        self.setGeometry(100, 100, 800, 800)

def main():
    app = QApplication(sys.argv)
    window = GridLayoutExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

