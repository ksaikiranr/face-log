#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

#: import main test2
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton



<RegisterScreen>:
    first_name_text_input: first_name
    last_name_text_input: last_name
    BoxLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                source: 'data/images/background.jpg'
                size: self.size
        orientation: "vertical"
        padding: 10
        spacing: 10
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                font_style: 'Body1'
                theme_text_color: 'Primary'
                color: (1, 1, 1, .8)
                text: "Register Screen"
                halign: 'center'
                size_hint_x: 15
                font_size: "35dp"
        BoxLayout:
            size_hint_y: None
            height: "48dp"
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                halign: 'center'
                size: root.width, root.height * 0.2
                font_size: "20dp"
                color: (1, 1, 1, .8)
                text: "First Name"
            MDTextField:
                hint_text: "First Name is required!"
                required: True
                helper_text_mode: "on_error"
                color: (1, 1, 1, .8)
                foreground_color: (1,1,1,0.9)
                hint_text_color: (1,1,1,0.5)
                line_color_focus: (1,1,1,0.9)
                line_color_normal: (1,1,1,0.5)
                _current_error_color: (1,1,1,0.5)
                _current_hint_text_color: (1,1,1,0.5)
                cursor_color: (0,1,1,1)
                id: first_name
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                halign: 'center'
                size: root.width, root.height * 0.2
                font_size: "20dp"
                color: (1, 1, 1, .8)
                text: "Last Name"
            MDTextField:
                hint_text: "Last name is required!"
                required: True
                helper_text_mode: "on_error"
                color: (1, 1, 1, .8)
                foreground_color: (1,1,1,0.9)
                hint_text_color: (1,1,1,0.5)
                line_color_focus: (1,1,1,0.9)
                line_color_normal: (1,1,1,0.5)
                _current_error_color: (1,1,1,0.5)
                _current_hint_text_color: (1,1,1,0.5)
                cursor_color: (0,1,1,1)
                id: last_name


        BoxLayout:
            size_hint_y: None
            height: "40dp"
            padding: 10
            spacing: 20
            MDRaisedButton:
                text: "Start Camera"
                size_hint_x: 15
                on_press: root.dostart(root.capture)
            MDRaisedButton:
                text: "Stop Camera"
                size_hint_x: 15
                on_press: root.doexit()
            MDRaisedButton:
                text: "Cancel Register"
                size_hint_x: 15
                on_press: root.manager.current = 'screen-home'

        BoxLayout:
            size_hint_y: None
            height: "30dp"
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                color: (1, 1, 1, .8)
                halign: 'center'
                size: root.width, root.height * 0.2
                font_size: "20dp"
                text: "Please align your face with camera for sample image."

        BoxLayout:
            KivyCameraReg:
                id: qrcamReg
        BoxLayout:
            size_hint_y: None
            height: "30dp"
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                color: (1, 1, 1, .8)
                halign: 'center'
                size: root.width, root.height * 0.2
                font_size: "20dp"
        BoxLayout:
            size_hint_y: None
            height: "30dp"
            padding: 10
            spacing: 20
            MDRaisedButton:
                text: "Capture Image"
                size_hint_x: 15
                on_press: root.capture_user()
            MDRaisedButton:
                text: "Verify and Submit"
                size_hint_x: 15
                on_press:
                    root.doexit()
                    root.manager.current = 'screen-login'


<LoginScreen>:
    BoxLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                source: 'data/images/background.jpg'
                size: self.size
        id: home_container
        orientation: "vertical"
        spacing: 10
        padding: 10

        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Login Screen"
                color: (1, 1, 1, .8)
                halign: 'center'
                size_hint_x: 15
                font_size: "35dp"
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                color: (1, 1, 1, .8)
                text: "Please align your face with camera for authentication."
                halign: 'center'
                size_hint_x: 15
                font_size: "15dp"

        BoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: 30
            padding: 20
            MDRaisedButton:
                text: "Start Camera"
                size_hint_x: 15
                on_press: root.dostart()
            MDRaisedButton:
                text: "Stop Camera"
                size_hint_x: 15
                on_press:
                    root.dostop()

        BoxLayout:
            id: login_cam
            size_hint_y: None
            height: root.height * 0.65



