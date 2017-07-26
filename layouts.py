from kivy.uix.gridlayout import GridLayout

class DefaultLayout(GridLayout):
    def __init__(self, **kwargs):
        super(DefaultLayout, self).__init__(**kwargs)
        self.cols = 1
        self.generate()

    def generate(self):
        self.map = GridLayout(cols=1, size_hint_y=.9)
        self.add_widget(self.map)
        self.context_menu = GridLayout(cols=4, size_hint_y=.1)
        self.add_widget(self.context_menu)

        return self

class SideBarLayout(GridLayout):
    def __init__(self, **kwargs):
        super(SideBarLayout, self).__init__(**kwargs)
        self.cols = 2
        self.generate()

    def generate(self):
        self.left = GridLayout(cols=1, size_hint_x=.9)
        self.add_widget(self.left)
        self.right = GridLayout(cols=1, size_hint_x=.1)
        self.add_widget(self.right)

        return self
