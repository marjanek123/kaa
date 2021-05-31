from kaa.engine import Scene
from controllers.player_controller import PlayerController
import registry
import settings
from kaa.nodes import Node
from kaa.geometry import Vector
from kaa.input import Keycode
from kaa.physics import SpaceNode
from controllers.enemies_controller import EnemiesController

from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode
from kaa.colors import Color
from map.genereate_map import BGMap
from map.genereate_objects import OBMap
import numpy as np


class GameplayScene(Scene):

    def __init__(self):
        
        self.space = SpaceNode(damping=0.1)
        self.enemies_controller = EnemiesController(self)
        


        self.root.add_child(self.space)

        self.player_controller = PlayerController(self)
        
        

        self.wood_cumulation=TextNode(font=registry.global_controllers.assets_controller.font_1,
                             origin_alignment=Alignment.left,color=Color(1, 0, 0, 1), position=Vector(10, 20), font_size=30, z_index=1,
                             text=f"Collected Wood: {self.player_controller.collected_wood}")
        self.food_cumulation=TextNode(font=registry.global_controllers.assets_controller.font_1,
                             origin_alignment=Alignment.left,color=Color(0, 1, 0, 1), position=Vector(200, 20), font_size=30, z_index=1,
                             text=f"Collected Food: {self.player_controller.collected_food}")
        self.gold_cumulation=TextNode(font=registry.global_controllers.assets_controller.font_1,
                             origin_alignment=Alignment.left,color=Color(1, 1, 0, 1), position=Vector(400, 20), font_size=30, z_index=1,
                             text=f"Collected Gold: {self.player_controller.collected_gold}")
        self.stone_cumulation=TextNode(font=registry.global_controllers.assets_controller.font_1,
                             origin_alignment=Alignment.left,color=Color(1, 1, 0, 1), position=Vector(600, 20), font_size=30, z_index=1,
                             text=f"Collected Stone: {self.player_controller.collected_stone}")
        self.population_space=TextNode(font=registry.global_controllers.assets_controller.font_1,
                             origin_alignment=Alignment.left,color=Color(1, 1, 0, 1), position=Vector(800, 20), font_size=30, z_index=1,
                             text="Population: {}/{}".format(self.player_controller.population_current,self.player_controller.player_population))
       
        
        self.root.add_child(self.wood_cumulation)
        self.root.add_child(self.food_cumulation)
        self.root.add_child(self.gold_cumulation)
        self.root.add_child(self.stone_cumulation)
        self.root.add_child(self.population_space)

        
        # self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2,
        #                     origin_alignment=Alignment.right, position=Vector(1910, 20), font_size=30, z_index=1,
        #                     color=Color(1, 0, 0, 1), text="Press Q to quit game"))
        # self.frag_count_label = TextNode(font=registry.global_controllers.assets_controller.font_1,
        #                     origin_alignment=Alignment.left, position=Vector(10, 70), font_size=40, z_index=1,
        #                     color=Color(1, 1, 0, 1), text="")
        # self.root.add_child(self.frag_count_label)
    def update(self, dt):
        self.wood_cumulation.text=f"Collected Wood: {self.player_controller.collected_wood}"
        self.food_cumulation.text=f"Collected Food: {self.player_controller.collected_food}"
        self.gold_cumulation.text=f"Collected Gold: {self.player_controller.collected_gold}"
        self.stone_cumulation.text=f"Collected Stone: {self.player_controller.collected_stone}"
        self.population_space.text="Population: {}/{}".format(self.player_controller.population_current,self.player_controller.player_population)

        self.enemies_controller.update(dt)
        self.player_controller.update(dt)
        
        if self.input.keyboard.is_pressed(Keycode.left):
            self.camera.position -= Vector(-0.1 * dt, 0)
        if self.input.keyboard.is_pressed(Keycode.right):
            self.camera.position -= Vector(0.1 * dt, 0)
        if self.input.keyboard.is_pressed(Keycode.up):
            self.camera.position -= Vector(0, -0.1 * dt)
        if self.input.keyboard.is_pressed(Keycode.down):
            self.camera.position -= Vector(0, 0.1 * dt)

        if self.input.keyboard.is_pressed(Keycode.pageup):
            self.camera.scale -= Vector(0.001*dt, 0.001*dt)
        if self.input.keyboard.is_pressed(Keycode.pagedown):
            self.camera.scale += Vector(0.001*dt, 0.001*dt)

        if self.input.keyboard.is_pressed(Keycode.home):
            self.camera.rotation_degrees += 0.03 * dt
        if self.input.keyboard.is_pressed(Keycode.end):
            self.camera.rotation_degrees -= 0.03 * dt
            
        for event in self.input.events():
            if event.keyboard_key:  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    if event.keyboard_key.key == Keycode.q:
                        self.engine.quit()
            if event.keyboard_key and event.keyboard_key.is_key_down:
                if event.keyboard_key.key == Keycode.escape:
                    self.engine.change_scene(registry.scenes.pause_scene)
    
    
        