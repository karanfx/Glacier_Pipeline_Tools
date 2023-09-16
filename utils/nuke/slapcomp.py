import nuke


#Get the shot plate
#Get the renders
#Reformat the renders
#merge it
#place a write node
#Write a slapcomp


r1 = nuke.nodes.Read (file="D:/test_data/Library Camera Track/Library Camera Track/UD_Plate/Library_03_dewarped.1001.jpg")
r2 = nuke.nodes.Read (file="filepath/filename.ext")
m = nuke.nodes.Merge (inputs=[r2, r1])