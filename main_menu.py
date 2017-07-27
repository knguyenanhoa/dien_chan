import subprocess

from functools import partial
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.graphics import *

from data.sets import Sets
from data.points_dict import PointsDict
from layouts import DefaultLayout
from tabs.stepper import Stepper
from tabs.overview import Overview

class MainMenu(GridLayout):
    sets = Sets()
    points_dict = PointsDict()
    letters = ['A','B','C','D','E','G',
        'H','I','K','L','M','N',
        'O','P','Q','R','S','T',
        'U','V','X','Y'
    ]

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 6

        self.show_main_menu()

    def show_main_menu(self, *args, **kwargs):
        self.clear_widgets()
        Window.set_title('Main')

        for letter in self.letters:
            button = Button(text=letter)
            button.bind(on_press=partial(self.show_sub_menu, letter=letter))
            self.add_widget(button)


    def show_sub_menu(self, *args, **kwargs):
        self.clear_widgets()
        Window.set_title('Sub')

        letter = kwargs['letter']
        list = self.sets.list(key=letter)

        for key in list.keys():
            button = Button(text=key)
            button.bind(on_press=partial(self.show_overview, key=key, list=list, letter=letter))
            self.add_widget(button)

    def show_overview(self, *args, **kwargs):

        current_letter = kwargs['letter']
        step_list = kwargs['list'][kwargs['key']]

        self.clear_widgets()
        Window.set_title(kwargs['key'])
        self.default_layout = DefaultLayout()
        self.add_widget(self.default_layout)

        ####overview
        tp = self.create_tabbed_panel(step_list=step_list)
        self.default_layout.main.add_widget(tp)

        ####context_menu
        button = Button(text='Back', size_hint_x=.1)
        button.bind(on_press=partial(self.show_sub_menu, letter=current_letter))
        self.default_layout.context_menu.add_widget(button)

        button = Button(text='Main', size_hint_x=.1)
        button.bind(on_press=partial(self.show_main_menu))
        self.default_layout.context_menu.add_widget(button)

        steps = ""
        for point in step_list:
            steps += (" => %s" % point)
        label = Label(text=steps, size_hint_x=.8, color=[1,0,0,1], bold=True)
        self.default_layout.context_menu.add_widget(label)

        button = Button(text='Print', size_hint_x=.1)
        button.bind(on_press=partial(self.printer))
        self.default_layout.context_menu.add_widget(button)

        button = Button(text='Details', size_hint_x=.1)
        #button.bind(on_press=partial(self.detail))
        self.default_layout.context_menu.add_widget(button)



        
    def printer(self, *args, **kwargs):
        pass

        #try:
        #    path = "./images/print.png"
        #    result = subprocess.run(["lpr",path])
        #except:
        #    print('No image')

    def create_tabbed_panel(self, *args, **kwargs):
        step_list = kwargs['step_list']

        tp = TabbedPanel(do_default_tab=False)

        tab1 = TabbedPanelHeader(text='Overview')
        tp.add_widget(tab1)
        tab2 = TabbedPanelHeader(text='Step')
        tp.add_widget(tab2)

        tab1.content = Overview().generate(step_list=step_list,)
        tab2.content = Stepper().generate(step_list=step_list, current_point=0,)

        return tp

