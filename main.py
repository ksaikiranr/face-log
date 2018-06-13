# coding:utf-8
### Kivy imports ###
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, SwapTransition, Screen
from kivy.base import EventLoop
### Kivy imports end ###
import kivy
kivy.require("1.10.0")

import os
import cv2
import face_recognition

from kivymd import  *

## UI imports ##
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker

from kivymd.grid import SmartTile
from kivymd.list import TwoLineAvatarIconListItem
from kivy.modules import inspector
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.list import MDList
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.metrics import dp

##################### Common variables ###############################
blueColor = (255, 0, 0)
greenColor = (0, 255, 0)
redColor = (0, 0, 255)
known_face_encodings = []
known_face_names = []
imagesDir = './users/'
global scrmgr

auth_user_name = ""

capture = cv2.VideoCapture(0)
#######################################################################
## 	        Collecting images of existing users and traning          ##
#######################################################################

imageNames = os.listdir(imagesDir)
# print("Found these images in users folder " + str(imageNames))
for name in imageNames:
	# print(face_recognition.face_encodings(face_recognition.load_image_file(imagesDir+name)))
	known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(imagesDir + name))[0])
	known_face_names.append(name.split('.')[0])


############             Training end                       ############

class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
	pass


class AvatarSampleWidget(ILeftBody, Image):
	pass


#######################################################################
## 	        Authenticating user                                      ##
#######################################################################

class LoginScreen(Screen):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.register_event_type('on_login')
	
	def dostart(self):
		try:
			self.ids.login_cam.clear_widgets()
			self.ids.home_container.came.remove_widget(self.ids.cc)
		except:
			pass
		bx = BoxLayout(orientation="vertical", spacing="10", padding="10", id="bxla")
		self.camauth = CameraAuth(id="cme")
		self.camauth.bind(on_login_return=self.disp_home)
		self.camauth.size = 0.8 * self.width, 0.6 * self.height
		bx.add_widget(self.camauth)
		self.ids.login_cam.add_widget(bx)
	
	def dostop(self):
		# self.remove_widget(self.ids.login_cam)
		print(self.ids.login_cam.children)
		self.camauth.stop()
	
	def disp_home(self, *args):
		print("disp @ loginScrn clasx	")
		print("my args are" + str(args))
		self.dispatch("on_login")
		pass
	
	def on_login(self):
		pass


