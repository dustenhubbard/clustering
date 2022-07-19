import bpy
import numpy as np

'''
This file reads the output from the skeletonization (skel-poly.cgal) and generates in blender a number of segments representing the skeleton.
GCG
Updated for blender 3.3, ddh 2022-07-19
'''

cgal_file = "./skel-poly.cgal"
nr = []
vertices = []
f = open(cgal_file, "r")
for line in f:
    line_split = line.split()
    nr_points_per_line = np.int(line_split[0])
    nr.append(nr_points_per_line)
    temp_line = line_split[1:]
    fpoints = []
    for i in range(nr_points_per_line):
        fpoints.append((float(temp_line[i*3]),float(temp_line[i*3+1]),float(temp_line[i*3+2])))
    vertices.append(fpoints)

for i in vertices:
    verts = i
    edges = []
    for e in range(len(verts)-1):
        edges.append([e,e+1])

    mymesh = bpy.data.meshes.new("ske_")
    myobject = bpy.data.objects.new("ske_",mymesh)

    bpy.context.scene.collection.objects.link(myobject)

    mymesh.from_pydata(verts,edges,[])
    mymesh.update()
