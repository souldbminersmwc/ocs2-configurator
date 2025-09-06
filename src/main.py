import dearpygui.dearpygui as dpg
import gpu
import cpu
import ram
from PIL import Image
import numpy as np
import psutil
import os
import common as c
dpg.create_context()

assets_path="assets/"

image_path = assets_path + "coolerhd.png"
image = Image.open(image_path).convert("RGBA")
image = image.resize((64, 64))
width, height = image.size

image_data = np.array(image) / 255.0
image_data = image_data.flatten()

with dpg.font_registry():
    lexend = dpg.add_font(assets_path + "Lexend.ttf", 16)
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=image_data, tag="coolerhd")


def get_drives():
    drives = []
    for part in psutil.disk_partitions(all=False):
        drives.append(part.device)
    return drives

drive_list = get_drives()

def check_atmosphere(sender, app_data, user_data):
    drive = app_data
    atmosphere_path = os.path.join(drive, "atmosphere")
    package3_path = os.path.join(atmosphere_path, "package3")
    if os.path.isfile(f"{atmosphere_path}/kips/loader.kip"):
        dpg.set_value("status_text", "OCS2 Install Found!")
    elif os.path.isdir(atmosphere_path) and os.path.isfile(package3_path):
        dpg.set_value("status_text", "Atmosphere install found!")
    else:
        dpg.set_value("status_text", "Atmosphere not found!")
with dpg.window(label="Configurator", width=400, height=300,id="main_window"):
    with dpg.tab_bar():
        with dpg.tab(label="Settings"):
            dpg.add_text("Installation Drive")
            dpg.add_combo(
                items=drive_list,
                default_value="Select a drive!",
                callback=check_atmosphere
            )
            dpg.add_text("", tag="status_text")
            dpg.add_text(c.get_value("cpu_speedo"))
        with dpg.tab(label="GPU"):
            gpu.populate()
        with dpg.tab(label="CPU"):
            cpu.populate()
        with dpg.tab(label="RAM"):
            ram.populate()

dpg.bind_font(lexend)
dpg.create_viewport(title="OCS2 Configuration", width=854, height=480)
dpg.setup_dearpygui()
dpg.set_viewport_large_icon(assets_path + "icon.ico")
dpg.show_viewport()
dpg.set_viewport_title("OCS2 Configurator")
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
