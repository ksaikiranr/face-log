# coding:utf-8
### Kivy imports ###
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, SwapTransition, Screen
### Kivy imports end ###

import os
import cv2
import face_recognition

##################### Common variables ###############################
blueColor = (255, 0, 0)
greenColor = (0, 255, 0)
redColor = (0, 0, 255)
known_face_encodings = []
known_face_names = []
imagesDir = './users/'
capture = None

#######################################################################
## 	        Collecting images of existing users and traning          ##
#######################################################################



############             Training end                       ############


#######################################################################
## 	        Authenticating user                                      ##
#######################################################################
class KivyCameraAuth(Image):
	pass

#######################################################################
## 	        Regestration of user                                     ##
#######################################################################
class KivyCameraReg(Image):
	pass
	

#######################################################################
##                    Regestration Screen                            ##
#######################################################################
class RegisterScreen(Screen):
	pass
	

############             Regestration class end            ############


#######################################################################
##                    Login known user screen                        ##
#######################################################################
class LoginScreen(Screen):
	pass
	

############             Login class end                   ############


#######################################################################
##                    Home Screen                                    ##
#######################################################################
class HomeScreen(BoxLayout):
	pass


############             Home class end                    ############


#######################################################################
##                    Root FaceLog app                               ##
#######################################################################
class FaceLogApp(App):
	
	def build(self):
		# Window.clearcolor = (0.176, 0.243, 0.314, 1.0)
		# loginWin = RegisterScreen()
		# loginWin.init_start()
		# return loginWin
		self.title = 'FaceLog'
		self.init()
		return self.screen_manager
	
	def init(self):
		global capture
		capture = cv2.VideoCapture(0)
		self.screen_manager = ScreenManager(transition=SwapTransition())
		self.loginscreen = LoginScreen(name='login')
		self.loginscreen.dostart(capture)
		self.screen_manager.add_widget(self.loginscreen)
		self.loginscreen.doexit()
		self.registerscreen = RegisterScreen(name='register')
		self.registerscreen.dostart(capture)
		self.screen_manager.add_widget(self.registerscreen)
		self.registerscreen.doexit()
		self.screen_manager.current = 'register'
	
	def on_stop(self):
		global capture
		if capture:
			capture.release()
			capture = None


############             root class end                   ############


# creating instance to run
FaceLogApp().run()