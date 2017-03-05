#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'meddebmohamedfakher'

from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from home import Home
from datetime import datetime
from kivy.core.window import Window
from operator import truediv
import time 


class HomeScreen(Screen):
    mywidgets = None

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        if "name" in kwargs:
            self.name = kwargs['name']

        if "mywidgets" in kwargs:
            self.mywidgets = kwargs["mywidgets"]
        home_box = Home(mywidgets=self.mywidgets)
        self.add_widget(home_box)