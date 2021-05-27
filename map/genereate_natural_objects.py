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
import registry
from objects.natural_objects import NaturalObjects
from kaa.geometry import Vector, Polygon


class NaturalOBMap:
    def __init__(self,scene):

        self.objects=[]
        self.scene = scene
        self.createob()

    def createob(self):
        def gett(self,obj,pos):
            pos=pos
            with open("maplynaturalpos.json") as f:
                data = json.load(f)
            for a in range(0, len(data)):
                obj=data[a]["ob"]
                pos=data[a]["pos"]
                with open("maplyobj.json") as fr:
                    cdata = json.load(fr)
                for a in range(0, len(cdata)):
                    if cdata[a]["ob"]==obj:
                        p=cdata[a]["terrain"]
                        ob=NaturalObjects(size=24*cdata[a]["size"],player=0,food=cdata[a]["food"],wood=cdata[a]["wood"],gold=cdata[a]["gold"],stone=cdata[a]["stone"],sprite=Sprite(os.path.join("assets","obmap","{}".format(cdata[a]["img"]))),
                        position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48,
                        settings.VIEWPORT_HEIGHT/2-settings.MAP_Y/2*48+pos[1] * 48),
                        shp=Polygon([Vector(-24 * len(cdata[a]["terrain"][0])/2, -24*len(cdata[a]["terrain"][0])), Vector(24*len(cdata[a]["terrain"][0]), -24*len(cdata[a]["terrain"][0])), Vector(24*len(cdata[a]["terrain"][0]), 24*len(cdata[a]["terrain"][0])), Vector(-24*len(cdata[a]["terrain"][0]), 24*len(cdata[a]["terrain"][0])), Vector(-24*len(cdata[a]["terrain"][0]), -24*len(cdata[a]["terrain"][0]))]))
                        self.objects.append(ob)
                        self.scene.space.add_child(ob)  
                        get_to(p,pos)
                    


        def get_to(a1,a2):
            
            a=a2[0]
            b=a2[1]
            c = a1
            x1=0
            y1=0
            x=a
            y=b

            for row in range(len(a2)+2):
                
                y=b
                y1=0
                x += 1
                for col in range(len(a1)+1):
                    try:
                        if registry.global_controllers.assets_controller.mapk[x-1][y] == 0 and c[x1][y1]==0:
                            pass
                        elif registry.global_controllers.assets_controller.mapk[x-1][y] == 1 and c[x1][y1] == 0:
                            pass
                        elif registry.global_controllers.assets_controller.mapk[x-1][y] == 1 and c[x1][y1] >=2:
                            pass
                        elif registry.global_controllers.assets_controller.mapk[x-1][y] >= 2:
                            pass
                        else:
                            registry.global_controllers.assets_controller.mapk[x-1][y] = c[x1][y1]
                    except IndexError:
                        pass
                    
                    y += 1
                    y1+=1
                x1 += 1
            return registry.global_controllers.assets_controller.mapk


        def do_map():
            with open("maplynaturalpos.json") as f:
                    data = json.load(f)
            for a in range(0, len(data)):
                t=data[a]["ob"]
                p=data[a]["pos"]
                gett(self,t,p)        
            
            return registry.global_controllers.assets_controller.mapk
        do_map()