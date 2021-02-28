import bpy
import json
# Exports selected object vertices to json array
outputFile = 'C:/tmp/mesh.json'

verts = [v.co for v in bpy.context.object.data.vertices]
obj = []
for co in verts:
    temp = {"x": None, "y": None, "z": None}
    temp["x"] = co[0]
    temp["y"] = co[2]
    temp["z"] = co[1]
    obj.append(temp)

jsonDump = json.dumps(obj)

f = open(outputFile, 'w')
f.writelines(jsonDump)
f.close()
