import kivy
kivy.require('1.11.1')


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class frontend(GridLayout):

    def __init__(self, **kwargs):
        super(frontend, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text = 'SNE'))
        self.add_widget(Label(text = 'SNE'))

class vejrVejledning(App):

    def build(self):
        return frontend()


if __name__ == '__main__':
    vejrVejledning().run()
