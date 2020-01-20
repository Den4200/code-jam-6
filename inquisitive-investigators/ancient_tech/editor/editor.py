from typing import Any

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    NumericProperty,
    ListProperty
)

Builder.load_file('./ancient_tech/editor/editor.kv')


class TextEditor(BoxLayout):
    editor = ObjectProperty()
    recycler = ObjectProperty()

    foreground_color = ListProperty((1, 1, 1, 1))
    background_color = ListProperty((0, 0, 0, 1))

    font_name = StringProperty(
        './ancient_tech/static/retro_font.ttf'
    )
    font_size = NumericProperty(14)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(TextEditor, self).__init__(*args, **kwargs)



class TestApp(App):

    def build(self):
        return TextEditor()

if __name__ == '__main__':
    TestApp().run()