from dearpygui import dearpygui as dpg
import misc, time, datetime, config

dpg.create_context()
config.main()

# Themes
with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        # Window
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (19, 19, 22), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255 , 255, 255), category=dpg.mvThemeCat_Core)

        # Button
        dpg.add_theme_color(dpg.mvThemeCol_Button, (57, 58, 65), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (47, 48, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (38, 38, 44), category=dpg.mvThemeCat_Core)

        # Combo
        dpg.add_theme_color(dpg.mvThemeCol_Border, (57, 58, 65), category=dpg.mvThemeCat_Core)         # Border
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (38, 38, 44), category=dpg.mvThemeCat_Core)           # Dropdown menu background
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (47, 48, 55), category=dpg.mvThemeCat_Core)    # Hovered background
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (38, 38, 44), category=dpg.mvThemeCat_Core)    # Active background
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (47, 48, 55), category=dpg.mvThemeCat_Core)    # Hovered background
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (38, 38, 44), category=dpg.mvThemeCat_Core)    # Active background

        # Slider
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255, 255, 255), category=dpg.mvThemeCat_Core)        # Slider knob
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (255, 255, 255), category=dpg.mvThemeCat_Core)    # Active knob

        # Checkbox
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255), category=dpg.mvThemeCat_Core)  # Green checkmark

        # Plot
        dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 255, 255), category=dpg.mvThemeCat_Plots)  # white line color

        # TABS
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (57, 58, 65), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (47, 48, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (38, 38, 44), category=dpg.mvThemeCat_Core)
        # Optional: text color inside tab
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)

    # When the button is disabled (change colors)
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (125 , 125, 125), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (47, 48, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (47, 48, 55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (47, 48, 55), category=dpg.mvThemeCat_Core)

with dpg.theme() as light_theme:
    with dpg.theme_component(dpg.mvAll):
        # Window
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (237, 237, 233), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)

        # Button
        dpg.add_theme_color(dpg.mvThemeCol_Button, (214, 204, 194), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (213, 189, 175), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (227, 213, 202), category=dpg.mvThemeCat_Core)

        # Combo
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (214, 204, 194), category=dpg.mvThemeCat_Core)           # Background
        dpg.add_theme_color(dpg.mvThemeCol_Border, (214, 204, 1945), category=dpg.mvThemeCat_Core)         # Border
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (227, 213, 202), category=dpg.mvThemeCat_Core)           # Dropdown menu background
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (213, 189, 175), category=dpg.mvThemeCat_Core)    # Hovered background
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (213, 189, 175), category=dpg.mvThemeCat_Core)    # Active background
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (213, 189, 175), category=dpg.mvThemeCat_Core)    # Hovered background
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (227, 213, 202), category=dpg.mvThemeCat_Core)    # Active background

        # Slider
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255, 255, 255), category=dpg.mvThemeCat_Core)        # Slider knob
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (255, 255, 255), category=dpg.mvThemeCat_Core)    # Active knob

        # Checkbox
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (0, 0, 0), category=dpg.mvThemeCat_Core)  # Green checkmark

        # Plot
        dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 0, 0), category=dpg.mvThemeCat_Plots)  # black line color

        # TABS
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (214, 204, 194), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (213, 189, 175), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (227, 213, 202), category=dpg.mvThemeCat_Core)
        # Optional: text color inside tab
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)

    # When the button is disabled (change colors)
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (125 , 125, 125), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (224, 214, 204), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (224, 214, 204), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (224, 214, 204), category=dpg.mvThemeCat_Core)

last_click_time = [0] # variable to store the last time the button was clicked.

# Put the followig variables in a config file!!!!!!!!!!!!!!!!
api_request_delay = int(config.get_data('Settings', 'api_request_delay')) # amount of seconds to be able to update the data from the api request.
auto_update_delay = int(config.get_data('Settings', 'auto_update_delay')) # variable in frames.
can_auto_update = config.get_data('Settings', 'can_auto_update') == 'True' # allow the app to auto update the data from the API call.

# Dividend data (for line chart)
x_data = list(map(int, config.get_data('Dividends', 'month').split(',')))
y_data = list(map(float, config.get_data('Dividends', 'value').split(',')))

