from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class SwipeButton(Button):
    def __init__(self, **kwargs):
        super(SwipeButton, self).__init__(**kwargs)
        self.bind(on_touch_down=self.on_touch_down, on_touch_up=self.on_touch_up)

    def on_touch_down(self, instance, touch):
        if self.collide_point(*touch.pos):
            touch.ud['swipe_start'] = touch.pos
        return super(SwipeButton, self).on_touch_down(instance, touch)

    def on_touch_up(self, instance, touch):
        if 'swipe_start' in touch.ud:
            start_pos = touch.ud['swipe_start']
            end_pos = touch.pos
            if end_pos[1] > start_pos[1] + 100:  # Swipe distance threshold
                self.show_search_box()
        return super(SwipeButton, self).on_touch_up(instance, touch)

    def show_search_box(self):
        layout = self.parent
        search_box = TextInput(hint_text='Search', multiline=False)
        layout.add_widget(search_box)


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.add_widget(SwipeButton())


class MyApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
