import numpy as np
import settings
import json
from kaa.nodes import Node
import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector
import random
from kaa.physics import BodyNode, BodyNodeType, HitboxNode

class OBMap(BodyNode):
    def __init__(self):
        self.ob=createob()

    def createob(self):
        
        def gett(self,obj,pos):
            pos=pos
            with open("maplyobj.json") as fr:
                data = json.load(fr)
            for a in range(0, len(data)):
                if data[a]["ob"]==obj:
                    p=data[a]["terrain"]
                    self.root.add_child(Node(sprite=Sprite(os.path.join('assets', 'obmap', '{}'.format(data[a]["img"]))),
                                    position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48, settings.VIEWPORT_HEIGHT/2-settings.MAP_Y/2*48+pos[1] * 48), 
                                    scale=Vector(1.5,1.5),
                                    z_index=int("{}".format(data[a]["index_z"]))))
                    get_to(self,p,pos)


        def get_to(self,a1,a2):
            
            a=a2[0]
            b=a2[1]
            c = a1
            x1=0
            y1=0
            x=a
            y=b

            for row in range(len(a2)-1):
                
                y=b
                y1=0
                x += 1
                for col in range(len(a1)):
                    try:
                        if self.mapk[x-1][y] == 0 and c[x1][y1]==0:
                            pass
                        elif self.mapk[x-1][y] == 1 and c[x1][y1] == 0:
                            pass
                        elif self.mapk[x-1][y] == 1 and c[x1][y1] >=2:
                            pass
                        elif self.mapk[x-1][y] >= 2:
                            pass
                        else:
                            self.mapk[x-1][y] = c[x1][y1]
                    except IndexError:
                        pass
                    
                    y += 1
                    y1+=1
                x1 += 1
            return self.mapk


        def do_map(self):
            with open("maplypos.json") as f:
                    data = json.load(f)
            for a in range(0, len(data)):
                t=data[a]["ob"]
                p=data[a]["pos"]
                gett(self,t,p)        
            print(self.mapk)
            return self.mapk
        do_map(self)