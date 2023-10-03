import nuke
import os


#Get the shot plate 
#Get the renders
#Reformat the renders
#merge it - done
#place a write node - done
#Write a slapcomp

#print(nuke.env)
# print(os.getenv("NUKE_TEMP_DIR"))

# 

#GET ALL RENDERS AND PLATES
renders = ["a","b","c","d","e"]
output = ""
save_file = ""
plate = "D:/test_data/Library Camera Track/Library Camera Track/UD_Plate/Library_03_dewarped.1001.jpg"

def slapcomp(plates,renders,output):
    read_plate = nuke.nodes.Read(file = plate)

    merge_all = nuke.nodes.Merge(inputs=[read_plate])
    for render in renders:
        read_renders = nuke.nodes.Read(file=render)
        merge_all = nuke.nodes.Merge(inputs=[read_renders,merge_all])


    write = nuke.nodes.Write(file=output, inputs=[merge_all])
    # nuke.execute( write, 1, 1 )
    nuke.scriptSaveAs(filename=save_file, overwrite=- 1)