<HomeScreen>:


    users_list: users_list_view

    BoxLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                source: 'data/images/background.jpg'
                size: self.size
        orientation: "vertical"
        spacing: 10
        padding: 10


        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Login Screen"
                halign: 'center'
                size_hint_x: 15
                color: (1, 1, 1, .8)
                font_size: "35dp"
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                text: "Please note, all actions performed in this window are irreversible."
                halign: 'center'
                size_hint_x: 15
                color: (1, 1, 1, .8)
                font_size: "20dp"

        BoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: 30
            padding: 20
            MDRaisedButton:
                text: "Add User"
                opposite_colors: True
                size_hint: (None, None)
                on_release: root.dispatch('on_newuser')
                size_hint_x: 15
            MDRaisedButton:
                text: "Delete User"
                opposite_colors: True
                on_release: root.delete_user()
                size_hint: (None, None)
                size_hint_x: 15
            MDRaisedButton:
                text: "Log Out"
                opposite_colors: False
                on_release:
                    root.manager.current = 'screen-login'
                size_hint: (None, None)
                size_hint_x: 15
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            spacing: 30
            padding: 20
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                font_style: 'Headline'
                text: "Users List"
                color: (1, 1, 1, .8)
                halign: 'center'
                font_size: "20dp"
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                text: "User Details"
                font_style: 'Headline'
                color: (1, 1, 1, .8)
                halign: 'center'
                font_size: "20dp"
        BoxLayout:
            id: login_cam
            size_hint_y: None
            height: root.height * 0.65
            padding: 10
            spacing: 10
            MDCard:
                md_bg_color: (.15, 0.15, 0.15, 1)
                padding: 5
                spacing: 5
                ListView:
                    id: users_list_view
                    adapter:
                        ListAdapter(data=[], cls= main.UserImagesButton, selection_mode='single', allow_empty_selection=True)
            BoxLayout:
                id: detail_user


<bhila>:


    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 10

        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 5
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Login Screen"
                halign: 'center'
                size_hint_x: 15
                font_size: "35dp"
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            padding: 5
            spacing: 10
            MDLabel:
                font_name: 'Lato-Regular.ttf'
                theme_text_color: 'Primary'
                text: "Please note, all actions performed in this window are irreversible."
                halign: 'center'
                size_hint_x: 15
                font_size: "15dp"


        BoxLayout:
            size_hint_y: None
            height: "40dp"
            spacing: 30
            padding: 20
            Button:
                text: "Add User"
                opposite_colors: True
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                halign: 'center'
                on_press: root.add_user()
            MDRaisedButton:
                text: "Add User"
                opposite_colors: True
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                halign: 'center'
                on_release: root.add_user()
            MDRaisedButton:
                text: "Edit User"
                opposite_colors: True
                halign: 'center'
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                on_release: root.edit_user()
            MDRaisedButton:
                text: "Delete User"
                opposite_colors: True
                halign: 'center'
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                on_release: root.delete_user()

            MDRaisedButton:
                text: "Log Out"
                opposite_colors: False
                size_hint: None, None
                halign: 'center'
                size: 4 * dp(48), dp(48)
                on_release: root.logout()

        GridLayout:
            rows: 1
            cols: 2
            #padding: 20
            #spacing: 20
            ListViewModal:
                spacing: 5
                padding: 30
                ListView:
                    id: users_list_view
                    adapter:
                        ListAdapter(data=[], cls= main.UserImagesButton)
            BoxLayout:
                id: detail_user


    MDRaisedButton:
        text: "Delete User"
        opposite_colors: True
        size_hint_x: 15
        on_release: root.delete_user()

    MDRaisedButton:
        text: "Log Out"
        opposite_colors: False
        size_hint_x: 15
        on_release: root.logout()

