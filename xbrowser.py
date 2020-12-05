import kivy
import webview
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.splitter import Splitter
from kivy.config import Config
from kivy.uix.popup import Popup
from multiprocessing import Process

import os
from os.path import join, isdir

Config.set('graphics', 'resizable', True)

global global_app
global curr_file
global ep_id
curr_file = "AAAAAAAAAAAAA"

# This class manages both the Editor and Preview Pages
class WindowManager(ScreenManager):
	pass

# load file popup
class LoadDialog(GridLayout):
	def is_dir(self, directory, filename):
		return isdir(join(directory, filename))
	
	pass

# Home page, where user can open project or create new
class HomePage(Screen):
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		self._popup = Popup(title="Load file", content=LoadDialog(), size_hint=(0.9, 0.9))
		self._popup.open()


# Both views, each with a header
class EditorPage(Screen):
	def __init__(self, **kwargs):
		super(EditorPage, self).__init__(**kwargs)
		global ep_id
		ep_id = self.ids

	pass
class PreviewPage(Screen):
	pass

# Header which is visible in both pages
# TODO: have header be independant from window manager
class Header(GridLayout):
	def __init__(self, **kwargs):
		super(Header, self).__init__(**kwargs)

	def generateBrowser(self):
		# Check if current file is an .html file
		global curr_file
		if (curr_file[-5:] == ".html"):
			webview.create_window('Browser Preview', os.path.relpath(curr_file, "./"))
			webview.start(debug=True)
		else:
			print("Please Select an HTML File!")
	pass

class SplitterRight(Splitter):
	pass
class SplitterTop(Splitter):
	pass

class XBrowserApp(App):
	def build(self):

		# Define all the screens that can be navigated to
		self.screen_manager = ScreenManager()

		self.home_page = HomePage()
		screen = Screen(name="Home")
		screen.add_widget(self.home_page)
		self.screen_manager.add_widget(screen)

		self.editor_page = EditorPage()
		screen = Screen(name="Editor")
		screen.add_widget(self.editor_page)
		self.screen_manager.add_widget(screen)

		self.preview_page = PreviewPage()
		screen = Screen(name="Preview")
		screen.add_widget(self.preview_page)
		self.screen_manager.add_widget(screen)

		return self.screen_manager

	# Define app methods
	def toggleMode(instance):
		if global_app.screen_manager.current == "Editor":
			global_app.screen_manager.transition.direction = "left"
			global_app.screen_manager.current = "Preview"
		else:
			global_app.screen_manager.transition.direction = "right"
			global_app.screen_manager.current = "Editor"

	def chooseFile(instance, selection):
		try:
			if selection[0]: # returns true if selection exists, thus selection[0] is a file
				global ep_id
				with open (selection[0], 'r') as f:
					ep_id.editor.text = f.read()
				global curr_file
				curr_file = selection[0]
		except:
			print("Please select a text file.")
		
	
	def load(self, path, filename):
		print("Opened File: " + os.path.join(path, filename[0]))
		with open(os.path.join(path,)) as stream:
			global ep_id
			ep_id.editor.text = stream.read()
		ep_id.filechooser.path = "./"
		print ("Path: " + path)
		global_app.screen_manager.current = "Editor"

		self.home_page.dismiss_popup()

if __name__ == '__main__':
	global global_app
	global_app = XBrowserApp()
	global_app.run()