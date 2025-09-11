
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


import dearpygui.dearpygui as dpg
import struct
from defaults import d
import common as c
import gpu as g
import cpu
import struct
import defaults as df
import re
global g_freq_str
kip_file_path=None

# This is grouped together as in the binary C/C++ pad doubles to align to memory banks.
variables = [
    # Common
    ("custrev", "u32"),
    ("mtcConf", "u32"),
    ("commonCpuBoostClock", "u32"),
    ("commonEmcMemVolt", "u32"),

    # Erista
    ("eristaCpuMaxVolt", "u32"),
    ("eristaEmcMaxClock", "u32"),

    # Mariko
    ("marikoCpuMaxVolt", "u32"),
    ("marikoEmcMaxClock", "u32"),
    ("marikoEmcVddqVolt", "u32"),
    ("marikoCpuUV", "u32"),
    ("marikoGpuUV", "u32"),
    ("commonGpuVoltOffset", "u32"),
    ("marikoCpuHighVoltOffset", "u32"),
    ("marikoCpuHighUV", "u32"),

    # CPU/GPU
    ("cpuMaxFreq", "u32"),
    ("gpuMaxFreq", "u32"),
    ("gpuVmax", "u32"),
    ("gpuVmin", "u32"),

    ("marikoEmcDvbShift", "u32"),

    # RAM timings (u32)
    ("latency", "u32"),
    ("BL", "u32"),
    ("tRFCpb", "u32"),
    ("tRFCab", "u32"),
    ("tRAS", "u32"),
    ("tRPpb", "u32"),
    ("tRPab", "u32"),
    ("tRC", "u32"),
    ("tWTR", "u32"),
    ("tWR", "u32"),
    ("tR2REF", "u32"),
    ("tRCD", "u32"),
    ("tREFpb", "u32"),
    ("tMRWCKEL", "u32"),
    ("tSR", "u32"),
    ("tFAW", "u32"),

    # RAM timings (double)
    ("tDQSCK_min", "double"),
    ("tDQSCK_max", "double"),
    ("tWPRE", "double"),
    ("tRPST", "double"),
    ("tDQSS_max", "double"),
    ("tDQS2DQ_max", "double"),
    ("tDQSQ", "double"),
    ("tRTP", "double"),
    ("tRRD", "double"),
    ("tXP", "double"),
    ("tCMDCKE", "double"),
    ("tCKELCS", "double"),
    ("tCSCKEH", "double"),
    ("tXSR", "double"),
    ("tCKE", "double"),
    ("tCKCKEH", "double"),

    # Mariko GPU voltages (keep individually)
    ("g_volt_76800", "u32"),
    ("g_volt_153600", "u32"),
    ("g_volt_230400", "u32"),
    ("g_volt_307200", "u32"),
    ("g_volt_384000", "u32"),
    ("g_volt_460800", "u32"),
    ("g_volt_537600", "u32"),
    ("g_volt_614400", "u32"),
    ("g_volt_691200", "u32"),
    ("g_volt_768000", "u32"),
    ("g_volt_844800", "u32"),
    ("g_volt_921600", "u32"),
    ("g_volt_998400", "u32"),
    ("g_volt_1075200", "u32"),
    ("g_volt_1152000", "u32"),
    ("g_volt_1228800", "u32"),
    ("g_volt_1267200", "u32"),
    ("g_volt_1305600", "u32"),
    ("g_volt_1344000", "u32"),
    ("g_volt_1382400", "u32"),
    ("g_volt_1420800", "u32"),
    ("g_volt_1459200", "u32"),
    ("g_volt_1497600", "u32"),
    ("g_volt_1536000", "u32"),
]


