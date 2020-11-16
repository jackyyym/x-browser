import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# Modes
# 0: Editor no console
# 1: Preview no console
# 2: Editor with console
# 3: Preview with console
mode = 0
global global_app

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

#Toggling settings and views
class Header(GridLayout):
	def __init__(self, **kwargs):
		super(Header, self).__init__(**kwargs)
		self.cols = 3
		#Space for a logo?
		self.add_widget(Label(text="", size_hint_x=None, height=100))
		self.add_widget(Button(text="Toggle Console"))

		#Define mode toggle button
		self.toggle_mode_btn = Button(text="Toggle Mode" )
		self.toggle_mode_btn.bind(on_press=self.toggle_mode)
		self.add_widget(self.toggle_mode_btn)
	def toggle_mode(self, instance):
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
		self.add_widget(Button(text="Safari"))
		self.add_widget(Button(text="Chrome"))
		self.add_widget(Button(text="Firefox"))
		self.add_widget(Button(text="Opra"))

#Editor View
class Editor(GridLayout):
	def __init__(self, **kwargs):
		super(Editor, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(TextInput())
		self.add_widget(Preview_One())

#Preview for editor view
class Preview_One(GridLayout):
	def __init__(self, **kwargs):
		super(Preview_One, self).__init__(**kwargs)
		self.rows = 2
		self.add_widget(Tabs(size_hint_y=None, height=50))
		self.add_widget(Label(text="Preview"))

#Preview View
class Preview(GridLayout):
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		self.rows = 2
		self.cols = 2
		self.add_widget(Label(text="Safari"))
		self.add_widget(Label(text="Chrome"))
		self.add_widget(Label(text="Firefox"))
		self.add_widget(Label(text="Opra"))

class MyApp(App):
	def build(self):
		self.screen_manager = ScreenManager()
		
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
