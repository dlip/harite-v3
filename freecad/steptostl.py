import sys
import os
import shutil

freecad_path = os.path.dirname(
    os.path.dirname(os.path.realpath(shutil.which("freecad")))
)
sys.path.append(f"{freecad_path}/Ext")
import freecad
import FreeCAD as App
import Part
import Mesh
import os

# Directory with .step files (current dir)
directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.lower().endswith((".step", ".stp")):
        base_name = os.path.splitext(filename)[0]
        step_path = os.path.join(directory, filename)
        stl_path = os.path.join(directory, base_name + ".stl")

        # Create a new document
        doc = App.newDocument(base_name)

        shape = Part.Shape()
        shape.read(step_path)
        pf = doc.addObject("Part::Feature", "MyShape")
        pf.Shape = shape

        Mesh.export([pf], stl_path)

        # Close the document
        App.closeDocument(doc.Name)

        print(f"Converted {filename} -> {base_name}.stl")
