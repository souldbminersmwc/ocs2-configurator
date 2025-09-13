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
from defaults import d
import common as c
timing_vars = [
    "d.tBL",
    "d.tRFCpb",
    "d.tRFCab",
    "d.tRAS",
    "d.tRPpb",
    "d.tRPab",
    "d.tRC",
    "d.tDQSCK_min",
    "d.tDQSCK_max",
    "d.tWPRE",
    "d.tRPST",
    "d.tDQSS_max",
    "d.tDQS2DQ_max",
    "d.tDQSQ",
    "d.tWTR",
    "d.tRTP",
    "d.tWR",
    "d.tR2REF",
    "d.tRCD",
    "d.tRRD",
    "d.tREFpb",
    "d.tXP",
    "d.tCMDCKE",
    "d.tMRWCKEL",
    "d.tCKELCS",
    "d.tCSCKEH",
    "d.tXSR",
    "d.tCKE",
    "d.tSR",
    "d.tFAW",
    "d.tCKCKEH"
]

timing_preset_default = [
    16,   # tBL
    140,  # tRFCpb
    280,  # tRFCab
    42,   # tRAS
    18,   # tRPpb
    21,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    10,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    18,   # tRCD
    10.0, # tRRD
    488,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_aamgcl_c = [
    # Ignore tRTW, it is autocalculated
    16,   # tBL
    70,  # tRFCpb
    140,  # tRFCab (tRFCpb * 2)
    28,   # tRAS
    14,   # tRPpb
    17,   # tRPab (tRPpb + 3)
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    3,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    3.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_aamgcl_st = [
    # Ignore tRTW, it is autocalculated
    16,   # tBL
    70,  # tRFCpb
    140,  # tRFCab (tRFCpb * 2)
    22,   # tRAS
    14,   # tRPpb
    17,   # tRPab (tRPpb + 3)
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    2,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    2.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_mgcj_c = [
    16,   # tBL
    80,  # tRFCpb
    160,  # tRFCab
    30,   # tRAS
    16,   # tRPpb
    19,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    6,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    15,   # tRCD
    6.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_mgcj_st = [
    16,   # tBL
    70,  # tRFCpb
    140,  # tRFCab
    20,   # tRAS
    15,   # tRPpb
    18,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    6,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    6.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_ab_mgcl_c = [
    16,   # tBL
    80,  # tRFCpb
    160,  # tRFCab
    20,   # tRAS
    14,   # tRPpb
    17,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    4,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    4.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_ab_mgcl_st = [
    16,   # tBL
    70,  # tRFCpb
    140,  # tRFCab
    22,   # tRAS
    14,   # tRPpb
    17,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    2,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    3.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_wtb_c = [
    16,   # tBL
    100,  # tRFCpb
    200,  # tRFCab
    28,   # tRAS
    14,   # tRPpb
    17,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    5,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    14,   # tRCD
    3.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

timing_preset_wtb_st = [
    16,   # tBL
    100,  # tRFCpb
    200,  # tRFCab
    24,   # tRAS
    12,   # tRPpb
    15,   # tRPab
    60,   # tRC
    1.5,  # tDQSCK_min
    3.5,  # tDQSCK_max
    1.8,  # tWPRE
    0.4,  # tRPST
    1.25, # tDQSS_max
    0.8,  # tDQS2DQ_max
    0.18, # tDQSQ
    5,   # tWTR
    7.5,  # tRTP
    18,   # tWR
    25.5,   # tR2REF
    12,   # tRCD
    1.0, # tRRD
    9999,  # tREFpb
    10,   # tXP
    1.75, # tCMDCKE
    14,   # tMRWCKEL
    5,    # tCKELCS
    1.75, # tCSCKEH
    287.5,# tXSR
    7.5,  # tCKE
    15,   # tSR
    40,   # tFAW
    1.75  # tCKCKEH
]

def load_defaults():
    apply_timing_preset(timing_preset_default)

def temporary_presets_unavailable():
    c.show_popup_big("We need your help!", "This timing preset currently unavailable due to lack of data. If you have a ram module and want to contribute your data, reach out to me (soul_9017) on the OC discord")

def apply_timing_preset(preset):

    if len(preset) != len(timing_vars):
        raise ValueError("Preset invalid!")
    
    for var_name, value in zip(timing_vars, preset):
        setattr(d, var_name.split('.')[-1], value)

        flag = 0 if var_name.endswith("tBL") else 5

        c.load_entry_object(var_name.split('.')[-1], flag)
    c.show_popup("Sucess", "Preset Applied!")

def apply_reg_timings(sender, app_data):
    ram_selected = dpg.get_value("ram_type")
    print(ram_selected)
    match(ram_selected):
        case "Choose your RAM Type!":
            c.show_popup("Error", "You must select a ram type to apply a preset")
        case "Samsung AA-MGCL/MGCR":
            apply_timing_preset(timing_preset_aamgcl_c)
        case "Samsung AM-MGCJ":
            apply_timing_preset(timing_preset_mgcj_c)
        case "Samsung AB-MGCL":
            apply_timing_preset(timing_preset_ab_mgcl_c)
        case "Micron WT:B":
            apply_timing_preset(timing_preset_wtb_c)
        case _:
            temporary_presets_unavailable()

def apply_st_timings(sender, app_data):
    ram_selected = dpg.get_value("ram_type")
    match(ram_selected):
        case "Choose your RAM Type!":
            c.show_popup("Error", "You must select a ram type to apply a preset")
        case "Samsung AA-MGCL/MGCR":
            apply_timing_preset(timing_preset_aamgcl_st)
        case "Samsung AM-MGCJ":
            apply_timing_preset(timing_preset_mgcj_st)
        case "Samsung AB-MGCL":
            apply_timing_preset(timing_preset_ab_mgcl_st)
        case "Micron WT:B":
            apply_timing_preset(timing_preset_wtb_st)
        case _:
            temporary_presets_unavailable()

