import dearpygui.dearpygui as dpg
import common
def populate():
    offsets = list(range(0, 101, 5))
    processed_offsets = ["Disabled" if v == 0 else f"-{v}mV" for v in offsets]
    voltages = [0] + list(range(480, 960 + 1, 5))  # 0 first for Disabled
    processed_voltages = ["Disabled" if v == 0 else f"{v}mV" for v in voltages]
    processed_voltages_default = ["Default" if v == 0 else f"{v}mV" for v in voltages]
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

    dpg.add_text("Speedos")
    dpg.add_input_text(label="GPU Speedo")

    dpg.add_separator()

    dpg.add_text("Frequencies")
    dpg.add_button(
            label="What is this?",
            callback=common.show_info_window,
            user_data="A higher GPU frequency significantly increases power draw. To sustain higher frequencies without exeeding PMIC limit, undervolt your device \nDO NOT enable GPU scheduling without a adequate undervolt as it can cause hardware damage due to the high power consumption",
            width=120,
            height=64,  # height=0 makes it match text
            small=True,
            tag="freqs_info"
    )
    dpg.add_checkbox(label="GPU Scheduling", default_value=True)
    dpg.add_combo(
        items=freqs_mhz_label,
        default_value="1152.0MHz",
        label="GPU Max Frequency"
    )

    dpg.add_separator()

    dpg.add_text("Voltages")
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
        tag="gpu_vmin"
    )
    dpg.add_combo(
        items=processed_voltages,
        default_value="Disabled",
        label="Gpu vMax",
        tag="gpu_vmax"
    )

    dpg.add_separator()


    dpg.add_text("Undervolt")

    dpg.add_button(
        label="What is this?",
        callback=common.show_info_window,
        user_data="A undervolted device consumes less power, heats up less, which enables higher clocks. \nThe GPU Undervolt mode should be set to Default or High, test which one is suitable to your console. Custom is only meant for ADVANCED USERS, as the values in it could cause HARDWARE DAMAGE! \nThe Offset should be kept at the minumum your GPU requires to function at the high ram clock (high ram clock means more GPU power needed, usually 600mV is sufficient)",
        width=120,
        height=64,  # height=0 makes it match text
        small=True,
        tag="uv_info"
    )
    dpg.add_combo(
        items=["Default Table", "High Table", "Custom Table"],
        default_value="Default Table",
        label="Undervolt Modes",
        tag="uv_mode"
    )
    dpg.add_combo(
        items=processed_offsets,
        default_value="Disabled",
        label="Gpu Volt Offset",
        tag="volt_offset"
    )

    dpg.add_separator()

    dpg.add_text("GPU Custom Table")
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
                    label=mhz_label
                )
                dpg.add_image("coolerhd", width=16, height=16)
        else:
            dpg.add_combo(
                items=processed_voltages,
                default_value="Disabled",
                label=mhz_label
            )