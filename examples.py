from kaa.engine import Engine, Scene
from kaa.geometry import Vector
from kaa.sprites import Sprite, split_spritesheet
from kaa.nodes import Node
from kaa.geometry import Alignment
from kaa.transitions import NodeSpriteTransition
import os
from kaa.geometry import Polygon, Circle




class MyScene(Scene):

    def __init__(self):
        super().__init__()
        self.arrow_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow.png'))
        self.arrow3 = Circle(233, center=Vector(200, 230))
        self.arrow1 = Node(sprite=self.arrow_sprite, position=Vector(200, 200),)


        self.arrow1.origin_alignment = Alignment.left
        self.arrow1.scale =Vector(3.1,1)
        self.root.add_child(self.arrow1)
        
        


    def update(self, dt):
        pass
        #  .... previous code ....
    # self.arrow2.rotation_degrees += 1  # rotating 1 degree PER FRAME (not the best design)
    # self.arrow3.rotation_degrees += 90 * dt / 1  # rotating 90 degrees PER SECOND (good design!)

with Engine(virtual_resolution=Vector(800, 600)) as engine:
    # set  window properties
    engine.window.size = Vector(800, 600)
    engine.window.title = "My first kaa game!"
    # initialize and run the scene
    my_scene = MyScene()
    engine.run(my_scene)