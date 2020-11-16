import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Modes
# 0: Editor no console
# 1: Preview no console
# 2: Editor with console
# 3: Preview with console
mode = 3

browsers = ["Safari", "Chrome", "Firefox", "Opera"]
current_browser = 0

#This view is always on
class Basic(GridLayout):
	def __init__(self, **kwargs):
		super(Basic, self).__init__(**kwargs)
		self.cols = 0
		self.rows = 2
		self.add_widget(Header(size_hint_y=None, height=50))
		if (mode == 2 or mode == 3):
			self.add_widget(Body_Console())
		elif mode == 1:
			self.add_widget(Preview())
		else:
			self.add_widget(Editor())

#Toggling settings and views
class Header(GridLayout):
	def __init__(self, **kwargs):
		super(Header, self).__init__(**kwargs)
		self.cols = 3
		#Space for a logo?
		self.add_widget(Label(text="", size_hint_x=None, height=100))
		self.add_widget(Button(text="Toggle Console", on_press=self.toggleConsole))
 		self.add_widget(Button(text="Toggle Mode", on_press=self.toggleMode))
 	def toggleMode(instance, value):
		global mode
 		mode ^= 1
 	def toggleConsole(instance, value):
		global mode
 		mode ^= 2

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
		self.add_widget(Button(text="1-Safari", value=0, on_press=self.onChange))
		self.add_widget(Button(text="2-Chrome", value=1, on_press=self.onChange))
		self.add_widget(Button(text="3-Firefox", value=2, on_press=self.onChange))
		self.add_widget(Button(text="4-Opera", value=3, on_press=self.onChange))
	def onChange(instance, value):
		global current_browser
		current_browser = int(value.text[0])-1

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
		self.add_widget(Image(source="screenshots/" + browsers[current_browser] +".png", keep_ratio=False, allow_stretch=True))

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
		return Basic()

if __name__ == '__main__':
	MyApp().run()
