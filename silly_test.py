import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setGeometry(100, 100, 400, 300)  # Set the size and position
        self.treeWidget.setColumnCount(2)

        # Add some items to the treeWidget (for demonstration purposes)
        item1 = QTreeWidgetItem(["Item 1", "Value 1"])
        item2 = QTreeWidgetItem(["Item 2", "Value 2"])
        self.treeWidget.addTopLevelItem(item1)
        self.treeWidget.addTopLevelItem(item2)

        self.treeWidget.itemSelectionChanged.connect(self.get_selected_items)

    def get_selected_items(self):
        selected_items = self.treeWidget.selectedItems()
        selected_texts = [item.text(0) for item in selected_items]
        print(f"Selected items: {selected_texts}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

