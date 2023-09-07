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


import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def createButtons(self, button_count):
        # Clear the layout to remove existing buttons
        self.clearLayout()

        # Create and add new buttons
        for i in range(button_count):
            button = QPushButton(f"Button {i+1}")
            self.layout.addWidget(button)

    def clearLayout(self):
        # Remove all widgets from the layout
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()

    # Example: Change the number of buttons dynamically
    window.createButtons(5)

    sys.exit(app.exec_())
