#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'saidanemahdi&meedbmohamedfakher'
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
from sqlalchemy.orm import sessionmaker
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from functools import partial
from kivy.uix.videoplayer import VideoPlayer
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
import datetime
import time
import serial
import threading


class Home(FloatLayout):
    mywidgets = None
    text = None
    zerozero_btn = None
    dot_btn = None
    delete_btn = None
    b = False
    image = None
    
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        if "mywidgets" in kwargs:
            self.mywidgets = kwargs["mywidgets"]
        
        self.text = TextInput(size_hint=(.57, .2), pos_hint={'x':.05, 'y':.75}, hint_text="Entrer Montant...", font_size="40sp")        
        one_btn = Button(text="1", size_hint=(.17, .1), pos_hint={'x':.05, 'y':.6}, background_normal="images/btn.png", font_size="40sp")
        two_btn = Button(text="2", size_hint=(.17, .1), pos_hint={'x':.25, 'y':.6}, background_normal="images/btn.png", font_size="40sp")
        three_btn = Button(text="3", size_hint=(.17, .1), pos_hint={'x':.45, 'y':.6}, background_normal="images/btn.png", font_size="40sp")
        four_btn = Button(text="4", size_hint=(.17, .1), pos_hint={'x':.05, 'y':.45}, background_normal="images/btn.png", font_size="40sp")
        five_btn = Button(text="5", size_hint=(.17, .1), pos_hint={'x':.25, 'y':.45}, background_normal="images/btn.png", font_size="40sp")
        six_btn = Button(text="6", size_hint=(.17, .1), pos_hint={'x':.45, 'y':.45}, background_normal="images/btn.png", font_size="40sp")
        seven_btn = Button(text="7", size_hint=(.17, .1), pos_hint={'x':.05, 'y':.30}, background_normal="images/btn.png", font_size="40sp")
        eight_btn = Button(text="8", size_hint=(.17, .1), pos_hint={'x':.25, 'y':.30}, background_normal="images/btn.png", font_size="40sp")
        nine_btn = Button(text="9", size_hint=(.17, .1), pos_hint={'x':.45, 'y':.30}, background_normal="images/btn.png", font_size="40sp")
        self.dot_btn = Button(text=".", size_hint=(.17, .1), pos_hint={'x':.05, 'y':.15}, background_normal="images/btn.png", font_size="40sp")
        zero_btn = Button(text="0", size_hint=(.17, .1), pos_hint={'x':.25, 'y':.15}, background_normal="images/btn.png", font_size="40sp")
        self.zerozero_btn = Button(text="00", size_hint=(.17, .1), pos_hint={'x':.45, 'y':.15}, background_normal="images/btn.png", font_size="40sp")
        self.delete_btn = Button(text="C", size_hint=(.27, .1), pos_hint={'x':.05, 'y':.0}, background_normal="images/btn.png", font_size="40sp")        
        validate_btn = Button(text="Paiement", size_hint=(.27, .1), pos_hint={'x':.35, 'y':.0}, background_normal="images/btn.png", font_size="40sp")        

        self.add_widget(self.text)
        self.add_widget(one_btn)
        self.add_widget(two_btn)
        self.add_widget(three_btn)
        self.add_widget(four_btn)
        self.add_widget(five_btn)
        self.add_widget(six_btn)
        self.add_widget(seven_btn)
        self.add_widget(eight_btn)
        self.add_widget(nine_btn)
        self.add_widget(self.dot_btn)
        self.add_widget(zero_btn)
        self.add_widget(self.zerozero_btn)
        self.add_widget(self.delete_btn)
        self.add_widget(validate_btn)

        one_btn.bind(on_release=self.edit_text)
        two_btn.bind(on_release=self.edit_text)
        three_btn.bind(on_release=self.edit_text)
        four_btn.bind(on_release=self.edit_text)
        five_btn.bind(on_release=self.edit_text)
        six_btn.bind(on_release=self.edit_text)
        seven_btn.bind(on_release=self.edit_text)
        eight_btn.bind(on_release=self.edit_text)
        nine_btn.bind(on_release=self.edit_text)
        self.dot_btn.bind(on_release=self.edit_text)
        zero_btn.bind(on_release=self.edit_text)
        self.zerozero_btn.bind(on_release=self.edit_text)
        self.delete_btn.bind(on_release=self.edit_text)
        validate_btn.bind(on_release=self.pin_view)

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos, source="images/body.png")
            self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def edit_text(self, instance):
        if instance.text == 'C':
            self.text.text=""
        else:
            self.text.text=self.text.text + instance.text

    def pin_view(self, instance):
        if instance.text=="Paiement":
            instance.text="OK"
            self.dot_btn.disabled=True
            self.zerozero_btn.disabled=True
            self.dot_btn.text=""
            self.zerozero_btn.text=""
            self.delete_btn.text="Corriger"
            self.text.text="Insérer Carte..."
            self.detecter_carte()
        else:
            instance.text="Paiement"
            self.dot_btn.disabled=False
            self.zerozero_btn.disabled=False
            self.dot_btn.text="."
            self.zerozero_btn.text="00"
            self.delete_btn.text="Supprimer"
            self.text.text="Entrer Montant..."
    
    def detecter_carte(self):
        try:
            self.text.text="Lancer Arduino..."
            t = threading.Thread(target=self.read_card)
            t.daemon = True
            t.start()
            self.image=Image(source="images/frames.zip", anim_delay=0.07)
            root_window = self.get_root_window()
            root_window.add_widget(self.image)
            self.text.text="Lecture Carte..."
        except Exception as e:
            print e
            self.text.text="Can't Connect to Card !!"

    def read_card(self):
        num_carte = ""
        line = ""
        try:
            ser = serial.Serial('/dev/cu.usbmodemFA141', 115200)
            ser.write('0')
            line = str(ser.readline())
            line = str(ser.readline())
            line = str(ser.readline())
            while "TEST" not in line:
                num_carte = num_carte + line[:3]
                line = str(ser.readline())
            root_window = self.get_root_window()
            root_window.remove_widget(self.image)
            self.text.text="Carte : "+num_carte + "\nCode Pin ?"
        except Exception as e:
            print e
            self.text.text="Can't Read to Card !!"

