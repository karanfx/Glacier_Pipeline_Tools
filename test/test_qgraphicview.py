# import sys
# from PySide2.QtCore import Qt, QTimer
# from PySide2.QtGui import QPixmap, QImageReader, QImage,QPainter
# from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QWidget, QVBoxLayout

# class ImageViewer(QGraphicsView):
#     def __init__(self, parent=None):
#         super(ImageViewer, self).__init__(parent)
#         self.setScene(QGraphicsScene(self))
#         self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
#         self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
#         self.image_item = QGraphicsPixmapItem()
#         self.scene().addItem(self.image_item)
#         self.current_frame = 0

#     def load_image_sequence(self, file_pattern):
#         self.image_sequence = []
#         reader = QImageReader(file_pattern)
#         while reader.size().isValid():
#             self.image_sequence.append(QPixmap.fromImage(reader.read()))
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(100)  # Adjust the interval as needed

#     def update_frame(self):
#         if self.current_frame < len(self.image_sequence):
#             self.image_item.setPixmap(self.image_sequence[self.current_frame])
#             self.current_frame += 1
#         else:
#             self.current_frame = 0

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     layout = QVBoxLayout()
#     viewer = ImageViewer()
#     layout.addWidget(viewer)
#     window.setLayout(layout)
#     window.resize(800, 600)
#     window.show()

#     # Load an image sequence (e.g., /path/to/sequence/image_%04d.png)
#     viewer.load_image_sequence("D:/test_seq/v002/test_explosion_v002_0001.jpg")

#     sys.exit(app.exec_())



# import sys
# from PySide2.QtCore import Qt, QUrl
# from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
# from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
# from PySide2.QtMultimediaWidgets import QVideoWidget

# class VideoPlayerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Video Player")
#         self.setGeometry(100, 100, 800, 600)

#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         self.layout = QVBoxLayout(self.central_widget)

#         self.video_widget = QVideoWidget(self)
#         self.layout.addWidget(self.video_widget)

#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVideoOutput(self.video_widget)

#         self.play_button = QPushButton("Play", self)
#         self.play_button.clicked.connect(self.play_video)
#         self.layout.addWidget(self.play_button)

#         # Replace 'path/to/your/video.mp4' with the path to your video file
#         video_url = QUrl.fromLocalFile("D:/test_seq/test_explosion_v002.mp4")
#         self.media_player.setMedia(QMediaContent(video_url))

#     def play_video(self):
#         if self.media_player.state() == QMediaPlayer.PlayingState:
#             self.media_player.pause()
#             self.play_button.setText("Play")
#         else:
#             self.media_player.play()
#             self.play_button.setText("Pause")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = VideoPlayerApp()
#     window.show()
#     sys.exit(app.exec_())



# import cv2
# import sys
# from PySide2 import QtCore, QtGui, QtWidgets
# import qimage2ndarray


# class VideoPlayer(QtWidgets.QWidget):

#     pause = False
#     video = False

#     def __init__(self, width=640, height=480, fps=30):
#         QtWidgets.QWidget.__init__(self)

#         self.video_size = QtCore.QSize(width, height)
#         self.camera_capture = cv2.VideoCapture(cv2.CAP_DSHOW)
#         self.video_capture = cv2.VideoCapture()
#         self.frame_timer = QtCore.QTimer()

#         self.setup_camera(fps)
#         self.fps = fps

#         self.frame_label = QtWidgets.QLabel()
#         self.quit_button = QtWidgets.QPushButton("Quit")
#         self.play_pause_button = QtWidgets.QPushButton("Pause")
#         self.camera_video_button = QtWidgets.QPushButton("Switch to video")
#         self.main_layout = QtWidgets.QGridLayout()

#         self.setup_ui()

#         QtCore.QObject.connect(self.play_pause_button, QtCore.SIGNAL("clicked()"), self.play_pause)
#         QtCore.QObject.connect(self.camera_video_button, QtCore.SIGNAL("clicked()"), self.camera_video)

#     def setup_ui(self):

#         self.frame_label.setFixedSize(self.video_size)
#         self.quit_button.clicked.connect(self.close_win)

#         self.main_layout.addWidget(self.frame_label, 0, 0, 1, 2)
#         self.main_layout.addWidget(self.play_pause_button, 1, 1, 1, 1)
#         self.main_layout.addWidget(self.camera_video_button,1, 0, 1, 1)
#         self.main_layout.addWidget(self.quit_button,2,0,1,2)

#         self.setLayout(self.main_layout)

#     def play_pause(self):
#         if not self.pause:
#             self.frame_timer.stop()
#             self.play_pause_button.setText("Play")
#         else:
#             self.frame_timer.start(int(1000 // self.fps))
#             self.play_pause_button.setText("Pause")

#         self.pause = not self.pause

#     def camera_video(self):
#         if not self.video:
#             path = QtWidgets.QFileDialog.getOpenFileName(filter="Videos (*.mp4)")
#             if len(path[0]) > 0:
#                 self.video_capture.open(path[0])
#                 self.camera_video_button.setText("Switch to camera")
#                 self.video = not self.video
#         else:
#             self.camera_video_button.setText("Switch to video")
#             self.video_capture.release()
#             self.video = not self.video


#     def setup_camera(self, fps):
#         self.camera_capture.set(3, self.video_size.width())
#         self.camera_capture.set(4, self.video_size.height())

#         self.frame_timer.timeout.connect(self.display_video_stream)
#         self.frame_timer.start(int(1000 // fps))

#     def display_video_stream(self):

#         if not self.video:
#             ret, frame = self.camera_capture.read()
#         else:
#             ret, frame = self.video_capture.read()

#         if not ret:
#             return False

#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         if not self.video:
#             frame = cv2.flip(frame, 1)
#         else:
#             frame = cv2.resize(frame, (self.video_size.width(), self.video_size.height()), interpolation=cv2.INTER_AREA)

#         image = qimage2ndarray.array2qimage(frame)
#         self.frame_label.setPixmap(QtGui.QPixmap.fromImage(image))

#     def close_win(self):
#         self.camera_capture.release()
#         self.video_capture.release()
#         cv2.destroyAllWindows()
#         self.close()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     player = VideoPlayer()
#     player.show()
#     sys.exit(app.exec_())


# #!/usr/bin/env python

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# import qimage2ndarray

# import cv2
# import sys

# class MainApp(QWidget):

#     def __init__(self):
#         QWidget.__init__(self)
#         self.video_size = QSize(320, 240)
#         self.setup_ui()
#         self.setup_camera()

#     def setup_ui(self):
#         """Initialize widgets.
#         """
#         self.image_label = QLabel()
#         self.image_label.setFixedSize(self.video_size)

#         self.quit_button = QPushButton("Quit")
#         self.quit_button.clicked.connect(self.close)

#         self.main_layout = QVBoxLayout()
#         self.main_layout.addWidget(self.image_label)
#         self.main_layout.addWidget(self.quit_button)

#         self.setLayout(self.main_layout)

#     def setup_camera(self):
#         """Initialize camera.
#         """
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.display_video_stream)
#         self.timer.start(30)

#     def display_video_stream(self):
#         """Read frame from camera and repaint QLabel widget.
#         """
#         _, frame = self.capture.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame = cv2.flip(frame, 1)
#         image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK
#         self.image_label.setPixmap(QPixmap.fromImage(image))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainApp()
#     win.show()
#     sys.exit(app.exec_())