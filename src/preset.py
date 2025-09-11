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
    26,   # tR2REF
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

def load_defaults():
    apply_timing_preset(timing_preset_default)
    c.show_popup("Sucess!", "Preset applied!")
def temporary_presets_unavailable():
    c.show_popup_big("We need your help!", "Timing presets are currently unavailable due to lack of data. If you have a ram module and want to contribute your data, reach out to me (soul_9017) on the OC discord")
def apply_timing_preset(preset):

    if len(preset) != len(timing_vars):
        raise ValueError("Preset invalid!")
    
    for var_name, value in zip(timing_vars, preset):
        setattr(d, var_name.split('.')[-1], value)  # use only part after "d."

        flag = 0 if var_name.endswith("tBL") else 5

        c.load_entry_object(var_name.split('.')[-1], flag)
