from kaa.nodes import Node
import registry
from kaa.geometry import Vector
from common.enums import WeaponType
from objects.weapons.force_gun import ForceGun
from objects.weapons.grenade_launcher import GrenadeLauncher
from objects.weapons.machine_gun import MachineGun

import settings
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Circle
from common.enums import WeaponType, HitboxMask

class Player(BodyNode):

    def __init__(self, position, hp=100, delta=None,go_point=None):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic , mass=1, z_index=10, sprite=registry.global_controllers.assets_controller.player_img, position=position)
        # custom properties
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
        
        

        