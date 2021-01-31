import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class mainOverview(BoxLayout):

    def __init__(self, **kwargs):
        BoxLayout(orientation='vertical')



class vejrVejledning(App):

    def build(self):
        return mainOverview()


if __name__ == '__main__':
    vejrVejledning().run()
