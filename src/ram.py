
"""

HOC Configurator

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
import common
import kip as k
import preset
from defaults import d

def populate():

    # Values in kHz
    adjusted_freqs_khz = [
        0, 1601280, 1633920, 1666560, 1701120, 1733760, 1766400, 1800000,
        1832640, 1865280, 1900800, 1933440, 1966080, 2000000, 2032640,
        2065280, 2100000, 2132640, 2165280, 2200000, 2232640, 2265280,
        2300000, 2332640, 2365280, 2400000, 2432640, 2465280, 2500000,
        2532640, 2565280, 2600000, 2632640, 2665280, 2700000, 2732640,
        2765280, 2800000, 2832640, 2865280, 2900000, 2932640, 2965280,
        3000000, 3032640, 3065280, 3100000, 3132640, 3165280, 3200000
    ]
    voltages_uv = [
    0, 1050000, 1062500, 1075000, 1087500, 1100000, 1112500, 1125000,
    1137500, 1150000, 1162500, 1175000, 1187500, 1200000, 1212500
    ]
    vddq_uv = [
    0, 550000, 555000, 560000, 565000, 570000, 575000, 580000, 585000, 590000, 595000,
    600000, 605000, 610000, 615000, 620000, 625000, 630000, 635000, 640000, 645000,
    650000
    ]
    voltages_mv = [v / 1000 for v in voltages_uv]
    voltages_mv_label = ["Default (1175 mV)" if f == 0 else f"{f} mV" for f in voltages_mv]
    vddq_mv = [v / 1000 for v in vddq_uv]
    vddq_mv_label = ["Default (600 mV)" if f == 0 else f"{f} mV" for f in vddq_mv]
    # Values in MHz (converted)
    values_mhz = [v / 1000 for v in adjusted_freqs_khz]
    values_mhz_label_m = ["Default (1996.8 MHz)" if f == 0 else f"{f} MHz" for f in values_mhz]
    values_mhz_label_e = ["Default (1862.4 MHz)" if f == 0 else f"{f} MHz" for f in values_mhz]
    dvb = [i for i in range(10)]
    dpg.add_separator(label="RAM Types")
    dpg.add_combo(
        items=["Samsung AA-MGCL/MGCR", "SK Hynix NEI/NEE", "SK Hynix x267", "Micron WT:B", "Micron AUT:B", "Micron WT:F", "Samsung AM-MGCJ", "Micron WT:E", "Samsung AB-MGCL", "Hynix NME", "Samsung HB-MGCH"],
        default_value="Choose your RAM Type!",
        label="RAM Type",
        tag="ram_type"
    )
    dpg.add_button(label="Apply Regular Preset", callback=preset.apply_reg_timings)
    dpg.add_button(label="Apply Tight Preset", callback=preset.apply_st_timings)
    dpg.add_button(label="Load Default Preset", callback=preset.load_defaults)

    dpg.add_separator(label="Frequencies (Mariko)")
    dpg.add_text("Multiple Ram Frequencies on Mariko is in development")
    dpg.add_combo(
        items=values_mhz_label_m,
        default_value="Default (1996.8 MHz)",
        label="RAM Max Frequency (Mariko)",
        tag="marikoEmcMaxClock",
        callback=k.grab_kip_storage_values

    )

    dpg.add_separator(label="Frequencies (Erista)")
    dpg.add_text("Multiple Ram Frequencies on Erista is in development")

    # dpg.add_combo(
    #     items=values_mhz_label_e,
    #     default_value="Default (2132.64 MHz)",
    #     label="RAM Max Frequency (Erista)",
    #     tag="e_emc_clock_1",
    #     callback=k.grab_kip_storage_values
    # )
    # dpg.add_combo(
    #     items=values_mhz_label_e,
    #     default_value="Default (1996.8 MHz)",
    #     label="RAM Second Frequency (Erista)",
    #     tag="e_emc_clock_2",
    #     callback=k.grab_kip_storage_values
    # )
    dpg.add_combo(
        items=values_mhz_label_e,
        default_value="Default (1862.4 MHz)",
        label="RAM Max Frequency (Erista)",
        tag="eristaEmcMaxClock",
        callback=k.grab_kip_storage_values
    )
    dpg.add_separator(label="Voltages")

    dpg.add_combo(
        items=voltages_mv_label,
        default_value="Default (1175 mV)",
        label="RAM Primary Voltage (VDD2)",
        tag="commonEmcMemVolt",
        callback=k.grab_kip_storage_values
    )
    dpg.add_combo(
        items=vddq_mv_label,
        default_value="Default (600 mV)",
        label="RAM Secondary Voltage (VDDQ, Mariko ONLY)",
        tag="marikoEmcVddqVolt",
        callback=k.grab_kip_storage_values
    )
    dpg.add_combo(
        items=dvb,
        default_value="0",
        label="SoC DVB Shift",
        callback=k.grab_kip_storage_values_no_mult,
        tag="marikoEmcDvbShift"
    )

    dpg.add_separator(label="Primary Timings")

    dpg.add_combo(
        items=["0", "2"],
        default_value="2",
        label="Burst Latency",
        callback=k.grab_kip_storage_values_no_mult,
        tag="mem_burst_latency"
    )
    dpg.add_slider_int(label="t1 tRCD", min_value=0, max_value=7, tag="t1_tRCD", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t2 tRP", min_value=0, max_value=7, tag="t2_tRP", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t3 tRAS", min_value=0, max_value=9, tag="t3_tRAS", callback=k.grab_kip_storage_values_no_mult)

    dpg.add_separator(label="Secondary Timings")

    dpg.add_slider_int(label="t4 tRRD", min_value=0, max_value=7, tag="t4_tRRD", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t5 tRFC", min_value=0, max_value=5, tag="t5_tRFC", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t6 tRTW", min_value=0, max_value=9, tag="t6_tRTW", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t7 tWTR", min_value=0, max_value=9, tag="t7_tWTR", callback=k.grab_kip_storage_values_no_mult)
    dpg.add_slider_int(label="t8 tREFI", min_value=0, max_value=5, tag="t8_tREFI", callback=k.grab_kip_storage_values_no_mult)