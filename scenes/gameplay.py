from kaa.engine import Scene
from controllers.player_controller import PlayerController
import registry
import settings
from kaa.nodes import Node
from kaa.geometry import Vector
from kaa.input import Keycode
from kaa.physics import SpaceNode
from controllers.enemies_controller import EnemiesController
from controllers.collisions_controller import CollisionsController

class GameplayScene(Scene):

    def __init__(self):
        super().__init__()
        self.space = SpaceNode()
        self.enemies_controller = EnemiesController(self)
        self.root.add_child(self.space)
        self.space = SpaceNode(damping=0.3)
        self.collisions_controller = CollisionsController(self)
        self.player_controller = PlayerController(self)
        
        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.background_img,
                                 position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2),
                                 z_index=0))
    def update(self, dt):
        self.player_controller.update(dt)
        self.player_controller.update(dt)
        

        for event in self.input.events():
            if event.keyboard_key:  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    if event.keyboard_key.key == Keycode.q:
                        self.engine.quit()