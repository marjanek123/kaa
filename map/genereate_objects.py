from registry import Registry
import numpy as np
import settings
import json
from kaa.nodes import Node
import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector
import random
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from objects.player import Player
from objects.objects import Objects
from kaa.geometry import Vector, Polygon


class OBMap:
    def __init__(self, scene):
        self.objects=[]
        self.scene = scene
        self.createob()

    def createob(self):
            with open("maplypos.json") as f:
                data = json.load(f)
            for a in range(0, len(data)):
                obj=data[a]["ob"]
                pos=data[a]["pos"]
                with open("maplyobj.json") as fr:
                    cdata = json.load(fr)
                for a in range(0, len(cdata)):
                    if cdata[a]["ob"]==obj:
                        ob=Objects(sprite=Sprite(os.path.join("assets","obmap","{}".format(cdata[a]["img"]))),
                        position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48,
                        settings.VIEWPORT_HEIGHT/2-settings.MAP_Y/2*48+pos[1] * 48),
                        shp=Polygon([Vector(-24 * len(cdata[a]["terrain"][0])/2, -24*len(cdata[a]["terrain"][0])), Vector(24*len(cdata[a]["terrain"][0]), -24*len(cdata[a]["terrain"][0])), Vector(24*len(cdata[a]["terrain"][0]), 24*len(cdata[a]["terrain"][0])), Vector(-24*len(cdata[a]["terrain"][0]), 24*len(cdata[a]["terrain"][0])), Vector(-24*len(cdata[a]["terrain"][0]), -24*len(cdata[a]["terrain"][0]))]))
                        self.objects.append(ob)
                        self.scene.space.add_child(ob)  