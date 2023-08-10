import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.treeWidget = QTreeWidget(self)
#         self.treeWidget.setGeometry(100, 100, 400, 300)  # Set the size and position
#         self.treeWidget.setColumnCount(2)

#         # Add some items to the treeWidget (for demonstration purposes)
#         item1 = QTreeWidgetItem(["Item 1", "Value 1"])
#         item2 = QTreeWidgetItem(["Item 2", "Value 2"])
#         self.treeWidget.addTopLevelItem(item1)
#         self.treeWidget.addTopLevelItem(item2)

#         self.treeWidget.itemSelectionChanged.connect(self.get_selected_items)

#     def get_selected_items(self):
#         selected_items = self.treeWidget.selectedItems()
#         selected_texts = [item.text(0) for item in selected_items]
#         print(f"Selected items: {selected_texts}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())
import os
dir = "bin/data/user.json"
# par_dir = os.path.dirname(dir) 
# par_dir = os.path.dirname(par_dir) 
# print(par_dir)

# current_file_path = os.path.abspath(__file__)
# pro_dir = os.path.dirname(current_file_path)
# # pro_dir = os.path.dirname(pro_dir)
# json_path = os.path.join(pro_dir,dir)
# print(json_path)
# print(pro_dir)

# current_directory = "D:/Work/houdinifx/pipe_test"
# folders_in_current_directory = [item for item in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, item))]
# # return folders_in_current_directory
# print(folders_in_current_directory)


import json
# #Import userID and tool dirs
# user_json_path = "bin/data/user.json"
# with open(user_json_path,"r") as uf:
#     user_json = json.load(uf)
# username = user_json.get('User_Data')
# username = username.get('user')
# print(username)

# tooldir = json.load(open('bin/data/softpaths.json'))
# print(tooldir)

# #Import userID and tool dirs
# user_json_path = "bin/data/user.json"
# with open(user_json_path,"r") as uf:
#     user_json = json.load(uf)
# userdata = user_json.get('User_Data')

# username = userdata.get('user')
# studio_dir = userdata.get('studiodir')

# tooldata = user_json.get('tools')
# print(tooldata)

# import os
# import sys
# import win32com.shell.shell as shell

# ASADMIN = 'asadmin'

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     print(script)
#     print(params)
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     # sys.exit(0)

import cv2
import os

class ImageSequencePlayer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_files = sorted([f for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg", ".bmp"))])
        self.current_frame_index = 0
        self.drawing = False
        self.annotation = ""

        cv2.namedWindow("Image Sequence Player")
        cv2.setMouseCallback("Image Sequence Player", self.on_mouse_event)

    def on_mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                cv2.circle(self.image, (x, y), 5, (0, 255, 0), -1)

    def play(self):
        for image_file in self.image_files:
            image_path = os.path.join(self.folder_path, image_file)
            self.image = cv2.imread(image_path)

            if self.image is not None:
                self.show_frame()
                key = cv2.waitKey(0) & 0xFF

                # Save annotated frame if 's' key is pressed
                if key == ord('s'):
                    output_file = os.path.splitext(image_file)[0] + "_annotated.jpg"
                    output_path = os.path.join(self.folder_path, output_file)
                    cv2.imwrite(output_path, self.image)

                # Quit if 'q' key is pressed
                if key == ord('q'):
                    break

        cv2.destroyAllWindows()

    def show_frame(self):
        cv2.putText(self.image, "Press 's' to save, 'q' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.imshow("Image Sequence Player", self.image)

if __name__ == "__main__":
    folder_path = "D:/test_seq/v002"
    player = ImageSequencePlayer(folder_path)
    player.play()

