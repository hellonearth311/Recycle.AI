from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout 

class RecycleApp(App):
    def build(self):
        layout = FloatLayout()
        button = Button(
            text='Click Me!',
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(button)

        return layout


