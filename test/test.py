import json
import os
from PySide6 import QtWidgets

import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QFileDialog

class SequencePlayer(QMainWindow):
    def __init__(self, parent=None):
        super(SequencePlayer, self).__init__(parent)
        self.setWindowTitle("Sequence Player with Annotation")

        self.current_frame_index = 0
        self.image_sequence = []
        self.annotations = []

        # Create GUI elements
        self.image_label = QLabel(self)
        self.annotation_input = QLineEdit(self)
        self.load_button = QPushButton("Load Sequence", self)
        self.prev_button = QPushButton("Previous", self)
        self.next_button = QPushButton("Next", self)
        self.save_button = QPushButton("Save Annotations", self)

        # Connect buttons to functions
        self.load_button.clicked.connect(self.load_sequence)
        self.prev_button.clicked.connect(self.show_previous_frame)
        self.next_button.clicked.connect(self.show_next_frame)
        self.save_button.clicked.connect(self.save_annotations)

        # Layout setup
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.annotation_input)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        button_layout.addWidget(self.save_button)
        self.layout.addLayout(button_layout)

        main_widget = QWidget(self)
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def load_sequence(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Image Sequence", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)

        if file_path:
            self.image_sequence = []
            self.annotations = []

            image_folder = os.path.dirname(file_path)
            image_files = sorted([f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg", ".bmp"))])

            for image_file in image_files:
                image_path = os.path.join(image_folder, image_file)
                self.image_sequence.append(cv2.imread(image_path))
                self.annotations.append("")

            self.show_frame(self.current_frame_index)

    def show_frame(self, frame_index):
        frame = self.image_sequence[frame_index]
        annotation = self.annotations[frame_index]

        height, width, channels = frame.shape
        bytes_per_line = channels * width
        q_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        q_img = QImage(q_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.image_label.setPixmap(pixmap)
        self.annotation_input.setText(annotation)

    def show_previous_frame(self):
        if self.current_frame_index > 0:
            self.current_frame_index -= 1
            self.show_frame(self.current_frame_index)

    def show_next_frame(self):
        if self.current_frame_index < len(self.image_sequence) - 1:
            self.current_frame_index += 1
            self.show_frame(self.current_frame_index)

    def save_annotations(self):
        for i, annotation in enumerate(self.annotations):
            self.annotations[i] = self.annotation_input.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = SequencePlayer()
    player.show()
    sys.exit(app.exec_())
