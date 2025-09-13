
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


class Defaults:
    def __init__(self):
        self.autosave = 0
        self.custrev = 2
        self.mtc = 0
        self.boost = 1785000
        self.emc_volt = 1175000
        self.e_c_max_volt = 1235
        self.e_emc_max_clock = 1862400
        self.m_cpu_max_volt = 1120
        self.m_emc_max_clock = 1996800
        self.m_emc_vddq = 600000
        self.m_cpu_uv = 0
        self.m_gpu_uv = 0
        self.m_gpu_offset = 0
        self.m_cpu_hv_offset = 0
        self.m_cpu_huv = 0
        self.cpu_max_freq = 1785000
        self.gpu_max_freq = 921600
        self.g_vmin = 600
        self.g_vmax = 800
        self.m_emc_dvb = 0
        self.m_emc_latency = 0
        self.tBL = 16
        self.tRFCpb = 140
        self.tRFCab = 280
        self.tRAS = 42
        self.tRPpb = 18
        self.tRPab = 21
        self.tRC = 60
        self.tDQSCK_min = 1.5
        self.tDQSCK_max = 3.5
        self.tWPRE = 1.8
        self.tRPST = 0.4
        self.tDQSS_max = 1.25
        self.tDQS2DQ_max = 0.8
        self.tDQSQ = 0.18
        self.tWTR = 10
        self.tRTP = 7.5
        self.tWR = 18
        self.tR2REF = 25
        self.tRCD = 18
        self.tRRD = 10.0
        self.tREFpb = 488
        self.tXP = 10
        self.tCMDCKE = 1.75
        self.tMRWCKEL = 14
        self.tCKELCS = 5
        self.tCSCKEH = 1.75
        self.tXSR = 287.5
        self.tCKE = 7.5
        self.tSR = 15
        self.tFAW = 40
        self.tCKCKEH = 1.75
        self.m_freq_76800 = 600
        self.m_freq_153600 = 600
        self.m_freq_230400 = 600
        self.m_freq_307200 = 600
        self.m_freq_384000 = 600
        self.m_freq_460800 = 600
        self.m_freq_537600 = 600
        self.m_freq_614400 = 600
        self.m_freq_691200 = 600
        self.m_freq_768000 = 600
        self.m_freq_844800 = 605
        self.m_freq_921600 = 635
        self.m_freq_998400 = 665
        self.m_freq_1075200 = 695
        self.m_freq_1152000 = 730
        self.m_freq_1228800 = 760
        self.m_freq_1267200 = 785
        self.m_freq_1305600 = 800
        self.m_freq_1344000 = 0
        self.m_freq_1382400 = 0
        self.m_freq_1420800 = 0
        self.m_freq_1459200 = 0
        self.m_freq_1497600 = 0
        self.m_freq_1536000 = 0


# Create a global instance
d = Defaults()