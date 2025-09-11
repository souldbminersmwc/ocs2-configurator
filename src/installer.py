
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
import psutil
import os
import common as c
import urllib.request
import zipfile
import kip as k
from defaults import d

def autosave_toggle(sender, app_data):
    d.autosave=app_data
    print(f"Autosave toggled to {d.autosave}")


def get_drives():
    drives = []
    for part in psutil.disk_partitions(all=False):
        drives.append(part.device)
    return drives


# Change if you plan to fork
kip_download_link="https://github.com/souldbminersmwc/Switch-OC-Suite-2/releases/latest/download/loader.kip"
sys_clk_ocs2_download_link="https://github.com/souldbminersmwc/Switch-OC-Suite-2/releases/latest/download/sys-clk-ocs2.zip"


def downloadLoader():
    print("Downloading ocs2.kip...")
    if c.drive==0:
        print("Drive not selected!")
        c.show_popup(title="Error:", content="Please select a installation c.drive first!")
    else:
        try:
            directory_make = c.drive + "atmosphere/kips/"
            urllib.request.urlretrieve(kip_download_link, directory_make + "ocs2.kip")
        except Exception as e:
            c.show_popup(title="Error", content=f"Download failed:\n{e}")
        finally:
            c.show_popup(title="Info:", content="Downloaded kip!")


def downloadSysClk():
    if c.drive == 0:
        print("Drive not selected!")
        c.show_popup(title="Error:", content="Please select an installation c.drive first!")
        return

    zip_filename = "ocs2_clk.zip"
    zip_path = os.path.join(c.drive, zip_filename)

    try:
        print(f"Downloading {zip_filename} to {c.drive} ...")
        urllib.request.urlretrieve(sys_clk_ocs2_download_link, zip_path)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(c.drive)

        c.show_popup(title="Success", content="Installed sys-clk-ocs2!")

    except Exception as e:
        print(f"Download or extraction failed: {e}")
        c.show_popup(title="Error", content=f"Download failed:\n{e}")

    finally:
        if os.path.exists(zip_path):
            os.remove(zip_path)


drive_list = get_drives()

def check_atmosphere(sender, app_data, user_data):
    c.drive = app_data
    atmosphere_path = os.path.join(c.drive, "atmosphere")
    package3_path = os.path.join(atmosphere_path, "package3")
    if os.path.isfile(f"{atmosphere_path}/kips/ocs2.kip"):
        dpg.set_value("status_text", "OCS2 Install Found!")
        k.kip_file_path = f"{atmosphere_path}/kips/ocs2.kip"
        k.read_kip(c.drive + "atmosphere/kips/ocs2.kip")
        print(f"Reading kip from c.drive {c.drive}")
        k.load_all_vars()
    elif os.path.isdir(atmosphere_path) and os.path.isfile(package3_path):
        dpg.set_value("status_text", "Atmosphere install found!")
    else:
        dpg.set_value("status_text", "Atmosphere not found!")
