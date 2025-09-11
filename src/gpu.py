
"""

OCS2 Configurator

Copyright (C) Souldbminer

This program is free software; you can redistribute it and/or modify it
under the terms and conditions of the GNU General Public License,
version 2, as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import configparser
import dearpygui.dearpygui as dpg
import kip as k
import common
from pathlib import Path

def check_gpu_sched():
    if(common.drive == 0):
        return False
    ini_path = Path(common.drive + "/atmosphere/config/system_settings.ini")
    if not ini_path.exists():
        return False
    config = configparser.ConfigParser()
    config.read(ini_path)

    try:
        value = config["am.gpu"]["gpu_scheduling_enabled"]
        return value.strip() == "0x1"
    except KeyError:
        return False

def toggle_gpu_sched(sender, app_data):
    if(common.drive == 0):
        common.show_popup("Error", "GPU Scheduling Toggle is unavailable for Manual Kip Selection")
        return False
    ini_path = Path(common.drive + "/atmosphere/config/system_settings.ini")
    ini_path.parent.mkdir(parents=True, exist_ok=True)

    config = configparser.ConfigParser()
    if ini_path.exists():
        config.read(ini_path)

    if "am.gpu" not in config:
        config["am.gpu"] = {}
    if app_data:
        config["am.gpu"]["gpu_scheduling_enabled"] = "0x1"
    else:
        config["am.gpu"]["gpu_scheduling_enabled"] = "0x0"
    with ini_path.open("w") as f:
        config.write(f)
    common.show_popup("Sucess", f"Set GPU Scheduling to {app_data}")

def populate():
    offsets = list(range(0, 51, 5))
    processed_offsets = ["Disabled" if v == 0 else f"-{v} mV" for v in offsets]
    voltages = [0] + list(range(480, 960 + 1, 5))  # 0 first for Disabled
    processed_voltages = ["Disabled" if v == 0 else f"{v} mV" for v in voltages]
    processed_voltages_default = ["Default" if v == 0 else f"{v} mV" for v in voltages]
    freqs_khz = [
        76800, 153600, 230400, 307200, 384000, 460800, 537600, 614400, 691200, 768000,
        844800, 921600, 998400, 1075200, 1152000, 1228800, 1267200, 1305600, 1344000, 1382400, 1420800,
        1459200, 1497600, 1536000
    ]
    freqs_mhz = [
        76.8, 153.6, 230.4, 307.2, 384.0, 460.8, 537.6, 614.4, 691.2, 768.0,
        844.8, 921.6, 998.4, 1075.2, 1152.0, 1228.8, 1267.2, 1305.6, 1344.0, 1382.4,
        1420.8, 1459.2, 1497.6, 1536.0
    ]
    freqs_mhz_label = [f"{f} MHz" for f in freqs_mhz]
    
    dpg.add_separator(label="Notice")
    dpg.add_text("Everything in this tab other than the maximum frequency and Scheduling only works for Mariko switch units. Erista units cannot use these settings yet")

    dpg.add_separator(label="Frequencies")

    dpg.add_button(
            label="What is this?",
            callback=common.show_info_window,
            user_data="A higher GPU frequency significantly increases power draw. To sustain higher frequencies without exeeding PMIC limit, undervolt your device \nDO NOT disable GPU scheduling without a adequate undervolt as it can cause hardware damage due to the high power consumption",
            width=120,
            height=64,  # height=0 makes it match text
            small=True,
            tag="freqs_info"
    )
    dpg.add_checkbox(label="GPU Scheduling", default_value=True, tag="gpu_sched", callback=toggle_gpu_sched)
    dpg.add_combo(
        items=freqs_mhz_label,
        default_value="921.6MHz",
        label="GPU Max Frequency",
        callback=k.grab_kip_storage_values,
        tag="gpu_max_freq"
    )

    dpg.add_separator(label="Voltages")

    dpg.add_button(
            label="What is this?",
            callback=common.show_info_window,
            user_data="Lower voltages reduce power draw and tempratures. Higher voltages can boost available clockspeeds. Choose voltages with caution, as high voltages can cause IRREPERABLE hardware damage",
            width=120,
            height=64,  # height=0 makes it match text
            small=True,
            tag="volt_info"
    )
    dpg.add_combo(
        items=processed_voltages,
        default_value="Disabled",
        label="Gpu vMin",
        callback=k.grab_kip_storage_values_no_mult,
        tag="g_vmin"
    )
    dpg.add_combo(
        items=processed_voltages,
        default_value="Disabled",
        label="Gpu vMax",
        callback=k.grab_kip_storage_values_no_mult,
        tag="g_vmax"
    )

    dpg.add_separator(label="Undervolt")

    dpg.add_button(
        label="What is this?",
        callback=common.show_info_window,
        user_data="A undervolted device consumes less power, heats up less, which enables higher clocks. \nThe GPU Undervolt mode should be set to Default or High, test which one is suitable to your console. Custom is only meant for ADVANCED USERS, as the values in it could cause HARDWARE DAMAGE! \nThe Offset should be kept at the minumum your GPU requires to function at the high ram clock (high ram clock means more GPU power needed)",
        width=120,
        height=64,  # height=0 makes it match text
        small=True,
        tag="uv_info"
    )
    dpg.add_combo(
        items=["No Table (UV0)", "Regular Table (UV1)", "High Table (UV2)", "Custom Table (UV3)"],
        default_value="No Table (UV0)",
        label="Undervolt Modes",
        callback=k.grab_kip_storage_values_no_mult,
        tag="m_gpu_uv"
    )
    dpg.add_combo(
        items=processed_offsets,
        default_value="Disabled",
        label="Gpu Volt Offset",
        callback=k.grab_kip_storage_values_no_mult,
        tag="m_gpu_offset"
    )

    dpg.add_separator(label="Custom Table")

    for freq in freqs_khz:
        if(freq > 1382400):
            mhz_label = f"{freq / 1000:.1f} MHz (DANGEROUS)"
        elif(freq > 1152000):
            mhz_label = f"{freq / 1000:.1f} MHz (UNSAFE)"
        else:
            mhz_label = f"{freq / 1000:.1f} MHz"
        mhz_tag = f"combo_{freq}"
        if freq == 1536000:
            with dpg.group(horizontal=True):  # align horizontally
                dpg.add_combo(
                    items=processed_voltages,
                    default_value="Disabled",
                    label=mhz_label,
                    tag="g_volt_" + str(freq),
                    callback=k.grab_kip_storage_values_no_mult
                )
                dpg.add_image("coolerhd", width=16, height=16)
        else:
            dpg.add_combo(
                items=processed_voltages,
                default_value="Disabled",
                label=mhz_label,
                tag="g_volt_" + str(freq),
                callback=k.grab_kip_storage_values_no_mult
            )