from Weather import dangerRating

from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView

Window.size = (300,500)

class mainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        windItem = TwoLineListItem(text="Vind", secondary_text=str(dangerRating()[0]))
        windIcon = IconLeftWidget(icon="weather-windy")
        windItem.add_widget(windIcon)

        visItem = TwoLineListItem(text="Sigtbarhed", secondary_text=str(dangerRating()[1]))
        visIcon = IconLeftWidget(icon="weather-fog")
        visItem.add_widget(visIcon)

        tempItem = TwoLineListItem(text="Temperatur", secondary_text=str(dangerRating()[2]))
        tempIcon = IconLeftWidget(icon="snowflake")
        tempItem.add_widget(tempIcon)

        list_view.add_widget(windItem)
        list_view.add_widget(visItem)
        list_view.add_widget(tempItem)

        screen.add_widget(scroll)
        return screen


mainApp().run()
