from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import WeaponType, HitboxMask
from kaa.geometry import Vector
import settings
import registry
from kaa.sprites import Sprite
import os
import json

class Objects(BodyNode):

    def __init__(self, sprite , position, shp):
        # node's properties
        super().__init__(body_type=BodyNodeType.static , z_index=10, sprite=sprite, position=position)
        # custom properties
        self.shape=shp
        self.add_child(HitboxNode(
            shape=self.shape,
            mask=HitboxMask.naturalobject,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER
        ))

    
            
