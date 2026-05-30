import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty
from bpy.types import Operator
from ui import menu_export_button

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
        items=get_materials()
        )
    
def register():
    bpy.utils.register_class(ExportShaderGraph)
    bpy.types.TOPBAR_MT_file_export.append(menu_export_button)