def load_all_vars():
    # common
    c.load_entry_object("custrev", 0)
    c.load_entry_object("mtc", 0)
    c.load_entry_object("boost", 1)
    c.load_entry_object("emc_volt", 2)

    # erista
    c.load_entry_object("e_c_max_volt", 3)
    c.load_entry_object("e_emc_max_clock", 1)

    # mariko
    c.load_entry_object("m_cpu_max_volt", 3)
    c.load_entry_object("m_emc_max_clock", 1)
    c.load_entry_object("m_emc_vddq", 2)
    c.load_entry_object("m_cpu_uv", 4)
    c.load_entry_object("m_gpu_uv", 4)
    c.load_entry_object("m_gpu_offset", 3)
    c.load_entry_object("m_cpu_hv_offset", 3)
    c.load_entry_object("m_cpu_huv", 0)

    # CPU/GPU
    c.load_entry_object("cpu_max_freq", 1)
    c.load_entry_object("gpu_max_freq", 1)
    c.load_entry_object("g_vmax", 3)
    c.load_entry_object("g_vmin", 3)
    c.load_entry_object("m_emc_dvb", 0)
    c.load_entry_object("m_emc_latency", 0)

    # ram timings u32
    c.load_entry_object("tBL", 5)
    c.load_entry_object("tRFCpb", 5)
    c.load_entry_object("tRFCab", 5)
    c.load_entry_object("tRAS", 5)
    c.load_entry_object("tRPpb", 5)
    c.load_entry_object("tRPab", 5)
    c.load_entry_object("tRC", 5)
    c.load_entry_object("tWTR", 5)
    c.load_entry_object("tWR", 5)
    c.load_entry_object("tR2REF", 5)
    c.load_entry_object("tRCD", 5)
    c.load_entry_object("tREFpb", 5)
    c.load_entry_object("tMRWCKEL", 5)
    c.load_entry_object("tSR", 5)
    c.load_entry_object("tFAW", 5)

    # ram timings double
    c.load_entry_object("tDQSCK_min", 5)
    c.load_entry_object("tDQSCK_max", 5)
    c.load_entry_object("tWPRE", 5)
    c.load_entry_object("tRPST", 5)
    c.load_entry_object("tDQSS_max", 5)
    c.load_entry_object("tDQS2DQ_max", 5)
    c.load_entry_object("tDQSQ", 5)
    c.load_entry_object("tRTP", 5)
    c.load_entry_object("tRRD", 5)
    c.load_entry_object("tXP", 5)
    c.load_entry_object("tCMDCKE", 5)
    c.load_entry_object("tCKELCS", 5)
    c.load_entry_object("tCSCKEH", 5)
    c.load_entry_object("tXSR", 5)
    c.load_entry_object("tCKE", 5)
    c.load_entry_object("tCKCKEH", 5)

    # GPU volt array
    c.load_entry_object("g_volt_76800", 3)
    c.load_entry_object("g_volt_153600", 3)
    c.load_entry_object("g_volt_230400", 3)
    c.load_entry_object("g_volt_307200", 3)
    c.load_entry_object("g_volt_384000", 3)
    c.load_entry_object("g_volt_460800", 3)
    c.load_entry_object("g_volt_537600", 3)
    c.load_entry_object("g_volt_614400", 3)
    c.load_entry_object("g_volt_691200", 3)
    c.load_entry_object("g_volt_768000", 3)
    c.load_entry_object("g_volt_844800", 3)
    c.load_entry_object("g_volt_921600", 3)
    c.load_entry_object("g_volt_998400", 3)
    c.load_entry_object("g_volt_1075200", 3)
    c.load_entry_object("g_volt_1152000", 3)
    c.load_entry_object("g_volt_1228800", 3)
    c.load_entry_object("g_volt_1267200", 3)
    c.load_entry_object("g_volt_1305600", 3)
    c.load_entry_object("g_volt_1344000", 3)
    c.load_entry_object("g_volt_1382400", 3)
    c.load_entry_object("g_volt_1420800", 3)
    c.load_entry_object("g_volt_1459200", 3)
    c.load_entry_object("g_volt_1497600", 3)
    c.load_entry_object("g_volt_1536000", 3)
    
