# # import pxr.Usdview 
# import os
# cur_shot = os.environ("SHOT")
# print(cur_shot)

# print('Launch through subprocess')
vers = "v002"
# n_vers = vers + 1

import os
import re
versions = os.listdir("D:/test_studio/Show01/Seq_AB/Shot_AB001/libs/fx")

numbers = [int(re.search(r'\d+', name).group(0)) for name in versions if re.search(r'\d+', name)]

l = ["v001","v004","v005","v006"]
max_v = str(max(l))
max_v = max_v.strip('v')
print(int(max_v)+1)

max_v = str(max(l))
max_v = int(max_v.strip('v')) +1
print(int(max_v)+1)
vers_up = f"v{max_v:03d}"
print(vers_up)
# print(max(versions))
# print(versions[-1])
# print(numbers)