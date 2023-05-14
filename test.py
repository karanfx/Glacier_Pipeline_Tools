import json
import os

# j = open('tools_path.json')
# k = json.load(j)

# #print(k)
# for i in k:
#     #print(i)
#     print(k[i])

path = 'D:\Work\houdinifx'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])