def update_api():
    #print("call")
    current_time = time.time()
    if current_time - last_click_time[0] < api_request_delay:
        return
    
    #update API data
    data = misc.get_account_cash()
    dpg.set_value(free_text, f" [Free]     {data['free']}(EUR)")
    dpg.set_value(equi_text, f" [Equity]   {data['invested']}(EUR)")
    dpg.set_value(pnl_text, f" [PnL]      {data['ppl']}(EUR) {(data['ppl']*100)/data['invested']:.2f}%")
    dpg.set_value(total_text, f" [Total]    {data['total']}(EUR)")
    dpg.set_value(last_updated_text, f" Last updated {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

    last_click_time[0] = current_time
    dpg.configure_item("update_btn", enabled=False, label='Updating...')
    dpg.configure_item("spinner", show=True)
    dpg.set_frame_callback(dpg.get_frame_count() + 300, lambda: (
        dpg.configure_item("update_btn", enabled=True, label="Update"), 
        dpg.configure_item("spinner", show=False))
        )

    if state["checkbox_state"] == True:
        dpg.set_frame_callback(dpg.get_frame_count() + state["slider_value"], update_api)

def switch_theme(sender, app_data):
    if app_data == "Dark Theme":
        dpg.bind_theme(dark_theme)
        config.update_data('Settings', 'theme', str(app_data)) # Update config file
    elif app_data == "Light Theme":
        dpg.bind_theme(light_theme)
        config.update_data('Settings', 'theme', str(app_data)) # Update config file

def on_change(sender, app_data, user_data):
    if sender == auto_update_cbox:
        user_data["checkbox_state"] = app_data
        config.update_data('Settings', 'can_auto_update', str(app_data)) # Update config file
    elif sender == update_delay_slider:
        user_data["slider_value"] = app_data
        config.update_data('Settings', 'auto_update_delay', str(app_data)) # Update config file
    print(user_data)
    
state = {"slider_value": auto_update_delay, "checkbox_state": can_auto_update}

# Main window
with dpg.window(label="portfolio", width=500, height=900) as main_window:
    def close_app():
        dpg.stop_dearpygui()

    with dpg.tab_bar():
        with dpg.tab(label="Portfolio"):
            with dpg.group(horizontal=True):
                dpg.add_text(" Personal Toolbox")
                dpg.add_spacer(width=245)
                dpg.add_combo(["Dark Theme", "Light Theme"], callback=switch_theme, default_value=config.get_data('Settings', 'theme'), width=150)
                #dpg.add_spacer(width=25)
                dpg.add_button(label='X', width=30, callback=close_app)

            dpg.add_spacer(height=15)
            dpg.add_text(" ===========[ Portfolio ]===========")
            free_text = dpg.add_text(f" [Free]     0(EUR)")
            equi_text = dpg.add_text(f" [Equity]   0(EUR)")
            pnl_text = dpg.add_text(f" [PnL]      0(EUR) 0%")
            total_text = dpg.add_text(f" [Total]    0(EUR)")

            with dpg.group(horizontal=True):
                dpg.add_button(label="Update", width=250, height=35, callback=update_api, tag="update_btn")
                dpg.add_loading_indicator(tag='spinner', radius=2.5, show=False)

            last_updated_text = dpg.add_text(" Last updated: ")

            dpg.add_text(" ============[ Settings ]===========")
            auto_update_cbox = dpg.add_checkbox(label="Auto update", default_value=can_auto_update, callback=on_change, user_data=state)
            update_delay_slider = dpg.add_slider_int(min_value=400, max_value=9999, default_value=auto_update_delay, width=250, label="Update delay", callback=on_change, user_data=state)
            dpg.add_text(" ===================================")

            with dpg.plot(label="Dividend Payments", height=250, width=-1):
                dpg.add_plot_axis(dpg.mvXAxis, label="Month")
                with dpg.plot_axis(dpg.mvYAxis, label="Amount(EUR)") as y_axis:
                    dpg.add_line_series(x_data, y_data, label="Line", parent=y_axis)
        with dpg.tab(label="Stocks"):
            dpg.add_text("Incomeshares ETP data")
        

dpg.set_frame_callback(dpg.get_frame_count() + 1, update_api) # Update data using API on startup

# Setup theme
if config.get_data('Settings', 'theme') == 'Light Theme':
    dpg.bind_theme(light_theme) #Theme setup
elif config.get_data('Settings', 'theme') == 'Dark Theme':
    dpg.bind_theme(dark_theme) #Theme setup

dpg.create_viewport(title='Personal Toolbox', width=600, height=620, decorated=True, resizable=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(main_window, True)

dpg.start_dearpygui()
dpg.destroy_context()
