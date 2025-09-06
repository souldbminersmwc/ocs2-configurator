import dearpygui.dearpygui as dpg
import common


def populate():
    dpg.add_text("Speedos & Ram Type")
    dpg.add_input_text(label="SoC Speedo")
    dpg.add_combo(
        items=["Samsung AA-MGCL/MGCR", "SK Hynix NEI/NEE", "SK Hynix H54", "Micron WT:B", "Micron AUT:B", "Micron WT:F", "Samsung AM-MGCJ", "Micron WT:E", "Samsung AB-MGCL / 1z", "Hynix NME", "Samsung HB-MGCH", "Micron WT:C", "Hynix NLE"],
        default_value="Choose your RAM Type!",
        label="RAM Type",
        tag="ram_type"
    )
    dpg.add_separator()