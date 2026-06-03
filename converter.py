# Blender ShaderGraph_to_XML
# Contributor(s): Tom Schäfer (tschaefer.acc@gmail.com) and Laurin von Bergmann
#
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
import xml.etree.ElementTree as ET

def convert_materials_to_xml(materials: list) -> str:
    # root element
    root = ET.Element("ShaderGraphs")

    for material in materials:
        convert_shader_graph_to_xml(material, root)

    return ET.tostring(root, pretty_print=True).decode()

def convert_shader_graph_to_xml(material, root):
    material_element = ET.SubElement(root, "Material", name=material.name)

    # TODO: node groups should get replaced by their contents. They can be identified by their bl_idname "ShaderNodeGroup" and accessed via bpy.data.node_groups.
    # TODO: validate wether all needed node properties are exported
    # TODO: the actually relevant properties are currently not exported correctly, they are most likely stored as an array in the 'input' and 'output' properties of the node which are arrays

    # Iterate through the nodes in the material's node tree
    for node in material.node_tree.nodes:
        node_element = ET.SubElement(material_element, "Node", type=node.bl_idname, name=node.name)

        # Add properties of the node as sub-elements

        property_selection = {
            'type', 'inputs', 'outputs', 'internal_links', 'node_tree'
        }

        for prop_name in node.bl_rna.properties.keys():
            if prop_name not in property_selection:  # Skip unneeded properties
                continue
            prop_value = getattr(node, prop_name)
            ET.SubElement(node_element, "Property", name=prop_name).text = str(prop_value)

    # TODO: sort links in graph order
    # Store node links
    # Format: <Link from_node="NodeA" from_socket="Output" to_node="NodeB" to_socket="Input"/>
    # Socket is the connection point (variable) from the graph
    links_element = ET.SubElement(material_element, "Links")
    for link in material.node_tree.links:
        ET.SubElement(
            links_element,
            "Link",
            from_node=link.from_node.name,
            from_socket=link.from_socket.name,
            to_node=link.to_node.name,
            to_socket=link.to_socket.name,
        )