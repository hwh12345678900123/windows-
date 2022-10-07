import tools.file
import os

# with open('test2.py', 'w') as f:
#     f.write("def a():\n")
#     f.write("    print('Hello world!')")
# f.close()
# import test2
#
# test2.a()
with open('test2.py', 'r') as f:
    print(f.readlines())
f.close()