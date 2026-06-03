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
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

# List of all materials in file
#def get_materials_callback(self, context):
#    items = [("ALL", "All Materials", "Export every material in the file")]
#    for material in bpy.data.materials:
#        items.append((material.name, material.name, f"Export {material.name}"))
#    return items

class ExportShaderGraph(bpy.types.Operator, ExportHelper):
    bl_idname = "export.shadergraph"
    bl_label = "Export ShaderGraph"
    filename_ext = ".xml"

    select_all: BoolProperty(
        name="Select Everything",
        default=False,
        description="Toggle all materials for export",
    )

    old_select_all: BoolProperty(
        default=False,
        options={'HIDDEN'}
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "select_all")
        layout.separator()
        layout.label(text="Select Material to Export:")

        box = layout.box()

        for item in context.blend_data.materials:
            row = box.row()
            row.prop(item, "export", text=item.name)

    def invoke(self, context, event):
        self.filepath = ""
        self.select_all = False
        self.old_select_all = False
        return context.window_manager.invoke_props_dialog(self)

    def check(self, context):
        if self.select_all != self.old_select_all:
            for item in context.blend_data.materials:
                item.export = self.select_all
            self.old_select_all = self.select_all    
            return True
        return True


    def execute(self, context):
        target_filepath = self.filepath
        materials_to_export = [item for item in bpy.data.materials if item.export]

        if not materials_to_export:
            self.report({'ERROR'}, "No material selected for export.")
            return {'CANCELLED'}

        for material in materials_to_export:
            # Here you would implement the actual export logic for each material
            print(f"{material.name} in {target_filepath} rein (oder in dich)")
        return {'FINISHED'}

def register():
    bpy.types.Material.export = BoolProperty(name="", default=False)
    bpy.utils.register_class(ExportShaderGraph)


def unregister():
    bpy.utils.unregister_class(ExportShaderGraph)
    del bpy.types.Material.export