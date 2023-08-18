import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem


import cv2
import os

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

os.system("Houdini")
