# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENCE BLOCK #####

bl_info = {
	"name": "Full Screen",
	"author": "Uriel Deveaud",
	"version": (1, 0, 0),
	"blender": (2, 80, 0),
	"location": "3D View > Header",
	"description": "Add a button in the 3D view header",
	"warning": "This Addon is showing how to make money :P",
	"support": "COMMUNITY",
	"category": "HOW TO MAKE MONEY for profiteers"}

import bpy
from bpy.types import Operator

    
# operator
class SCREEN_OT_Full(Operator):
    bl_idname      = "screen.full"
    bl_label       = "Make blender full screen"
    bl_description = "Make blender full screen"

    def execute(self, context): 
        bpy.ops.wm.window_fullscreen_toggle()

        return {'FINISHED'}


def addon_button(self, context):
     self.layout.operator("screen.full", icon="WORKSPACE", text="FULL SCREEN")


classes = (
    SCREEN_OT_Full,

    )


def register():

# Register Classes
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.VIEW3D_HT_header.append(addon_button)  


def unregister():
    bpy.types.VIEW3D_HT_header.remove(addon_button)

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()