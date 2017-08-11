import re

from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics.transformation import Matrix

from data.points_dict import PointsDict

class Locator(GridLayout):
    points_dict = PointsDict().list()
    lookup_text = ""

    def __init__(self, **kwargs):
        super(Locator, self).__init__(**kwargs)
        self.cols=3

    def generate(self, *args, **kwargs):
        self.clear_widgets()
        point = kwargs['point']
        print(point)

        self.controls = GridLayout(cols=1, size_hint_x=.2)
        self.add_widget(self.controls)
        self.generate_controls()

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/do_hinh_dien_chan_4.png")
            image.points = Widget()
            image.points.canvas.add(Color(.2,0,2)) 
            image.points.point = Point(pointsize=.35)
            draw = re.compile("A")
            if draw.search(str(point)) == None:
                try:
                    coords = self.points_dict[str(point)]
                    image.points.point.add_point(coords[0],coords[1])
                    image.points.vline = Line(points=[coords[0],100,coords[0],0])
                    image.points.hline = Line(points=[13,coords[1],87,coords[1]])
                except:
                    print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.6)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        image = Widget()
        with image.canvas:
            image.background = Image(source="./images/DoHInhTracDien.jpg")
            image.points = Widget()
            image.points.canvas.add(Color(1,0,0)) 
            image.points.point = Point(pointsize=.35)
            draw = re.compile("A")
            if draw.search(str(point)) != None:
                try:
                    coords = self.points_dict[str(point)]
                    image.points.point.add_point(coords[0],coords[1])
                    image.points.vline = Line(points=[coords[0],100,coords[0],0])
                    image.points.hline = Line(points=[13,coords[1],87,coords[1]])
                except:
                    print('Not a point or no point found')

        scatter = Scatter(auto_bring_to_front=False, size_hint_x=.6)
        scatter.apply_transform(Matrix().scale(6,6,1))
        scatter.add_widget(image)
        self.add_widget(scatter)

        return self

    def generate_controls(self):
        self.input = TextInput(multiline=False)
        self.controls.add_widget(self.input)

        button = Button(text='Locate')
        button.bind(on_press=self.lookup)
        self.controls.add_widget(button)

    def lookup(self, *args):
        text = self.input.text
        self.generate(point=text)
