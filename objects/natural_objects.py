from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import  HitboxMask
from kaa.geometry import Vector
import settings
import registry
from kaa.sprites import Sprite
import os
import json

class NaturalObjects(BodyNode):

    def __init__(self,player, sprite , position, shp,size,wood=0,food=0,gold=0,stone=0):
        # node's properties
        super().__init__(body_type=BodyNodeType.static , z_index=10, sprite=sprite, position=position)
        # custom properties
        self.player=player
        self.size=size
        self.food=food
        self.wood=wood
        self.gold=gold
        self.stone=stone
        self.shape=shp        
        self.add_child(HitboxNode(
            shape=self.shape,
            mask=HitboxMask.naturalobject,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER
        ))

    
            
