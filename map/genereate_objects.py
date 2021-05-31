import  registry 
import numpy as np
import settings
import json
from kaa.nodes import Node
import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector
import random
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from objects.buldings.objects import Objects
from objects.buldings.barack import Barack
from objects.buldings.house import House
from kaa.geometry import Vector, Polygon
from objects.units.vilager import Vilager

class OBMap:
    def __init__(self,scene):
        self.initedObjects=[]
        self.initedObjects.append(Vilager)


        self.objects=[]
        self.scene = scene
        self.createob()
        print(self.initedObjects)

    def createob(self):
        
        
        with open("maplypleyerobjects.json") as f:
            data = json.load(f)
        for count1 in range(0, len(data)):
            obj=data[count1]["ob"]
            pos=data[count1]["pos"]
            with open("maplyobj.json") as fr:
                cdata = json.load(fr)
            for a in range(0, len(cdata)):
                for object in self.initedObjects:
                    if Vilager.name==cdata[a]["ob"]:
                        object.position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48)
                        object.player=data[count1]["player"]
                        self.objects.append(object)
                        self.scene.space.add_child(object)  
                        

                        # p=cdata[a]["terrain"]
                        # ob=Objects(population_add=cdata[a]["pop"],size=24*cdata[a]["size"],player=player,sprite=Sprite(os.path.join("assets","obmap","{}".format(cdata[a]["img"]))),
                        # position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48,
                        # settings.VIEWPORT_HEIGHT/2-settings.MAP_Y/2*48+pos[1] * 48),
                        # shp=Polygon([Vector(-24 * cdata[a]["size"], -24*cdata[a]["size"]), Vector(24*cdata[a]["size"], -24*cdata[a]["size"]), Vector(24*cdata[a]["size"], 24*cdata[a]["size"]), Vector(-24*cdata[a]["size"], 24*cdata[a]["size"]), Vector(-24*cdata[a]["size"], -24*cdata[a]["size"])]))
                        # self.objects.append(ob)
                        # self.scene.space.add_child(ob)  
                        # get_to(p,pos)
                


        # def get_to(a1,a2):
            
        #     a=a2[1]
        #     b=a2[0]
        #     c = a1
        #     x1=0
        #     y1=0
        #     x=a
        #     y=b

        #     for row in range(len(a2)+2):
                
        #         y=b
        #         y1=0
        #         x += 1
        #         for col in range(len(a1)+1):
        #             try:
        #                 if registry.global_controllers.assets_controller.mapk[x-1][y] == 0 and c[x1][y1]==0:
        #                     pass
        #                 elif registry.global_controllers.assets_controller.mapk[x-1][y] == 1 and c[x1][y1] == 0:
        #                     pass
        #                 elif registry.global_controllers.assets_controller.mapk[x-1][y] == 1 and c[x1][y1] >=2:
        #                     pass
        #                 elif registry.global_controllers.assets_controller.mapk[x-1][y] >= 2:
        #                     pass
        #                 else:
        #                     registry.global_controllers.assets_controller.mapk[x-1][y] = c[x1][y1]
        #             except IndexError:
        #                 pass
                    
        #             y += 1
        #             y1+=1
        #         x1 += 1
        #     return registry.global_controllers.assets_controller.mapk


        # def do_map():
        #     with open("maplypleyerobjects.json") as f:
        #             data = json.load(f)
        #     for a in range(0, len(data)):
        #         t=data[a]["ob"]
        #         p=data[a]["pos"]
        #         player=data[a]["player"] 
        #         gett(self,t,p,player)        
            
        #     return registry.global_controllers.assets_controller.mapk
        # do_map()