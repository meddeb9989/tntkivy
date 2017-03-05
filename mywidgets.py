#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'meddebmohamedfakher'

from kivy.properties import ObjectProperty, ListProperty


class MyWidgets():
    root = ObjectProperty(None)
    screen_manager_box = ObjectProperty(None)
    
    home_screen = None
    
    videopop = None
    pricepop = None
    reviewpop = None
    fidelitypop = None
    dragwidget = None
    slider_app = None
    screensaver_time = 30
    kiosk_state = "activated"
    deactivate_image = None
    app = None
    main_app = None
    indication_img = None

    def set_main_app(self, widget):
        self.main_app = widget

    def set_root_view(self, widget):
        self.root = widget

    def set_screen_manager_box(self, widget):
        self.screen_manager_box = widget

    def set_home_screen(self, widget):
        self.home_screenname = widget

    def set_videopop(self, widget):
        self.videopop = widget

    def set_pricepop(self, widget):
        self.pricepop = widget

    def set_reviewpop(self, widget):
        self.reviewpop = widget

    def set_fidelitypop(self, widget):
        self.fidelitypop = widget

    def set_dragwidget(self, widget):
        self.dragwidget = widget

    def set_slider_app(self, widget):
        self.slider_app = widget

    def set_screensaver_time(self, time):
        self.screensaver_time = time

    def set_kiosk_state(self, state):
        self.kiosk_state = state

    def set_deactivate_image(self, image):
        self.deactivate_image = image

    def set_app(self, widget):
        self.app = widget

    def set_indication_img(self, widget):
        self.indication_img = widget

    def get_main_app(self):
        return self.main_app

    def get_app(self):
        return self.app

    def get_root_view(self):
        return self.root

    def get_screen_manager_box(self):
        return self.screen_manager_box

    def get_home_screen(self):
        return self.home_screenname

    def get_videopop(self):
        return self.videopop

    def get_pricepop(self):
        return self.pricepop

    def get_reviewpop(self):
        return self.reviewpop

    def get_fidelitypop(self):
        return self.fidelitypop

    def get_dragwidget(self):
        return self.dragwidget

    def get_slider_app(self):
        return self.slider_app

    def get_screensaver_time(self):
        return self.screensaver_time

    def get_kiosk_state(self):
        return self.kiosk_state
   
    def get_deactivate_image(self):
        return self.deactivate_image

    def get_indication_img(self):
        return self.indication_img