#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'meddebmohamedfakher'

from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from home import Home


class MyScreenManager(ScreenManager):
    mywidgets = None

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        if "mywidgets" in kwargs:
            self.mywidgets = kwargs["mywidgets"]

class First(Screen):
    def __init__(self, **kwargs):
        super(First, self).__init__(**kwargs)
