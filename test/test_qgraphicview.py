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



import sys
from PySide2.QtCore import Qt, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget

class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.video_widget = QVideoWidget(self)
        self.layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_video)
        self.layout.addWidget(self.play_button)

        # Replace 'path/to/your/video.mp4' with the path to your video file
        video_url = QUrl.fromLocalFile("D:/test_seq/test_explosion_v002.mp4")
        self.media_player.setMedia(QMediaContent(video_url))

    def play_video(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            self.play_button.setText("Play")
        else:
            self.media_player.play()
            self.play_button.setText("Pause")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoPlayerApp()
    window.show()
    sys.exit(app.exec_())
