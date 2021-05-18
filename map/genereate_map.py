import settings
from kaa.nodes import Node
import random
import json
import registry
import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector
import math
class BGMap:
    def __init__(self):
        self.bg=createbg()
        



    def openerbg(self):
        with open("map/bg_map.json") as bg:
            data = json.load(bg)
        # with open("map/bg_object.json") as fr:
        #     ob_data = json.load(fr)
        for x in range(settings.MAP_Y*settings.MAP_X):
            t = data[x]["t"]
            p = data[x]["pos"]

            with open("map/bg_object.json") as fr:
                ob_data = json.load(fr)
            for a in range(len(ob_data)):
                if ob_data[a]["terainbg"] == t:
                    self.root.add_child(Node(sprite=Sprite(os.path.join('assets', 'bgmap', '{}'.format(ob_data[a]["imgbg"]))),
                                    position=Vector(settings.WIDTH/2-settings.MAP_X/2*48+p[0] * 48, settings.HEIGHT/2-settings.MAP_Y/2*48+p[1] * 48), scale=Vector(1.5,1.5), 
                                    z_index=0))



    # def createbg(width,height):
    #     for x in settings.MAP_X -1:
    #         for y in settings.MAP_Y -1:



    #             self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.background_img,
    #                              position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2),
    #                              z_index=0))