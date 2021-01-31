# Файл разметки виджетов: schoolboysim.kv

from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import kivymd.uix.bottomnavigation
from kivy.core.window import Window

import json
import os

import webbrowser
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import Widget

# Создание начального сейва с стартовыми значениями
if not os.path.exists("data/save/session.sv"):
    with open("data/save/session.sv", "w") as write_file:
        json.dump({"Level": "1", "Exp": "0", "Money": "0", "Target": "Отменить д/з"},
                  write_file)
# Загрузка сейва
with open("data/save/session.sv", "r") as read_file:
    data1 = json.load(read_file)

# Окно игрового процесса
class Game(Screen):
    global data1
    data = data1

# Окно главного меню
class MainMenu(Screen):
    pass

# Окно информации
class InfoPage(Screen):
    def browser_open(self, link):
        webbrowser.open(link)


class SchoolboySimApp(MDApp):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)

        sm = ScreenManager()
        sm.add_widget(MainMenu(name='Menu'))
        sm.add_widget(InfoPage(name='Info'))
        sm.add_widget(Game(name="Game"))

        return sm

    # Сохранение при закрытии игры
    def on_request_close(self, *args):
        with open("data/save/session.sv", "w") as write_file:
            json.dump(data1, write_file)

SchoolboySimApp().run()