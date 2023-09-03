import hou
import os 
import shutil
from PySide2 import QtGui, QtWidgets, QtCore,QtUiTools
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap

uifile = "E:/Work/python_dev/QT_project_launcher/qt_ui_files/hou_tools_ui/cache_collector.ui"

class cache_collector(QtWidgets.QWidget):
    def __init__(self):
        super(cache_collector, self).__init__()
        self.ui = QtUiTools.QUiLoader().load(uifile,parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(),QtCore.Qt.Window)
        self.setWindowTitle("Glacier Apps - Cache Collector")
        self.setWindowIcon(QtGui.QIcon("E:/Work/python_dev/QT_project_launcher/bin/logo/favicon_sq_small.png"))
        #enable multi select 
        self.ui.cache_data_TW.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
                
        self.populate_caches()
        self.ui.collect_all_cache_PB.clicked.connect(self.collect_all_cache)
        self.ui.collect_selected_cache_PB.clicked.connect(self.collect_sel_cache)
        self.ui.delete_older_cache_PB.clicked.connect(self.cache_cleanup)

    def populate_caches(self):
        obj = hou.node("/obj")
        #children = obj.children()
        children = obj.allSubChildren()
        
        for child in children:
            #print(child.type().name())
            #print(child.NodeTypeCategory())
            if child.type().name() == "filecache":
                cache_path = child.parm("file").eval()
                cache_folder = os.path.dirname(cache_path)
                # print(child.name())
                # print(cache_path)
                
                #Count files 
                def count_dir(cache_path):
                    cache_path = os.path.dirname(cache_path)
                    if os.path.exists(cache_path):
                        count = len(os.listdir(cache_path))
                        
                        return count
                     

                #List for Tree Wid
                count = count_dir(cache_path)                
                cache_item = [child.name(),str(count),cache_path]
               
                # Add items in tree widget
                item = QtWidgets.QTreeWidgetItem(list(cache_item))
                self.ui.cache_data_TW.addTopLevelItem(item)


    def collect_all_cache(self):
        self.ui.cache_data_TW.selectAll()

        cache_item = self.ui.cache_data_TW.selectedItems()
        caches = [{item.text(0):item.text(2)} for item in cache_item]
        print(caches)
        dest_folder = "D:/Work/houdinifx/pipe_test/Show01/v001/"
        #print(child.path())
        #shutil.copytree(cache_path,target_folder)
        def copy_caches(src_folder,dest_folder):
            #check if dir exist
            if os.path.exists(src_folder):
                cache_dir = os.path.dirname(src_folder)
                cache_name = cache_dir.split("/")[-1]
                print(cache_name)
                target_dir = os.path.join(dest_folder,cache_name)
                os.mkdir(target_dir)
                shutil.copytree(src_folder,target_dir)
                #shutil.copy(cache_path,target_folder)
            else:
                print("Data not found")
            #    pass
        
        # copy_caches(caches,dest_folder)
        
    def collect_sel_cache(self):
        #Get Selected nodes
        cache_item = self.ui.cache_data_TW.selectedItems()
        caches = [{item.text(0):item.text(1)} for item in cache_item]
        print(caches)

        
    def cache_cleanup(self):
        print("cleaning caches..")


win = cache_collector()
win.show()