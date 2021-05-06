from kaa.physics import BodyNodeType, BodyNode, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import HitboxMask
import registry
import settings
from kaa.transitions import NodeSpriteTransition
import random




class Enemy(BodyNode):

    def __init__(self, position, hp=100, *args, **kwargs):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic, mass=1,
                         z_index=10, position=position,
                         transition=NodeSpriteTransition(registry.global_controllers.assets_controller.enemy_frames,
                                                         duration=max(200, random.gauss(400,100)), loops=0),
                         *args, **kwargs)
        self.stagger_time_left = 0
        
        self.add_child(HitboxNode(
            shape=Polygon([Vector(-8, -19), Vector(8, -19), Vector(8, 19), Vector(-8, 19), Vector(-8, -19)]),
            mask=HitboxMask.enemy,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_ENEMY,
        ))
        
        # custom properties
        self.hp = hp

        
        

    def stagger(self):
        # use the "stagger" sprite
        self.sprite = registry.global_controllers.assets_controller.enemy_stagger_img
        # stagger stops enemy from moving:
        self.velocity = Vector(0, 0)
        # track time for staying in the "staggered" state
        self.stagger_time_left = 150

    def recover_from_stagger(self):
        # start using the standard sprite animation again
        self.transition=NodeSpriteTransition(registry.global_controllers.assets_controller.enemy_frames,
                                                        duration=max(200, random.gauss(400, 100)), loops=0)

        self.stagger_time_left = 0

    