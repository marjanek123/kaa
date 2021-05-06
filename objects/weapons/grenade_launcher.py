import registry
from objects.weapons.base import WeaponBase
import random
from kaa.physics import BodyNodeType, HitboxNode, BodyNode
from kaa.geometry import Circle

import settings
from common.enums import HitboxMask

class GrenadeLauncher(WeaponBase):

    def __init__(self):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_img)