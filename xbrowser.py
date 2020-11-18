import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import NumericProperty

Config.set('graphics', 'resizable', True) 

global global_app

# This class manages both the Editor and Preview Pages
class WindowManager(ScreenManager):
	pass

# Home page, where user can open project or create new
class HomePage(Screen):
	pass

# Both views, each with a header
class EditorPage(Screen):
	pass
class PreviewPage(Screen):
	pass

# Header which is visible in both pages
# TODO: have header be independant from window manager
class Header(GridLayout):
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
	# def toggleConsole(self):
		
	def toggleMode(instance):
		if global_app.screen_manager.current == "Editor":
			global_app.screen_manager.transition.direction = "left"
			global_app.screen_manager.current = "Preview"
		else:
			global_app.screen_manager.transition.direction = "right"
			global_app.screen_manager.current = "Editor"

if __name__ == '__main__':
	global global_app
	global_app = XBrowserApp()
	global_app.run()
