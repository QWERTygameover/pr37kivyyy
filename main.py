from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.colorpicker import ColorPicker


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_width = 2
        self.color = (1, 0, 0, 1)  # Default to red color

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*self.color)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
            return True
        return super().on_touch_move(touch)

    def set_color(self, color):
        self.color = color

    def set_line_width(self, width):
        self.line_width = width


class PaintApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.paint_widget = PaintWidget()
        root.add_widget(self.paint_widget)

        # Create controls
        controls = BoxLayout(size_hint=(1, 0.2))

        # Add color picker
        self.color_picker = ColorPicker(size_hint=(0.7, 1))
        self.color_picker.bind(color=self.on_color)

        # Add line width slider
        self.line_width_slider = Slider(min=1, max=10, value=2, size_hint=(0.3, 1))
        self.line_width_slider.bind(value=self.on_line_width)

        # Add buttons and controls to layout
        controls.add_widget(self.color_picker)
        controls.add_widget(self.line_width_slider)

        root.add_widget(controls)

        return root

    def on_color(self, instance, value):
        self.paint_widget.set_color(value)

    def on_line_width(self, instance, value):
        self.paint_widget.set_line_width(value)


if __name__ == '__main__':
    PaintApp().run()
