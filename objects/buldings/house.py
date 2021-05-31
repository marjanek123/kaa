from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import HitboxMask
from kaa.geometry import Vector
import settings
import registry
from kaa.sprites import Sprite


class House(BodyNode):

    def __init__(self, player, sprite ,position,name="House"):
        # node's properties
        super().__init__(body_type=BodyNodeType.static , z_index=10, sprite=sprite, position=position)
        # custom properties
        self.name=name
        self.size=48
        self.player=player
        # self.shape=Polygon([Vector(-24, -24), Vector(24, -24), Vector(24, 24), Vector(-24, 24), Vector(-24, -24)])
        self.gathering_wood=False
        self.gathering_food=False
        self.gathering_gold=False
        self.gathering_stone=False
        self.population_add=5
        self.add_child(HitboxNode(
            shape=Polygon([Vector(-24, -24), Vector(24, -24), Vector(24, 24), Vector(-24, 24), Vector(-24, -24)]),
            mask=HitboxMask.naturalobject,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER
        ))

    
            
