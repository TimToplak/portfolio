from docx import Document
import json

inputFile = 'test.docx'
outputFile = 'textVertices.json'

document = Document(inputFile)
vertices = []
i = 0
j = 0
for paragraph in document.paragraphs:
    for run in paragraph.runs:
        for char in run.text:
            if char != '\xa0':  # remove whitespaces
                temp = {"x": None, "y": None, "z": None, "r": None, "g": None, "b": None}
                temp["x"] = i
                temp["y"] = j
                temp["z"] = 0
                temp["r"] = run.font.color.rgb[0]
                temp["g"] = run.font.color.rgb[1]
                temp["b"] = run.font.color.rgb[2]
                vertices.append(temp)
            i += 1
    i = 0
    j -= 1

jsonDump = json.dumps(vertices)

f = open(outputFile, 'w')
f.writelines(jsonDump)
f.close()
