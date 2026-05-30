import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty
from bpy.types import Operator

# List of all materials in file
def get_materials():
    materials = []
    for material in bpy.data.materials:
        materials.append(material)
    return materials

class ExportShaderGraph(bpy.types.Operator, ExportHelper):
    bl_idname = "export.shadergraph"
    bl_label = "Export ShaderGraph"
    filename_ext = ".xml"

    material_selection = EnumProperty(
        name="Material",
        description="Choose a material to export",
        # items=get_materials()
        )
    
def register():
    bpy.utils.register_class(ExportShaderGraph)


def unregister():
    bpy.utils.unregister_class(ExportShaderGraph)
    