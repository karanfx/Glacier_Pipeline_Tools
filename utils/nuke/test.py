# gradeShots.py
import nuke
import os
import sys

shot = sys.argv[0]
r = nuke.nodes.Read(file=sys.argv[0])
g = nuke.nodes.Grade( inputs=[r] )
g['black'].setValue( 0.05 )
outName = '{}-a-grade-up.mov'.format(os.path.split(shot)[0])
w = nuke.nodes.Write(file=outName, inputs=[g])
nuke.execute( w, 1, 1 )


#Command
# "C:/Program Files/Nuke14.0v1/Nuke14.0.exe" "E:/Work/python_dev/QT_project_launcher/utils/nuke/test.py" shot-90123-a.exr