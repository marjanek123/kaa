from kaa.engine import Engine, Scene
from kaa.geometry import Vector
from kaa.sprites import Sprite, split_spritesheet
from kaa.nodes import Node
from kaa.geometry import Alignment
from kaa.transitions import NodeSpriteTransition
import os

class MyScene(Scene):

    def __init__(self):
        super().__init__()
        self.arrow_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow.png'))
        self.arrow1 = Node(sprite=self.arrow_sprite, position=Vector(200, 200))
        self.arrow2 = Node(sprite=self.arrow_sprite, position=Vector(400, 300))
        self.arrow3 = Node(sprite=self.arrow_sprite, position=Vector(600, 500))
        self.root.add_child(self.arrow1)
        self.root.add_child(self.arrow2)
        self.root.add_child(self.arrow3)
        self.arrow1.position = Vector(360, 285)
        self.arrow1.z_index = 1  # note: default z_index is 0
        self.arrow1.rotation_degrees = 45
        self.arrow1.scale = Vector(0.5, 1)  # note: default is Vector(1,1)
        # create pixel marker sprite
        self.pixel_marker_sprite = Sprite(os.path.join('assets', 'gfx', 'pixel-marker.png'))
        # create pixel_marker 1 in the same spot as arrow2 (but with bigger z-index so we can see it)
        self.pixel_marker1 = Node(sprite=self.pixel_marker_sprite, position=Vector(400, 300), z_index=100)
        # create pixel_marker 2 in the same spot as arrow3
        self.pixel_marker2 = Node(sprite=self.pixel_marker_sprite, position=Vector(600, 500), z_index=100)
        # add pixel markers to the scene
        self.root.add_child(self.pixel_marker1)
        self.root.add_child(self.pixel_marker2)
        self.arrow3.origin_alignment = Alignment.right  # default is Alignment.center
        self.green_arrow_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow-green.png'))
        self.child_arrow1 = Node(sprite=self.green_arrow_sprite, position=Vector(0,0), rotation_degrees=90, z_index=1)
        self.arrow3.add_child(self.child_arrow1)
        self.explosion_spritesheet = Sprite(os.path.join('assets', 'gfx', 'explosion.png')) # laod the whole spritesheet
        self.explosion_frames = split_spritesheet(self.explosion_spritesheet, frame_dimensions=Vector(100,100),
            frames_count=75)  # create 75 separate <Sprite> objects
        explosion_animation = NodeSpriteTransition(self.explosion_frames, duration=1000, loops=0)  # create animation
        self.explosion = Node(position=Vector(600, 150), transition=explosion_animation)  # create node with animation
        self.root.add_child(self.explosion)  # add node to scene

        explosion_animation_long =  NodeSpriteTransition(self.explosion_frames, duration=4000, loops=3,
                                                         back_and_forth=True)  # create animation
        self.explosion2 = Node(position=Vector(100, 400), transition=explosion_animation_long)
        self.explosion3 = Node(position=Vector(200, 500), transition=explosion_animation_long)
        self.root.add_child(self.explosion2)
        self.root.add_child(self.explosion3)
        self.explosion3.lifetime = 5000


    def update(self, dt):
        #  .... previous code ....
        self.arrow2.rotation_degrees += 1  # rotating 1 degree PER FRAME (not the best design)
        self.arrow3.rotation_degrees += 90 * dt / 1000  # rotating 90 degrees PER SECOND (good design!)
        self.arrow3.rotation_degrees += 1

with Engine(virtual_resolution=Vector(800, 600)) as engine:
    # set  window properties
    engine.window.size = Vector(800, 600)
    engine.window.title = "My first kaa game!"
    # initialize and run the scene
    my_scene = MyScene()
    engine.run(my_scene)