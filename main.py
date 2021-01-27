from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget

class MainMenu(Screen):
	pass

class InfoPage(Screen):
	pass

class SchoolboySimApp(MDApp):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainMenu(name='Menu'))
		sm.add_widget(InfoPage(name='Info'))

		return sm

if __name__ == "__main__":
	SchoolboySimApp().run()