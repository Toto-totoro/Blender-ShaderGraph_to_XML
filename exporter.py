# Blender ShaderGraph_to_XML
# Contributor(s): Tom Schäfer (tschaefer.acc@gmail.com) and Laurin von Bergmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, EnumProperty
from bpy.types import Operator

# List of all materials in file
def get_materials_callback(self, context):
    items = [("ALL", "All Materials", "Export every material in the file")]
    for material in bpy.data.materials:
        items.append((material.name, material.name, f"Export {material.name}"))
    return items

class ExportShaderGraph(bpy.types.Operator, ExportHelper):
    bl_idname = "export.shadergraph"
    bl_label = "Export ShaderGraph"
    filename_ext = ".xml"

    material_selection: EnumProperty(
        name="Material",
        description="Choose a material to export",
        items=get_materials_callback
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Select Material to Export:")
        layout.prop(self, "material_selection")

    def invoke(self, context, event):
        self.filepath = ""
        return context.window_manager.invoke_props_dialog(self)

    def check(self, context):
        return True


    def execute(self, context):
        target_filepath = self.filepath
        chosen_material = self.material_selection

        if not chosen_material:
            self.report({'ERROR'}, "No material selected for export.")
            return {'CANCELLED'}

        if chosen_material == 'ALL':
            materials_to_export = bpy.data.materials
        else:
            materials_to_export = [bpy.data.materials.get(chosen_material)]

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExportShaderGraph)


def unregister():
    bpy.utils.unregister_class(ExportShaderGraph)
    