import registry
import settings
from .gameplay import GameplayScene
from kaa.engine import Scene
from kaa.input import Keycode, MouseButton
from kaa.nodes import Node
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode


class TitleScreenScene(Scene):

    def __init__(self):
        super().__init__()
        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.title_screen_background_img,
                                 z_index=0, position=Vector(0,0), origin_alignment=Alignment.top_left))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH/2, 500), text="Click to start the game",
                                     z_index=1, origin_alignment=Alignment.center))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH/2, 550), text="Press ESC to exit",
                                     z_index=1, origin_alignment=Alignment.center))

    def update(self, dt):

        for event in self.input.events():

            if event.keyboard_key:
                if event.keyboard_key.is_key_down and event.keyboard_key.key == Keycode.escape:
                    self.engine.quit()

            if event.mouse_button:
                if event.mouse_button.is_button_down and event.mouse_button.button == MouseButton.left:
                    self.engine.change_scene(registry.scenes.gameplay_scene)
    
    
    def start_new_game(self):
        registry.scenes.gameplay_scene = GameplayScene()
        self.engine.change_scene(registry.scenes.gameplay_scene)

    def update(self, dt):
        for event in self.input.events():
            # ... other code ...
            if event.mouse_button and event.mouse_button.is_button_down and event.mouse_button.button == MouseButton.left:
                self.start_new_game()