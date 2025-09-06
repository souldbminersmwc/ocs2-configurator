import dearpygui.dearpygui as dpg
import common
def populate():
    freqs_hz_cpu = [
        204000, 306000, 408000, 510000, 612000, 714000, 816000, 918000,
        1020000, 1122000, 1224000, 1326000, 1428000, 1581000, 1683000,
        1785000, 1887000, 1963500, 2091000, 2193000, 2295000, 2397000,
        2499000, 2601000, 2703000, 2805000, 2907000
    ]
    freqs_mhz_cpu = [
        204.0, 306.0, 408.0, 510.0, 612.0, 714.0, 816.0, 918.0,
        1020.0, 1122.0, 1224.0, 1326.0, 1428.0, 1581.0, 1683.0,
        1785.0, 1887.0, 1963.5, 2091.0, 2193.0, 2295.0, 2397.0,
        2499.0, 2601.0, 2703.0, 2805.0, 2907.0
    ]
    freqs_mhz_cpu_label = [f"{f} MHz" for f in freqs_mhz_cpu]
    offsets = list(range(0, 101, 5))
    processed_offsets = ["Disabled" if v == 0 else f"-{v}mV" for v in offsets]
    voltages = [0] + list(range(700, 1235 + 1, 5))  # 0 first for Disabled
    processed_voltages = ["Disabled" if v == 0 else f"{v}mV" for v in voltages]
    processed_voltages_default = ["Default" if v == 0 else f"{v}mV" for v in voltages]


    dpg.add_text("Speedos")
    dpg.add_input_text(label="CPU Speedo")

    dpg.add_separator()

    dpg.add_text("Frequencies")
    dpg.add_button(
            label="What is this?",
            callback=common.show_info_window,
            user_data="A higher CPU frequency significantly increases power draw. To sustain higher frequencies without exeeding PMIC limit, undervolt your device",
            width=120,
            height=64,  # height=0 makes it match text
            small=True,
            tag="c_freqs_info"
    )
    dpg.add_combo(
        items=freqs_mhz_cpu_label,
        default_value="1785.0MHz",
        label="CPU Max Frequency"
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
            tag="c_volt_info"
    )
    dpg.add_combo(
        items=processed_voltages,
        default_value="Disabled",
        label="CPU vMin",
        tag="cpu_vmin"
    )
    dpg.add_combo(
        items=processed_voltages,
        default_value="Disabled",
        label="CPU vMax",
        tag="cpu_vmax"
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
        tag="c_uv_info"
    )
    dpg.add_combo(
        items=["Default Table", "High Table"],
        default_value="Default Table",
        label="Undervolt",
        tag="c_uv_mode"
    )
    dpg.add_combo(
        items=["Default Table", "High Table", "Extreme Table"],
        default_value="Default Table",
        label="High Frequency Undervolt",
        tag="c_huv_mode"
    )
    dpg.add_combo(
        items=processed_offsets,
        default_value="Disabled",
        label="CPU Volt Offset",
        tag="c_volt_offset"
    )