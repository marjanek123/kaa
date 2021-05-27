from kaa.nodes import Node
import registry
from kaa.geometry import Vector

import settings
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Circle
from common.enums import  HitboxMask

class Longswordsman(BodyNode):

    def __init__(self, position, player, hp=60, delta=None,go_point=None, damage=7):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic , mass=1, z_index=10, sprite=registry.global_controllers.assets_controller.long_swordsman, position=position)
        # custom properties
        self.player=player
        self.damage=damage
        self.size=10
        self.hp = hp
        self.add_child(HitboxNode(
            shape=Circle(15),
            mask=HitboxMask.player,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER
        ))
        self.acceleration_per_second = 300
        self.delta=delta
        self.go_point=go_point
        self.mx=0
        self.my=0
        self.is_atacking=True
        self.buldier=False
        self.path=[]