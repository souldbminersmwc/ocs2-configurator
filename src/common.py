import dearpygui.dearpygui as dpg    

def show_info_window(sender, app_data, user_data):
    window_tag = "info_window" + user_data
    if not dpg.does_item_exist(window_tag):
        with dpg.window(label="Information", tag=window_tag, width=400, height=200):
            wrap_width = dpg.get_item_width(window_tag) - 10
            dpg.add_text(user_data, wrap=wrap_width)
    else:
        dpg.show_item(window_tag)

def store_value(sender, app_data, user_data=None):
    var_name = f"{dpg.get_item_(sender)}_value"
    globals()[var_name] = app_data
    print(f"{var_name} = {app_data}")

def get_value(tag, default=None):
    var_name = f"{tag}_value"
    return globals().get(var_name, default)