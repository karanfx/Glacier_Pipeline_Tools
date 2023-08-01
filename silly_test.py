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

tooldir = json.load(open('bin/data/softpaths.json'))
print(tooldir)

#Import userID and tool dirs
user_json_path = "bin/data/user.json"
with open(user_json_path,"r") as uf:
    user_json = json.load(uf)
userdata = user_json.get('User_Data')

username = userdata.get('user')
studio_dir = userdata.get('studiodir')

tooldata = user_json.get('tools')
print(tooldata)