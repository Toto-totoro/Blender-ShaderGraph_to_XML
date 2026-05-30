# Blender ShaderGraph_to_XML
# Contributor(s): Tom Schäfer (tschaefer.acc@gmail.com) and Laurin von Bergmann
#
# Template "Blender Add-on Template" by: Aaron Powell (aaron@lunadigital.tv)
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

bl_info = {
        "name": "Shader_to_XML",
        "description": "Exports a material's shader-graph into a serialized graph in XML.",
        "author": "Tom Schäfer, Laurin von Bergmann",
        "version": (1, 0),
        "blender": (5, 1, 2),
        "location": "File > Export > Shader Graph as XML",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "https://github.com/Toto-totoro/Blender-ShaderGraph_to_XML/wiki",
        "tracker_url": "https://github.com/Toto-totoro/Blender-ShaderGraph_to_XML/issues",
        "support": "COMMUNITY",
        "category": "Export"
        }

import bpy

#
# Add additional functions here
#

def register():
    from . import properties
    from . import ui
    from . import exporter
    properties.register()
    exporter.register()
    ui.register()

def unregister():
    from . import properties
    from . import ui
    from . import exporter
    properties.unregister()
    exporter.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()