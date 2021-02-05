from kivymd.app import MDApp

# Layouts
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

import kivymd.uix.bottomnavigation, json, os, webbrowser

from kivy.core.window import Window
from kivymd.utils import asynckivy
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivymd.toast import toast

# Создание начального сейва с стартовыми значениями
if not os.path.exists("data/save/session.sv"):
	with open("data/save/session.sv", "w") as write_file:
		json.dump({"Level": "1",
		"Exp": "0",
		"Money": "0",
		"Target": "Отменить д/з",
		"earn_action_1": "opened",
		"earn_action_2": "locked",
		"earn_action_3": "locked",
		"earn_action_4": "locked",
		"earn_action_5": "locked",
		"target_1": "opened",
		"target_2": "locked",
		"target_3": "locked",
		"target_4": "locked",
		"target_5": "locked"},
				  write_file)

# Загрузка сейва
with open("data/save/session.sv", "r") as read_file:
	data = json.load(read_file)

class Game(BoxLayout):
	global data
	temp_data = data

	def browser_open(self, link):
		webbrowser.open(link)

	# Сохранение при закрытии игры (через кнопку)
	def close_game(self):
		with open("data/save/session.sv", "w") as write_file:
			json.dump(data, write_file)
		exit()

	def close_actions(self, current_action, current_pb):
		if not current_action == self.btn1:
			self.btn1.icon = "lock"
			self.btn1.disabled = True

		if not current_action == self.btn2:
			self.btn2.icon = "lock"
			self.btn2.disabled = True

		if not current_action == self.btn3:
			self.btn3.icon = "lock"
			self.btn3.disabled = True

		if not current_action == self.btn4:
			self.btn4.icon = "lock"
			self.btn4.disabled = True

		if not current_action == self.btn5:
			self.btn5.icon = "lock"
			self.btn5.disabled = True

		current_action.opacity = 0
		current_action.disabled = True
		current_pb.opacity = 1


	def enable_actions(self, current_button, current_pb):
		self.btn1.disabled = False
		self.btn2.disabled = False
		self.btn3.disabled = False
		self.btn4.disabled = False
		self.btn5.disabled = False

		self.btn1.icon = "arrow-right-drop-circle-outline" if data.get("earn_action_1") == "opened" else "lock"
		self.btn2.icon = "arrow-right-drop-circle-outline" if data.get("earn_action_2") == "opened" else "lock"
		self.btn3.icon = "arrow-right-drop-circle-outline" if data.get("earn_action_3") == "opened" else "lock"
		self.btn4.icon = "arrow-right-drop-circle-outline" if data.get("earn_action_4") == "opened" else "lock"
		self.btn5.icon = "arrow-right-drop-circle-outline" if data.get("earn_action_5") == "opened" else "lock"


		current_button.opacity = 1
		current_pb.opacity = 0


	def update_level(self):
		if int(data.get("Exp")) >= 50 and int(data.get("Exp")) <= 224:
			if not data.get("Level") == "2": 
				data["Level"] = "2"
				data["earn_action_2"] = "opened"
				self.btn2.icon = "arrow-right-drop-circle-outline"
				self.btn2.text_color = .35, .66, .41, 1
				self.lvl.text = data.get("Level")

				data["target_2"] = "opened"
				self.t_btn2.icon = "cart-arrow-down"
				self.t_btn2.text_color = [.13, .59, .95, 1]

				toast("Уровень повышен!")


		if int(data.get("Exp")) >= 225 and int(data.get("Exp")) <= 674:
			if not data.get("Level") == "3": 
				data["Level"] = "3"
				data["earn_action_3"] = "opened"
				self.btn3.icon = "arrow-right-drop-circle-outline"
				self.btn3.text_color = .35, .66, .41, 1
				self.lvl.text = data.get("Level")

				data["target_3"] = "opened"
				self.t_btn3.icon = "cart-arrow-down"
				self.t_btn3.text_color = [.13, .59, .95, 1]

				toast("Уровень повышен!")

		if int(data.get("Exp")) >= 675 and int(data.get("Exp")) <= 1774:
			if not data.get("Level") == "4": 
				data["Level"] = "4"
				data["earn_action_4"] = "opened"
				self.btn4.icon = "arrow-right-drop-circle-outline"
				self.btn4.text_color = .35, .66, .41, 1
				self.lvl.text = data.get("Level")

				data["target_4"] = "opened"
				self.t_btn4.icon = "cart-arrow-down"
				self.t_btn4.text_color = [.13, .59, .95, 1]

				toast("Уровень повышен!")

		if int(data.get("Exp")) >= 1775:
			if not data.get("Level") == "5": 
				data["Level"] = "5"
				data["earn_action_5"] = "opened"
				self.btn5.icon = "arrow-right-drop-circle-outline"
				self.btn5.text_color = .35, .66, .41, 1
				self.lvl.text = data.get("Level")

				data["target_5"] = "opened"
				self.t_btn5.icon = "cart-arrow-down"
				self.t_btn5.text_color = [.13, .59, .95, 1]

				toast("Уровень повышен!")

	async def progress(self, current_button, current_pb):
				while not current_pb.value == 100:
					await asynckivy.sleep(0.05)
					current_pb.value += 1

				profit_money = None
				profit_exp = None

				if current_button == self.btn1:
					profit_money = 100
					profit_exp = 10
				elif current_button == self.btn2:
					profit_money = 500
					profit_exp = 25
				elif current_button == self.btn3:
					profit_money = 1000
					profit_exp = 50
				elif current_button == self.btn4:
					profit_money = 5000
					profit_exp = 100
				elif current_button == self.btn5:
					profit_money = 10000
					profit_exp = 150

				data["Money"] = str(int(data.get("Money")) + profit_money)
				self.mon.text = data.get("Money") + " руб"

				data["Exp"] = str(int(data.get("Exp")) + profit_exp)
				self.exp.text = data.get("Exp") + " exp"

				current_pb.value = 0

				self.update_level()

				self.enable_actions(current_button, current_pb)

	def earn_action(self, earn_action_id):
		if data[earn_action_id] == "locked":
			return

		current_button = None
		current_pb = None

		if earn_action_id == "earn_action_1":
			current_button = self.btn1
			current_pb = self.pb1
		elif earn_action_id == "earn_action_2":
			current_button = self.btn2
			current_pb = self.pb2
		elif earn_action_id == "earn_action_3":
			current_button = self.btn3
			current_pb = self.pb3
		elif earn_action_id == "earn_action_4":
			current_button = self.btn4
			current_pb = self.pb4
		elif earn_action_id == "earn_action_5":
			current_button = self.btn5
			current_pb = self.pb5

		self.close_actions(current_button, current_pb)

		asynckivy.start(self.progress(current_button, current_pb))

	def buy_target(self, current_target):
		if current_target == "target_1":
			current_button = self.t_btn1
		elif current_target == "target_2":
			current_button = self.t_btn2
		elif current_target == "target_3":
			current_button = self.t_btn3
		elif current_target == "target_4":
			current_button = self.t_btn4
		elif current_target == "target_5":
			current_button = self.t_btn5

		if data.get(current_target) == "locked":
			toast("Цель закрыта!")
		elif data.get(current_target) == "opened":
			if current_button == self.t_btn1:
				if not int(data.get("Money")) >=  600:
					toast("Нехватает денег: " + str(600 - int(data.get("Money"))))
				else:
					data["Money"] = str(int(data.get("Money")) - 600)
					self.mon.text = str(data.get("Money") + " руб")

					data["Target"] = "Отменить c/р"
					self.target.text = "Отменить c/р"

					data["target_1"] = "bought"
					self.t_btn1.icon = "check-circle-outline"
					self.t_btn1.text_color = [.35, .66 ,.41, 1]

					toast("Цель выполнена!")

			if current_button == self.t_btn2:
				if not int(data.get("Money")) >=  4000:
					toast("Нехватает денег: " + str(4000 - int(data.get("Money"))))
				elif data["target_1"] == "opened":
					toast("Необходимо сначала отменить д/з")
				else:
					data["Money"] = str(int(data.get("Money")) - 4000)
					self.mon.text = str(data.get("Money") + " руб")

					data["Target"] = "Отменить к/р"
					self.target.text = "Отменить к/р"

					data["target_2"] = "bought"
					self.t_btn2.icon = "check-circle-outline"
					self.t_btn2.text_color = [.35, .66 ,.41, 1]

					toast("Цель выполнена!")

			if current_button == self.t_btn3:
				if not int(data.get("Money")) >=  10000:
					toast("Нехватает денег: " + str(10000 - int(data.get("Money"))))
				elif data["target_2"] == "opened":
					toast("Необходимо сначала отменить с/р")
				else:
					data["Money"] = str(int(data.get("Money")) - 10000)
					self.mon.text = str(data.get("Money") + " руб")

					data["Target"] = "Отменить ВПР"
					self.target.text = "Отменить ВПР"

					data["target_3"] = "bought"
					self.t_btn3.icon = "check-circle-outline"
					self.t_btn3.text_color = [.35, .66 ,.41, 1]

					toast("Цель выполнена!")

			if current_button == self.t_btn4:
				if not int(data.get("Money")) >=  60000:
					toast("Нехватает денег: " + str(60000 - int(data.get("Money"))))
				elif data["target_3"] == "opened":
					toast("Необходимо сначала отменить к/р")
				else:
					data["Money"] = str(int(data.get("Money")) - 60000)
					self.mon.text = str(data.get("Money") + " руб")

					data["Target"] = "Отменить экзамены"
					self.target.text = "Отменить экзамены"

					data["target_4"] = "bought"
					self.t_btn4.icon = "check-circle-outline"
					self.t_btn4.text_color = [.35, .66 ,.41, 1]

					toast("Цель выполнена!")

			if current_button == self.t_btn5:
				if not int(data.get("Money")) >=  150000:
					toast("Нехватает денег: " + str(150000 - int(data.get("Money"))))
				elif data["target_4"] == "opened":
					toast("Необходимо сначала отменить ВПР")
				else:
					data["Money"] = str(int(data.get("Money")) - 150000)
					self.mon.text = str(data.get("Money") + " руб")

					data["Target"] = "Цели выполнены!\nТы стал лучшим школьником на земле!"
					self.target.text = "Цели выполнены!\nТы стал лучшим школьником на земле!"

					data["target_5"] = "bought"
					self.t_btn5.icon = "check-circle-outline"
					self.t_btn5.text_color = [.35, .66 ,.41, 1]

					toast("Цель выполнена!")



class MainApp(MDApp):
	def build(self):
		Window.bind(on_request_close=self.on_request_close)

		return Game()

	# Сохранение при закрытии игры (через вкладки)
	def on_request_close(self, *args):
		with open("data/save/session.sv", "w") as write_file:
			json.dump(data, write_file)

if __name__ == "__main__":
	MainApp().run()