from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.window import Window


class SlideBar(BoxLayout):
    def __init__(self, **kwargs):
        super(SlideBar, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.slide_line = Widget(size_hint=(1, 0.03))
        self.add_widget(self.slide_line)

        self.label = Label(text='Slide up', size_hint=(1, 0.07))
        self.add_widget(self.label)

        self.content = RelativeLayout(size_hint=(1, 0))
        self.search_bar = TextInput(
            size_hint=(0.8, None),
            height=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.content.add_widget(self.search_bar)
        self.add_widget(self.content)

        self.slide_animation = Animation(height=Window.height * 0.9, duration=0.3)
        self.slide_animation.bind(on_complete=self.on_slide_complete)
        self.slide_down_animation = Animation(height=0, duration=0.3)
        self.slide_down_animation.bind(on_complete=self.on_slide_down_complete)

        self.slide_up = False

        self.slide_line.size_hint = (1, 0.02)  # Initial shorter line

    def on_touch_down(self, touch):
        if touch.pos[1] < self.height * 0.1 and not self.slide_up:
            self.slide_up = True
            self.slide_animation.start(self.content)
            self.slide_line.size_hint = (1, 0.04)  # Longer line after sliding
            return True
        return super(SlideBar, self).on_touch_down(touch)

    def on_slide_complete(self, animation, widget):
        self.search_bar.focus = True

    def on_slide_down_complete(self, animation, widget):
        self.search_bar.focus = False
        self.slide_up = False
        self.slide_line.size_hint = (1, 0.03)  # Reset line size


class SlideBarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        slide_bar = SlideBar()
        layout.add_widget(slide_bar)
        return layout


if __name__ == '__main__':
    SlideBarApp().run()