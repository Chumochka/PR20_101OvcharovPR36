from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line, Rectangle

class PaintWidget(Widget):

    def on_touch_down(self, touch):
        red = int(self.parent.ids['ti_color_red'].text)/255
        green = int(self.parent.ids['ti_color_green'].text)/255
        blue = int(self.parent.ids['ti_color_blue'].text)/255
        slider = self.parent.ids['slider'].value
        with self.canvas:
            Color(red, green, blue)
            d = slider
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d*2, d*2))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width = d)
        with self.canvas:
            Color(0, 0, 0)
            Rectangle(pos=(0,0), size=(360,100))

    def on_touch_move(self, touch):
        try:
            touch.ud['line'].points += [touch.x, touch.y]
        except(KeyError):
            pass

class MainWidget(Widget):
    def on_text_changed_red(self,text):
        txt=str()
        for char in text:
            if(char.isdigit()):
                txt+=char
        if(txt==""):
            txt="0"
        if(int(txt)>255):
            txt="255"
        self.ids['ti_color_red'].text = txt

    def on_text_changed_green(self,text):
        txt=str()
        for char in text:
            if(char.isdigit()):
                txt+=char
        if(txt==""):
            txt="0"
        if(int(txt)>255):
            txt="255"
        self.ids['ti_color_green'].text = txt
    
    def on_text_changed_blue(self,text):
        txt=str()
        for char in text:
            if(char.isdigit()):
                txt+=char
        if(txt==""):
            txt="0"
        if(int(txt)>255):
            txt="255"
        self.ids['ti_color_blue'].text = txt

class PaintApp(App):

    def build(self):
        Window.size = (360,800)
        return MainWidget()

if __name__ == '__main__':
    PaintApp().run()