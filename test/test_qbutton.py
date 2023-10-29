# import typing
# from PySide2 import QtWidgets,QtCore,QtGui
# import PySide2.QtCore
# import PySide2.QtWidgets

# class window(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100,100,600,500)

#         vbox = QtWidgets.QGridLayout()

#         btn_names = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8","Item 8","Item 8","Item 8","Item 8","Item 8", "Item 6", "Item 7", "Item 8","Item 8","Item 8","Item 8","Item 8","Item 8"]
        
#         #Create Button Co-ordinate
#         num_cols = 4
#         num_rows = (len(btn_names) + num_cols - 1) // num_cols

        
#         for row in range(num_rows):
#             for col in range(num_cols):
#                 index = row * num_cols + col
                
#                 if index < len(btn_names):
#                     item = btn_names[index]
                    
#                     #Create Button 
#                     button = QtWidgets.QPushButton("",self)
#                     button.setIcon(QtGui.QIcon("D:/test_seq/test_explosion_v002.jpg"))
#                     # button.setIcon(QtGui.QIcon("D:/test_seq/explosion_gif.gif"))
#                     button.setIconSize(QtCore.QSize(200,200))

#                     print(row,col)

#                     vbox.addWidget(button,row,col)

#         self.setLayout(vbox)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication()
#     win = window()
#     win.show()
#     app.exec_()


# import sys
# from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

#     def createButtons(self, button_count):
#         # Clear the layout to remove existing buttons
#         self.clearLayout()

#         # Create and add new buttons
#         for i in range(button_count):
#             button = QPushButton(f"Button {i+1}")
#             self.layout.addWidget(button)

#     def clearLayout(self):
#         # Remove all widgets from the layout
#         while self.layout.count():
#             item = self.layout.takeAt(0)
#             widget = item.widget()
#             if widget:
#                 widget.deleteLater()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWidget()
#     window.show()


## Video player using QLABEL
# import sys
# import cv2
# from PySide2.QtCore import QTimer
# from PySide2.QtGui import QImage, QPixmap
# from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

# class VideoPlayerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Video Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a central widget
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         # Create a vertical layout
#         layout = QVBoxLayout(central_widget)

#         # Create a label to display video frames
#         self.video_label = QLabel()
#         layout.addWidget(self.video_label)

#         # Set the central widget layout
#         central_widget.setLayout(layout)

#         # Open a video file (replace with your video file path)
#         self.cap = cv2.VideoCapture("D:/test_seq/test_explosion_v012.mp4")

#         # Create a timer to update the video frames
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(1000 // 30)  # Set the timer interval (30 FPS)

#     def update_frame(self):
#         # Read a frame from the video capture
#         ret, frame = self.cap.read()

#         if ret:
#             # Correct the color channel ordering (BGR to RGB)
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             # Convert the OpenCV frame to a QImage
#             height, width, channel = frame_rgb.shape
#             bytes_per_line = 3 * width
#             q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

#             # Display the QImage in the QLabel
#             pixmap = QPixmap.fromImage(q_image)
#             self.video_label.setPixmap(pixmap)

#         else:
#             # Video playback is finished, reset to the beginning and continue
#             self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     player = VideoPlayerApp()
#     player.show()
#     sys.exit(app.exec_())


#Videoplayer using QPUSHBUTTON
# import sys
# import cv2
# from PySide2.QtCore import Qt, QTimer
# from PySide2.QtGui import QImage, QPixmap,QIcon
# from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

# class VideoButton(QPushButton):
#     def __init__(self):
#         super().__init__()

#         # Open a video file (replace with your video file path)
#         self.cap = cv2.VideoCapture("D:/test_seq/test_explosion_v012.mp4")

#         # Create a timer to update the video frames
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(1000 // 30)  # Set the timer interval (30 FPS)

#     def update_frame(self):
#         # Read a frame from the video capture
#         ret, frame = self.cap.read()

#         if ret:
#             # Correct the color channel ordering (BGR to RGB)
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             # Convert the OpenCV frame to a QImage
#             height, width, channel = frame_rgb.shape
#             bytes_per_line = 3 * width
#             q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

#             # Set the image as the button's icon
#             pixmap = QPixmap.fromImage(q_image)
#             self.setIcon(QIcon(pixmap))
#             self.setIconSize(pixmap.size())

#         else:
#             # Video playback is finished, reset to the beginning and continue
#             self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# class VideoPlayerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Video Player")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a central widget
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         # Create a vertical layout
#         layout = QVBoxLayout(central_widget)

#         # Create a custom video button
#         self.video_button = VideoButton()
#         layout.addWidget(self.video_button)

#         # Set the central widget layout
#         central_widget.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     player = VideoPlayerApp()
#     player.show()
#     sys.exit(app.exec_())


import sys
import cv2
from PySide2.QtCore import QTimer,QSize
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout

class VideoPlayerWidget(QWidget):
    def __init__(self, video_path, target_size):
        super().__init__()

        # Open a video file
        self.cap = cv2.VideoCapture(video_path)

        # Set the target size for video frames
        self.target_size = target_size

        # Create a timer to update the video frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 30)  # Set the timer interval (30 FPS)

        # Create a QPushButton to display video frames
        self.video_button = QPushButton(self)
        self.video_button.setIconSize(QSize(self.target_size[0],self.target_size[1]))

        # Set the layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.video_button)
        self.setLayout(layout)

    def update_frame(self):
        # Read a frame from the video capture
        ret, frame = self.cap.read()

        if ret:
            # Resize the frame to the target size
            frame_resized = cv2.resize(frame, self.target_size)

            # Correct the color channel ordering (BGR to RGB)
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

            # Convert the OpenCV frame to a QImage
            height, width, channel = frame_rgb.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Set the image as the button's icon
            pixmap = QPixmap.fromImage(q_image)
            self.video_button.setIcon(QIcon(pixmap))
            self.video_button.setIconSize(QSize(self.target_size[0],self.target_size[1]))

            self.video_button.setCheckable(True)
            self.video_button.setChecked(False)

        else:
            # Video playback is finished, reset to the beginning and continue
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

class VideoPlayerApp(QMainWindow):
    def __init__(self, video_paths, target_sizes):
        super().__init__()

        self.setWindowTitle("Multi-Video Player")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a grid layout to arrange the video players
        grid_layout = QGridLayout(central_widget)

        # Create and add video player widgets for each video path
        row, col = 0, 0
        for video_path, target_size in zip(video_paths, target_sizes):
            video_widget = VideoPlayerWidget(video_path, target_size)
            grid_layout.addWidget(video_widget, row, col)
            col += 1
            if col == 2:  # Adjust the number of columns as needed
                col = 0
                row += 1

        # Set the central widget layout
        central_widget.setLayout(grid_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Provide a list of video file paths and target sizes
    video_paths = ["D:/test_seq/test_explosion_v012.mp4", "D:/test_seq/test_explosion_v002.mp4", "D:/test_seq/test_explosion_v010.mp4"]

    target_sizes = [(320, 240), (640, 480), (480, 360)]

    player = VideoPlayerApp(video_paths, target_sizes)
    player.show()
    sys.exit(app.exec_())