class CameraAuth(Image):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.register_event_type('on_login_return')
		self.capture = None
		global capture
		self.start(capture)
	
	def on_login_return(self):
		pass
	
	def start(self, capture, fps=30):
		self.capture = capture
		rect, frame = self.capture.read()
		rect, frame = self.capture.read()
		self.update_schedule = Clock.schedule_interval(self.update, 1.0 / fps)
		print("start over auth")
	
	def stop(self):
		Clock.unschedule(self.update)
		print("releasing capture --------------------------")
		print(self.capture)
		self.update_schedule.cancel()
		print(self.capture)
		print("capture released ----------------------")
		print(self.capture)
	
	def update(self, dt):
		# print("From auth update")
		# Get frame
		print("in auth update")
		if self.capture == None:
			print("no cap found auth ")
			return
		ret, frame = self.capture.read()
		try:
			small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		except:
			print("Failed to get cv resize")
			self.stop()
			return
		# Convert the image from BGR color to RGB color
		rgb_small_frame = small_frame[:, :, ::-1]
		
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
		# print("Found face @ these locations: ", face_locations)
		face_names = []
		# print(known_face_names)
		# print(known_face_encodings)
		name = ''
		for face_encoding in face_encodings:
			# See if the face is a match for the known face(s)
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
			name = "Unknown"
			
			# If a match was found in known_face_encodings, just use the first one.
			if True in matches:
				first_match_index = matches.index(True)
				name = known_face_names[first_match_index]
			# set color for border in result display
			if name == "Unknown":
				drawColor = redColor
			else:
				drawColor = greenColor
			face_names.append(name)
		
		# Display the results
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			# Scale back up face locations since the frame we detected in was scaled to 1/4 size
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4
			
			# Draw a box around the face
			cv2.rectangle(frame, (left - 100, top - 100), (right + 100, bottom + 100), drawColor, 2)
			
			# Draw a label with a name below the face
			cv2.rectangle(frame, (left - 100, bottom + 100), (right - 100, bottom + 100), drawColor, cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.rectangle(frame, (left - 100, bottom + 100), (right + 100, bottom + 150), drawColor, cv2.FILLED)
			cv2.putText(frame, name, (left + 95, bottom + 130), font, 1.0, (255, 255, 255), 1)
		
		if name in known_face_names:
			print("usrr found@")
			global auth_user_name
			auth_user_name = name
			print("sending dispatch to on_login_return")
			self.dispatch('on_login_return')
			print("sent dispatch to on_login_return")
			self.stop()
			self.update_schedule.cancel()
		# display frame
		frame = cv2.flip(frame, 0)
		buf = frame.tostring()
		image_texture = Texture.create(
			size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
		image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
		# display image from the texture
		self.texture = image_texture


#############################################################################
class UserImagesButton(ListItemButton):
	pass


class ListViewModal(ModalView):
	def __init__(self, **kwargs):
		super(ListViewModal, self).__init__(**kwargs)


class UserImageDetailView(BoxLayout):
	user_name = StringProperty('', allownone=True)
	
	def __init__(self, **kwargs):
		kwargs['orientation'] = 'vertical'
		self.user_name = kwargs.get('user_name', '')
		super(UserImageDetailView, self).__init__(**kwargs)
		if self.user_name:
			self.redraw()
	
	def redraw(self, *args):
		print("########################################")
		print(self.ids)
		self.clear_widgets()
		
		print(self.user_name)
		a = []
		if not type(self.user_name) == type(a):
			print("user name is " + self.user_name)
			self.add_widget(Image(
				source=imagesDir + self.user_name,
				size=(450, 450)))
			
			## TODO display file attribs ##
			if self.user_name == "[]":
				return
			user_attributes = os.stat(imagesDir + self.user_name)
			fileProtectionMode = str(user_attributes.st_mode)
			fileInode = str(user_attributes.st_ino)
			fileSize = str(float(user_attributes.st_size) / 1000) + " KB"
			#fileLastEdited = str(user_attributes.st_mtime)
			#fileLastAccessed = str(user_attributes.st_atime)
			# print(type(os.stat(imagesDir + self.user_name)))
			attrib_grid = GridLayout(rows=6, cols=2, padding=25, spacing=25)
			attrib_grid.add_widget(Label(text='User Name', color=[1, 1, 1, 0.8], halign="left"))
			attrib_grid.add_widget(Label(text=self.user_name.strip('.'), color=[1, 1, 1, 0.8], halign="left"))
			attrib_grid.add_widget(Label(text='File Size', color=[1, 1, 1, 0.8], halign="left"))
			attrib_grid.add_widget(Label(text=fileSize, color=[1, 1, 1, 0.8], halign="left"))
			#attrib_grid.add_widget(Label(text='last Accessed timestamp', color=[1, 1, 1, 0.8], halign="left"))
			#attrib_grid.add_widget(Label(text=fileLastAccessed, color=[1, 1, 1, 0.8], halign="left"))
			#attrib_grid.add_widget(Label(text='last Edited timestamp', color=[1, 1, 1, 0.8]))
			#attrib_grid.add_widget(Label(text=fileLastEdited, color=[1, 1, 1, 0.8]))
			# attrib_grid.add_widget(Label(text='File Protection Mode', color=[1, 1, 1, 0.8]))
			# attrib_grid.add_widget(Label(text=fileProtectionMode, color=[1, 1, 1, 0.8]))
			
			self.add_widget(attrib_grid)
	
	def user_changed(self, list_adapter, *args):
		if len(list_adapter.selection) == 0:
			self.user_name = None
			return
		else:
			selected_object = list_adapter.selection[0]
			if hasattr(selected_object, 'user_name'):
				self.user_name = selected_object.user_name
			else:
				self.user_name = selected_object.text
		
		self.redraw()
	
	def clearwids(self):
		self.clear_widgets()


class HomeScreen(Screen):
	users_list = ObjectProperty()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.register_event_type('on_logout')
		self.register_event_type('on_newuser')
		self.setUserDirInfo()
		global auth_user_name
		print("auth user name is ++++" + auth_user_name)
		self.user_name_auth = auth_user_name
	
	def setUserDirInfo(self):
		# print(self.ids)
		self.userImages = os.listdir(imagesDir)
		
		for user in self.userImages:
			self.users_list.adapter.data.extend([user])
		
		if not self.users_list.adapter.selection:
			self.detail_view = UserImageDetailView(
				user_name=str(self.userImages[0]),
				size_hint=(.6, 1.0))
		else:
			self.detail_view = UserImageDetailView(
				user_name=str(self.users_list.adapter.selection),
				size_hint=(.6, 1.0))
		
		self.users_list.adapter.bind(
			on_selection_change=self.detail_view.user_changed)
		self.ids.detail_user.add_widget(self.detail_view)
	
	# print("Ids are -------------------\n" + str(self.ids))
	
	def delete_user(self):
		# print(self)
		# print(self.users_list.adapter.selection[0])
		# print(type(self.users_list.adapter.selection[0]))
		# print(self.users_list.adapter.selection[0].text)
		self.user_delete = self.users_list.adapter.selection[0].text
		self.user_name_delete = self.user_delete.split('.')[0]
		self.content = content = MDLabel(font_style='Subhead',
										 theme_text_color='Secondary',
										 text="All data associated with " + self.user_name_delete + " has been removed successfully!",
										 size_hint_y=None,
										 valign='top')
		self.dialog = MDDialog(title="Conform user delete operation",
							   content=self.content,
							   size_hint=(.8, None),
							   height=dp(200),
							   auto_dismiss=False)
		
		self.dialog.add_action_button("Dismiss", action=lambda *x: self.dialog.dismiss())
		self.dialog.open()
		print("########################")
		print(self.ids)
		self.detail_view.clearwids()
		self.ids.detail_user.clear_widgets()
		os.remove(imagesDir + self.user_delete)
		# print("delete called")
		self.users_list.adapter.data = []
		self.setUserDirInfo()
		self.detail_view.redraw()
	
	def edit_user(self):
		# print(self)
		# rint(self.users_list.adapter.selection[0].split('=')[1])
		print("edit user called")
	
	def on_newuser(self):
		pass
	
	def on_logout(self, **kwargs):
		# print(kwargs)
		pass


class UserImages(MDList):
	user_list = ObjectProperty()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print("called user image class")
		# print(self.ids)
		print(scrmgr)
		root = scrmgr
		# print(dir(root))
		# self.cols = 3
		# self.row_default_height = (root.width - self.cols * self.spacing[0]) / self.cols
		
		self.userImages = os.listdir(imagesDir)
		# heading = MDLabel()
		# heading.font_name = 'Lato-Regular.ttf'
		# heading.text = "Home Screen."
		# heading.halign = 'center'
		# heading.font_size ="20dp"
		# heading.size = 800 , 25
		# self.add_widget(heading)
		# intro = MDLabel()
		# intro.font_name = 'Lato-Regular.ttf'
		# intro.text = "Here is the list of known users. Please note all actions performed here can not be reversed."
		# intro.font_size = "18dp"
		# self.add_widget(intro)
		
		# print("found images ", self.userImages )
		
		for user in self.userImages:
			# print(face_recognition.face_encodings(face_recognition.load_image_file(imagesDir+name)))
			# print("adding " + user)
			rightIcon = IconRightSampleWidget()
			avatar = AvatarSampleWidget(source=imagesDir + user)
			# print(os.stat(imagesDir + user))
			tempwid = TwoLineAvatarIconListItem(text=user, secondary_text="...with avatar&icon")
			tempwid.id = user
			tempwid.add_widget(avatar)
			tempwid.add_widget(rightIcon)
			tempwid.on_release = self.editUser
			self.add_widget(tempwid)
	
	# self.add_widget(SmartTile(mipmap=True, source=imagesDir + user))
	# pass
	
	def on_login(self):
		print("disp @ loginScrn clasx	")
		pass
	
	def editUser(self):
		# print("clicked!" + str(self))
		# print(self.ids)
		bs = MDListBottomSheet()
		bs.add_item("Change user details of ", lambda x: x)
		bs.add_item("Here's an item with an icon", lambda x: x,
					icon='clipboard-account')
		bs.add_item("Here's another!", lambda x: x, icon='nfc')
		bs.open()


#######################################################################
## 	        Regestration of user                                     ##
#######################################################################
class KivyCameraReg(Image):
	
	def __init__(self, **kwargs):
		super(KivyCameraReg, self).__init__(**kwargs)
		self.capture = None
	
	# self.start(capture)
	
	def start(self, capture, fps=30):
		self.capture = capture
		Clock.schedule_interval(self.update, 1.0 / fps)
	
	# print("start over reg")
	
	def stop(self):
		Clock.unschedule(self.update)
		self.capture = None
	
	def update(self, dt):
		# Get frame
		print("From reg update")
		ret, frame = self.capture.read()
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		# Convert the image from BGR color to RGB color
		rgb_small_frame = small_frame[:, :, ::-1]
		
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small_frame)
		# print("Found face @ these locations: ", face_locations)
		
		# Display the results
		drawColor = blueColor
		name = "New User"
		for (top, right, bottom, left) in face_locations:
			# Scale back up face locations since the frame we detected in was scaled to 1/4 size
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4
			
			# Draw a box around the face
			cv2.rectangle(frame, (left - 100, top - 100), (right + 100, bottom + 100), drawColor, 2)
			
			# Draw a label with a name below the face
			cv2.rectangle(frame, (left - 100, bottom + 100), (right - 100, bottom + 100), drawColor, cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.rectangle(frame, (left - 100, bottom + 100), (right + 100, bottom + 150), drawColor, cv2.FILLED)
			cv2.putText(frame, name, (left + 95, bottom + 130), font, 1.0, (255, 255, 255), 1)
		
		# display frame
		frame = cv2.flip(frame, 0)
		buf = frame.tostring()
		image_texture = Texture.create(
			size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
		image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
		# display image from the texture
		self.texture = image_texture


#######################################################################
##                    Regestration Screen                            ##
#######################################################################
class RegisterScreen(Screen):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print("############REG#####REG##########")
		self.capture = capture
	
	# self.dostart(self.capture)
	
	def __enter__(self):
		print("reg start req")
	
	# self.dostart()
	
	def dostart(self, capture, *largs):
		self.capture = capture
		self.ids.qrcamReg.start(capture)
	
	def doexit(self):
		self.remove_widget(self.ids.qrcamReg)
		self.ids.qrcamReg.stop()
		pass
	
	def capture_user(self):
		'''
		Function to capture the images and give them the names
		according to their captured time and date.
		'''
		camera = self.ids['qrcamReg']
		username = self.first_name_text_input.text + " " + self.last_name_text_input.text
		rect, frame = self.capture.read()
		cv2.imwrite(imagesDir + username + ".png", frame)
		print("Captured")
	
	def find_face(self, file_name):
		frame = cv2.imread("./users/" + file_name + ".png")
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		# Convert the image from BGR color to RGB color
		rgb_small_frame = small_frame[:, :, ::-1]
		
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small_frame)
		# print("Found face @ these locations: ", face_locations)
		if face_locations:
			return True
		return False


#######################################################################
##                    Root FaceLog app                               ##
#######################################################################
class FaceLogApp(App):
	theme_cls = ThemeManager()
	title = "Face Log"
	
	menu_items = [
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
		{'viewclass': 'MDMenuItem',
		 'text': 'Example item'},
	]
	
	def build(self):
		self.init()
		return self.screenmanager
	
	def init(self):
		self.screenmanager = ScreenManager(transition=SwapTransition())
		global scrmgr
		scrmgr = self.screenmanager
		# print("from build " + str(scrmgr))
		self.loginscreen = LoginScreen(name='screen-login')
		self.loginscreen.bind(on_login=self.login)
		self.homescreen = HomeScreen(name='screen-home')
		self.homescreen.user_name_auth = 'ex'
		self.homescreen.bind(on_newuser=self.newuser_redirect)
		self.homescreen.bind(on_logout=self.logout_redirect)
		self.screenmanager.add_widget(self.loginscreen)
		self.screenmanager.add_widget(self.homescreen)
		self.registerscreen = RegisterScreen(name='screen-register')
		self.screenmanager.add_widget(self.registerscreen)
		scrmgr = self.screenmanager
		# self.screenmanager.current = 'screen-home'
		print(scrmgr)
		inspector.create_inspector(Window, Button)

	def newuser_redirect(self, *args):
		print("new user redirect from main")
		self.screenmanager.current = 'screen-register'
	
	def logout_redirect(self, *args):
		print("called from main redirect to login")
		print("Logged in waiting for re-direction---")
		print("recired args " + str(args))
		print(self.screenmanager)
		self.screenmanager.current = 'screen-login'
		print(self.screenmanager.current)
	
	def login(self, *args):
		print("Logged in waiting for re-direction---")
		print("recired args " + str(args))
		self.screenmanager.current = 'screen-home'
		print("auth user name is ++++" + auth_user_name)
		self.loginSuccessDialog()
	
	def loginSuccessDialog(self):
		global auth_user_name
		content = MDLabel(font_style='Body1',
						  theme_text_color='Secondary',
						  text="Welcome " + auth_user_name + "\n This is the home-screen, if you are not aware of the options given here"
															 "\nPlease refer documentation!",
						  size_hint_y=None,
						  valign='top')
		content.bind(texture_size=content.setter('size'))
		self.dialog = MDDialog(title="Login Success!",
							   content=content,
							   size_hint=(.8, None),
							   height=dp(200),
							   auto_dismiss=False)
		
		self.dialog.add_action_button("Dismiss",
									  action=lambda *x: self.dialog.dismiss())
		self.dialog.open()


############             root class end                   ############


if __name__ == '__main__':
	# creating instance to run
	FaceLogApp().run()