import hou
import os 
import shutil

obj = hou.node("/obj")
#children = obj.children()
children = obj.allSubChildren()
for child in children:
    #print(child.type().name())
    #print(child.NodeTypeCategory())
    if child.type().name() == "filecache":
        cache_path = child.parm("file").eval()
        cache_folder = os.path.dirname(cache_path)
        print(cache_path)

        target_folder = "D:/Work/houdinifx/pipe_test/Show01/v001/"
        #print(child.path())
        #shutil.copytree(cache_path,target_folder)
        if os.path.exists(cache_folder):
            print(cache_folder)
            cache_dir = os.path.dirname(cache_folder)
            cache_name = cache_dir.split("/")[-1]
            print(cache_name)
            target_dir = os.path.join(target_folder,cache_name)
            #os.mkdir(target_dir)
            print(target_dir)
            shutil.copytree(cache_folder,target_dir)
            #shutil.copy(cache_path,target_folder)
        else:
            print("not found")
        #    pass