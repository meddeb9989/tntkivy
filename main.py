#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from screenmanager import MyScreenManager
from screens import HomeScreen
from threading import Thread
from kivy.uix.image import Image
from kivy.uix.screenmanager import FadeTransition, SlideTransition, SwapTransition
from kivy.uix.boxlayout import BoxLayout
#from sos.web.users.crud import Crud
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.vkeyboard import VKeyboard
from mywidgets import MyWidgets
import time
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')
Config.set('kivy', 'keyboard_layout', 'azerty')
Config.set('kivy', 'desktop', 1)
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 700)
Config.write()


class Server(Thread):
    mywidgets = None

    def __init__(self, mywidgets, **kwargs):
        super(Server, self).__init__(**kwargs)
        self.mywidgets = mywidgets

    def run(self):
        mywebwidgets = self.mywidgets
        crud.set_widget(self.mywidgets)
        #app.run(host="192.168.137.123")
        #app.run()


class Paiement(App):
    server = None
    mywidgets = None
    touch_time = 0
    first_touch = True
    b = True
    deactivate = False

    def build(self):
        self.first_touch = True
        self.b = True
        self.mywidgets = MyWidgets()
        #self.server = Server(self.mywidgets)
        #self.server.daemon = True
        #self.server.start()
        self.title = 'Paiement'

        main = BoxLayout(orientation='vertical', spacing=0, mywidgets=self.mywidgets)

        myScreen = MyScreenManager(transition=SwapTransition(), mywidgets=self.mywidgets)
        
        home = HomeScreen(name="homescreen", mywidgets=self.mywidgets)

        myScreen.add_widget(home)

        self.mywidgets.set_main_app(main)
        self.mywidgets.set_screen_manager_box(myScreen)

        self.mywidgets.set_home_screen(home)
        self.mywidgets.set_app(self)

        main.add_widget(myScreen)

        Clock.max_iteration = 500
        return main

    def on_stop(self):
        #self.server._reset_internal_locks
        pass


if __name__ == "__main__":
    #Window.fullscreen = True
    Sc = Paiement()
    Sc.run()