def freq_to_label(freq):
    if freq > 1382400:
        return f"{freq / 1000:.1f} MHz (DANGEROUS)"
    elif freq > 1152000:
        return f"{freq / 1000:.1f} MHz (UNSAFE)"
    else:
        return f"{freq / 1000:.1f} MHz"
    
def store(sender, app_data):
    global kip_file_path
    kip_file_path=app_data['file_path_name']
    print("Selected" + kip_file_path)
    read_kip(kip_file_path)
    load_all_vars()


        
def grab_kip_storage_values(sender, app_data):
    tag = dpg.get_item_alias(sender) 
    if tag and hasattr(d, tag):
        numeric_str = app_data.split(" ")[0]
        value = int(float(numeric_str) * 1000)
        setattr(d, tag, value)  # store only numeric value
    
    print(tag, app_data, getattr(d, tag))  # shows numeric value
    if(d.autosave == True):
        write_kip()


def grab_kip_storage_values_no_mult(sender, app_data):
    tag = dpg.get_item_alias(sender) 
    if tag and hasattr(d, tag):
        if isinstance(app_data, str):
            numeric_str = re.sub(r"[^0-9.]", "", app_data)
            value = numeric_str
        value = app_data
        setattr(d, tag, value)  # store only numeric value
    
    print(tag, app_data, getattr(d, tag))  # shows numeric value
    if(d.autosave == True):
        write_kip()


def grab_value_freq_conversion(sender, app_data):
    #
    global g_freq_str
    g_freq_str = app_data
    g_freq_val = int(float(g_freq_str.replace(" MHz", "")) * 1000)
    print(g_freq_val)

def write_kip():
    global kip_file_path
    MAGIC = b"CUST"  # 0x43 0x55 0x53 0x54

    type_map = {
        "u32": ("<I", 4, lambda v: int(v) & 0xFFFFFFFF),
        "double": ("<d", 8, lambda v: float(v)),  # ensure float
    }

    if kip_file_path is None:
        if d.autosave:
            c.show_popup("Error", "You need to select a file to use Autosave!")
        else:
            c.show_popup("Error", "You need to select a file to save the KIP!")
        return

    with open(kip_file_path, "r+b") as f:
        data = f.read()
        idx = data.find(MAGIC)
        if idx == -1:
            c.show_popup("Error", "KIP is invalid!")
            return

        pos = idx + len(MAGIC)

        for attr_name, t in variables:
            if t not in type_map:
                c.show_popup("CodeError", f"Incorrect type for {attr_name} in variables table!")
                return

            fmt, size, convert = type_map[t]
            f.seek(pos)

            # Get the actual value from the d module
            value = getattr(d, attr_name)

            # Convert string input to correct numeric type
            try:
                packed_value = struct.pack(fmt, convert(value))
            except (ValueError, TypeError):
                c.show_popup("Error", f"Invalid value for {attr_name}: {value}")
                return

            f.write(packed_value)
            pos += size

    if not d.autosave:
        c.show_popup("Success", "KIP saved successfully!")


def read_kip(filename):
    MAGIC = b"CUST"
    fmt_map = {
        "u32": "<I",
        "double": "<d",
    }

    with open(filename, "rb") as f:
        data = f.read()
        idx = data.find(MAGIC)
        if idx == -1:
            raise ValueError("magic not found!")

        pos = idx + len(MAGIC)

        for attr_name, type_flag in variables:
            if type_flag not in fmt_map:
                raise ValueError(f"bad type: {type_flag}")

            fmt = fmt_map[type_flag]
            size = struct.calcsize(fmt)

            raw_bytes = data[pos:pos + size]
            value = struct.unpack(fmt, raw_bytes)[0]

            if type_flag == "double":
                value = float(value)
            else:
                value = int(value)

            setattr(d, attr_name, value)
            pos += size
    dpg.set_value("gpu_sched", g.check_gpu_sched())
    dpg.show_item("gpu_tab")
    dpg.show_item("cpu_tab")
    dpg.show_item("emc_tab")