#!/usr/bin/env python3

import sys
import pymeshlab as pml

if len(sys.argv) != 2:
    print('Please pass in one .obj file as an argument.')
    sys.exit()

obj_file = sys.argv[1]
obj_name = obj_file.split('.')[0]

mesh_set = pml.MeshSet()
mesh_set.load_new_mesh(obj_file)
mesh_set.save_current_mesh(obj_name + '.off')

print(f'{obj_file} saved as {obj_name + ".off"}')
