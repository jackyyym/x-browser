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

Config.set('graphics', 'resizable', True) 

# Modes
# 0: Editor no console
# 1: Preview no console
# 2: Editor with console
# 3: Preview with console
mode = 0
global global_app

browsers = ["Safari", "Chrome", "Firefox", "Opera"]
current_browser = 0

#This view is always on
class EditorPage(GridLayout):
	def __init__(self, **kwargs):
		super(EditorPage, self).__init__(**kwargs)
		self.cols = 0
		self.rows = 2
		self.add_widget(Header(size_hint_y=None, height=50))
		self.add_widget(Editor())

class PreviewPage(GridLayout):
	def __init__(self, **kwargs):
		super(PreviewPage, self).__init__(**kwargs)
		self.cols = 0
		self.rows = 2
		self.add_widget(Header(size_hint_y=None, height=50))
		self.add_widget(Preview())

class HomePage(GridLayout):
	def __init__(self, **kwargs):
		super(HomePage, self).__init__(**kwargs)
		self.cols = 0
		self.rows = 2
		self.add_widget(Label(text="LOGO", size_hint_x=.1, height=100))
		self.add_widget(Home(size_hint_y =None, height=500))

#Toggling settings and views
class Header(GridLayout):
	def __init__(self, **kwargs):
		super(Header, self).__init__(**kwargs)
		self.cols = 3
		#Space for a logo?
		self.add_widget(Label(text="LOGO", size_hint_x=.25, height=100))
		
		self.add_widget(Button(text="Toggle Console", on_press=self.toggleConsole))
		self.add_widget(Button(text="Toggle Mode", on_press=self.toggleMode))
	def toggleConsole(instance, value):
		global mode
		mode ^= 2
	def toggleMode(instance, value):
		global mode
		mode ^= 1
		if global_app.screen_manager.current == "Editor":
			global_app.screen_manager.transition.direction = "left"
			global_app.screen_manager.current = "Preview"
		else:
			global_app.screen_manager.transition.direction = "right"
			global_app.screen_manager.current = "Editor"

#When console mode is active, have this be the body
class Body_Console(GridLayout):
	def __init__(self, **kwargs):
		super(Body_Console, self).__init__(**kwargs)
		self.rows = 2
		if mode == 2:
			self.add_widget(Editor())
		else:
			self.add_widget(Preview())
		self.add_widget(Console(size_hint_y=None, height=200))

#The view for console
class Console(GridLayout):
	def __init__(self, **kwargs):
		super(Console, self).__init__(**kwargs)
		self.rows = 2
		self.add_widget(Tabs(size_hint_y=None, height=50))
		self.add_widget(Label(text="Console"))

#The view for browser tabs (used for console and preview in Edit mode)
class Tabs(GridLayout):
	def __init__(self, **kwargs):
		super(Tabs, self).__init__(**kwargs)
		self.cols = 4
		self.add_widget(Button(text="1-Safari", on_press=self.onChange))
		self.add_widget(Button(text="2-Chrome", on_press=self.onChange))
		self.add_widget(Button(text="3-Firefox", on_press=self.onChange))
		self.add_widget(Button(text="4-Opera", on_press=self.onChange))
	def onChange(instance, value):
		global current_browser
		current_browser = int(value.text[0])-1

#Launch/Home View
class Home(GridLayout):
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Button(text="Open New File", font_size = "30sp", on_press=self.onChange))
		self.add_widget(Button(text="Upload a File", font_size = "30sp", on_press=self.errorMsg))
	def onChange(instance, value):
		global mode
		mode ^= 1 
		global_app.screen_manager.current = "Editor"
	def errorMsg(self, event):
		print("This mode is not currently available")
#Editor View
class Editor(GridLayout):
	def __init__(self, **kwargs):
		super(Editor, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(TextInput())
		self.add_widget(Preview_One())

#Preview for editor view
class Preview_One(TabbedPanel):
	pass

#Preview View
class Preview(GridLayout):
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		self.rows = 2
		self.cols = 2
		self.add_widget(Image(source="screenshots/Safari.png", keep_ratio=False, allow_stretch=True))
		self.add_widget(Image(source="screenshots/Chrome.png", keep_ratio=False, allow_stretch=True))
		self.add_widget(Image(source="screenshots/Firefox.png", keep_ratio=False, allow_stretch=True))
		self.add_widget(Image(source="screenshots/Opera.png", keep_ratio=False, allow_stretch=True))

class MyApp(App):
	def build(self):
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

if __name__ == '__main__':
	global global_app 
	global_app = MyApp()
	global_app.run()
