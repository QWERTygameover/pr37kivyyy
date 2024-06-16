from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.slider import Slider


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.line_width = 1
        self.color = (0, 0, 0, 1)
        self.canvas.before.add(Color(*self.color))

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()
        self.canvas.before.add(Color(*self.color))


class PaintApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.painter = PaintWidget()

        # Creating the top layout for controls
        controls_layout = BoxLayout(size_hint_y=0.2)

        # Add ColorPicker
        self.color_picker = ColorPicker(size_hint=(0.4, 1))
        self.color_picker.bind(color=self.on_color)
        controls_layout.add_widget(self.color_picker)

        # Add Line Width Slider
        self.slider = Slider(min=1, max=10, value=1, size_hint=(0.4, 1))
        self.slider.bind(value=self.on_line_width)
        controls_layout.add_widget(self.slider)

        # Add Clear Button
        clear_btn = Button(text='Clear', size_hint=(0.2, 1))
        clear_btn.bind(on_release=self.clear_canvas)
        controls_layout.add_widget(clear_btn)

        # Add the controls and the painter to the root layout
        root.add_widget(controls_layout)
        root.add_widget(self.painter)

        return root

    def on_color(self, instance, value):
        self.painter.color = value

    def on_line_width(self, instance, value):
        self.painter.line_width = value

    def clear_canvas(self, instance):
        self.painter.clear_canvas()


if __name__ == '__main__':
    PaintApp().run()
