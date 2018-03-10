<FaceLogLab@Label>:
    font_size: '18sp'
    font_name: 'Lato-Regular.ttf'


<FaceLogIps@TextInput>:
    background_normal:'images/textinput.png'
    background_active:'images/textinput_active.png'
    background_disabled_normal:'images/textinput_disabled.png'
    background_disabled_active:'images/textinput_disabled.png'
    font_name: 'Lato-Regular.ttf'
    font_size: '18sp'
    cursor_color: 0.498, 0.549, 0.552,1.0
    foreground_color: 0.204, 0.286, 0.369, 1.0
    selection_color: 0.925, 0.941, 0.937, 0.5
    padding: '10dp', '10dp'
    halign:'justify'
    border: 10,10,10,10

<RegisterScreen>:
    first_name_text_input: first_name
    last_name_text_input: last_name
    BoxLayout:
        orientation: "vertical"
        canvas:
            Color:
                rgba: 0.176, 0.243, 0.314, 1.0
            Rectangle:
                pos: self.pos
                size: self.size
        padding: 10
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "60dp"
            Label:
                text: "User Registeration"
                font_name: 'Lato-Bold.ttf'
                font_size: '25sp'
        BoxLayout:
            size_hint_y: None
            height: "48dp"
            FaceLogLab:
                text: "First Name"
            FaceLogIps:
                id: first_name
            FaceLogLab:
                text: "Last Name"
            FaceLogIps:
                id: last_name

        BoxLayout:
            size_hint_y: None
            height: "30dp"
            FaceLogLab:
                text: "Please align your face with camera for sample image."
        BoxLayout:
            KivyCameraReg:
                id: qrcamReg

        BoxLayout:
            size_hint_y: None
            height: "40dp"
            spacing: 25
            Button:
                text: "Capture Image"
                size_hint_x: 15
                on_press: root.captureUser()
            Button:
                text: "Verify and Submit"
                size_hint_x: 15
                on_press:
                    root.doexit()
                    root.manager.current = 'login'



<LoginScreen>:

    BoxLayout:
        orientation: "vertical"

        padding: 10
        spacing: 10

        BoxLayout:
            size_hint_y: None
            height: "60dp"
            Label:
                text: "User Login"

        BoxLayout:
            size_hint_y: None
            height: "30dp"
            FaceLogLab:
                text: "Please align your face with camera for authentication."
        BoxLayout:
            KivyCameraAuth:
                id: qrcamAuth

        BoxLayout:
            size_hint_y: None
            height: "40dp"
            spacing: 25
            Button:
                text: "bhla"
                size_hint_x: 15
                on_press: root.captureUser()
            Button:
                text: "Register"
                size_hint_x: 15
                on_press:
                    root.doexit()
                    root.manager.current = 'register'

