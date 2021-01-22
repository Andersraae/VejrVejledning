import kivy
kivy.require('1.11.1')


from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class frontend(GridLayout):

    def __init__(self, **kwargs):
            self.cols = 2

class vejrVejledning(App):

    def build(self):
        return frontend()


if __name__ == '__main__':
    vejrVejledning().run()
