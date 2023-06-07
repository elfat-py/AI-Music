from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window


class MyCarousel(Carousel):
    def __init__(self, **kwargs):
        super(MyCarousel, self).__init__(**kwargs)



        # Add images to the carousel
        image1 = Image(
            source='lion.jpg',
            size_hint=(1/3, 1/3),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.5}
        )
        image2 = Image(
            source='mountain.jpg',
            size_hint=(1/3, 1/3),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            keep_ratio=True
        )


        #Add the FloatLayout to the carousel
        #self.add_widget(layout)
        self.add_widget(image1)
        self.add_widget(image2)

    def on_touch_down(self, touch):
        self.touch_start_x = touch.x

    def on_touch_move(self, touch):
        if self.touch_start_x is not None:
            if touch.x - self.touch_start_x > 50:
                self.load_previous()
            elif touch.x - self.touch_start_x < -50:
                self.load_next()

    def on_touch_up(self, touch):
        self.touch_start_x = None

    """""
    def on_touch_move(self, touch):
        if self.current_slide == 0 and touch.dx < -50:
            self.load_next()
            self.current_slide = 1
        elif self.current_slide == 1 and touch.dx > 50:
            self.load_previous()
            self.current_slide = 0



        def on_touch_move(self, touch):
            if touch.dx < -50:
                self.load_next()
                self.current_index = 1
            elif touch.dx > 50:
                self.load_previous()
                self.current_index = 0
"""""

""""
    def on_touch_move(self, touch):
        if abs(touch.dx) > 50:
            if touch.dx > 0:
                self.load_previous()
            else:
                self.load_next()
        return super(MyCarousel, self).on_touch_move(touch)
"""""

class MyApp(App):
    def build(self):
        carousel = MyCarousel(size_hint=(1, 1))
        # Set the app's window size to simulate a phone
        Window.size = (360, 640)

        #Here the background will be determined by the user's mood we will get the input from the file we have determined to keep this input
        background = Image(source='phoneBackground.jpg')
        layout = FloatLayout()
        layout.add_widget(background)
        layout.add_widget(carousel)




        return layout


if __name__ == '__main__':
    MyApp().run()
