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

        #add logo and window name
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

            if child.type().name() == "filecache":
                cache_path = child.parm("file").eval()
                cache_folder = os.path.dirname(cache_path)

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
        
        for item in cache_item:
            name = item.text(0)
            count = item.text(1)
            path = item.text(2)
            # print(name,count,path)

            if count == "None":
                #Not Found Message
                message = 'Cache not found for {}'.format(name)
                hou.ui.displayMessage(message, title="Not Found", severity=hou.severityType.Message)
            else:
                #find the current cache node 
                obj = hou.node("/obj")
                children = obj.allSubChildren()
        
                for child in children:
                    if child.name() == name:
                        #Copy Data to new Dir 
                        cur_vers = os.path.dirname(path)
                        vers = os.path.dirname(cur_vers)
                        # print(cur_vers)
                        # print(vers)

                        #Set Dest Dir
                        dest_path = path.replace('cache','collect_cache')
                        dest_dir = os.path.dirname(dest_path)
                        #Copy Data
                        shutil.copytree(cur_vers,dest_dir)
                        #Create a replica file cache node
                        parent = child.parent()
                        node_path = parent.path()
                        # print(node_path)
                        new_cache_node = parent.createNode('filecache',"collect_" + name)
                        new_cache_node.parm("file").set(dest_path)
        
    def collect_sel_cache(self):
        #Get Selected nodes
        cache_item = self.ui.cache_data_TW.selectedItems()
        
        for item in cache_item:
            name = item.text(0)
            count = item.text(1)
            path = item.text(2)
            # print(name,count,path)

            if count == "None":
                #Not Found Message
                # print('cache not found for {}'.format(name))
                message = 'Cache not found for {}'.format(name)
                hou.ui.displayMessage(message, title="Not Found", severity=hou.severityType.Message)
            else:
                #find the current cache node 
                obj = hou.node("/obj")
                children = obj.allSubChildren()
        
                for child in children:
                    if child.name() == name:
                        #Copy Data to new Dir 
                        cur_vers = os.path.dirname(path)
                        vers = os.path.dirname(cur_vers)
                        print(cur_vers)
                        print(vers)
                        
                        #Set Dest Dir
                        dest_path = path.replace('cache','collect_cache')
                        dest_dir = os.path.dirname(dest_path)
                        #Copy Data
                        shutil.copytree(cur_vers,dest_dir)

                        #Create a replica file cache node
                        parent = child.parent()
                        node_path = parent.path()
                        print(node_path)
                        new_cache_node = parent.createNode('filecache',"collect_" + name)
                        new_cache_node.parm("file").set(dest_path)

    def cache_cleanup(self):
        #Get Selected nodes
        cache_item = self.ui.cache_data_TW.selectedItems()
        
        for item in cache_item:
            name = item.text(0)
            count = item.text(1)
            path = item.text(2)
            # print(name,count,path)

            if count == "None":
                #Not Found Message
                # print('cache not found for {}'.format(name))
                message = 'Cache not found for {}'.format(name)
                hou.ui.displayMessage(message, title="Not Found", severity=hou.severityType.Message)
            else:
                #find the current cache node 
                obj = hou.node("/obj")
                children = obj.allSubChildren()
        
                for child in children:
                    if child.name() == name:
                        #Copy Data to new Dir 
                        cur_vers = os.path.dirname(path)
                        vers = os.path.dirname(cur_vers)

                        # print(cur_vers)
                        # print(vers)
                        
                        for dir in os.listdir(vers): 
                            dir = os.path.join(vers,dir)
                            dir = dir.replace("\\","/")

                            #Cache Removed 
                            if dir != cur_vers:
                                shutil.rmtree(dir)
                                print("Cache Removed : ",dir)
                            else:
                                print("Sel_version",dir)

win = cache_collector()
win.show()