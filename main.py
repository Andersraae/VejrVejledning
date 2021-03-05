from Weather import dangerRating

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem, TwoLineIconListItem
from kivymd.uix.list import IconLeftWidget

Window.size = (300,500)

class mainApp(MDApp):
    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        windItem = TwoLineIconListItem(text="Vind", secondary_text=str(dangerRating()[0]))
        windIcon = IconLeftWidget(icon="weather-windy")
        windItem.add_widget(windIcon)

        visItem = TwoLineIconListItem(text="Sigtbarhed", secondary_text=str(dangerRating()[1]))
        visIcon = IconLeftWidget(icon="weather-fog")
        visItem.add_widget(visIcon)

        tempItem = TwoLineIconListItem(text="Temperatur", secondary_text=str(dangerRating()[2]))
        tempIcon = IconLeftWidget(icon="snowflake")
        tempItem.add_widget(tempIcon)

        list_view.add_widget(windItem)
        list_view.add_widget(visItem)
        list_view.add_widget(tempItem)

        screen.add_widget(scroll)
        return screen


mainApp().run()
