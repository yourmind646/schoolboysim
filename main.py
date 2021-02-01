# Файл разметки виджетов: schoolboysim.kv

from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition
import kivymd.uix.bottomnavigation
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

import json
import os
from kivymd.utils import asynckivy

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

    # Сохранение при закрытии игры (через кнопку)
    def close_game(self):
        with open("data/save/session.sv", "w") as write_file:
            json.dump(data1, write_file)
        exit()

    def earn_action(self, action_id):
        import time

        if action_id == "1":
            self.pb1.opacity = 1
            self.btn1.opacity = 0
            self.btn1.disabled = True
            async def progress():
                while not self.pb1.value == 100:
                    await asynckivy.sleep(0.05)
                    self.pb1.value += 1

                data1["Money"] = str(int(data1.get("Money")) + 100)
                self.mon.text = data1.get("Money") + " ₽"

                data1["Exp"] = str(int(data1.get("Exp")) + 10)
                self.exp.text = data1.get("Exp") + " exp"

                self.btn1.opacity = 1
                self.btn1.disabled = False

                self.pb1.opacity = 0
                self.pb1.value = 0

            asynckivy.start(progress())





# Окно главного меню
class MainMenu(Screen):
    # Сохранение при закрытии игры (через кнопку)
    def close_game(self):
        with open("data/save/session.sv", "w") as write_file:
            json.dump(data1, write_file)
        exit()

# Окно информации
class InfoPage(Screen):
    def browser_open(self, link):
        webbrowser.open(link)


class SchoolboySimApp(MDApp):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)

        sm = ScreenManager(transition = FallOutTransition())
        sm.add_widget(MainMenu(name='Menu'))
        sm.add_widget(InfoPage(name='Info'))
        sm.add_widget(Game(name="Game"))

        return sm

    # Сохранение при закрытии игры (через вкладки)
    def on_request_close(self, *args):
        with open("data/save/session.sv", "w") as write_file:
            json.dump(data1, write_file)

SchoolboySimApp().run()