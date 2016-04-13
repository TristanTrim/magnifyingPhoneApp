
from kivy.app import App
#from plyer import camera as Camera
from kivy.uix.camera import Camera
#from camerapreview import CameraPreview as Camera
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
#from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty
from random import randint, random
from functools import partial


"""
Hopefully this will end up as and application for magnifying text or whatever using your phone.
"""




class Puzzle(Camera):

    zoom = NumericProperty(100)

   #def on_texture_size(self, instance, value):
   #    self.build()

    def on_blocksize(self, instance, value):
        self.build()

   #def build(self):
   #    self.clear_widgets()
   #    texture = self.texture
   #    if not texture:
   #        return
   #    #bs = self.blocksize
   #    tw, th = self.texture_size
   #   #for x in range(int(tw / bs)):
       #    for y in range(int(th / bs)):
       #        bx = x * bs
       #        by = y * bs
       #        subtexture = texture.get_region(bx, by, bs, bs)
       #        #node = PuzzleNode(texture=subtexture,
       #        #                  size=(bs, bs), pos=(bx, by))
       #        node = Scatter(pos=(bx, by), size=(bs, bs))
       #        with node.canvas:
       #            Color(1, 1, 1)
       #            Rectangle(size=node.size, texture=subtexture)
       #        self.add_widget(node)

       #self.shuffle()

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            #self.shuffle()
            print("THE USER DOUBLE TAPPED!!")
            return True
        super(Puzzle, self).on_touch_down(touch)


class PuzzleApp(App):
    def build(self):
        root = Widget()
        print(root.height,root.width)
        puzzle = Camera(size=(480, 320), resolution=(480, 320), play=True, allow_stretch=True)
        print("The camera is a {}".format(puzzle))
        slider = Slider(min=100, max=400, step=10, size=(800, 50))
        slider.value=100
        slider.bind(value=partial(self.on_value, puzzle))

        root.add_widget(puzzle)
        root.add_widget(slider)
        return root

    def on_value(self, puzzle, instance, value):
        value = int((value + 5) / 10) * 10
        puzzle.size = (4.8*value,3.2*value)
        instance.value = value

PuzzleApp().run()


