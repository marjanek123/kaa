from kaa.nodes import Node
import registry
from kaa.geometry import Vector


from kaa.transitions import NodeScaleTransition
import settings
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Circle
from common.enums import  HitboxMask

class Vilager(BodyNode):

    def __init__(self, position, player, hp=40, delta=None,go_point=None,damage=3,):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic , mass=1, z_index=10, sprite=registry.global_controllers.assets_controller.player_img, position=position)
        # custom properties
        self.path=[]
        self.food=0
        self.wood=0
        self.gold=0
        self.stone=0
        self.player=player
        self.all_hp=hp
        self.hp = hp
        self.size=10
        self.damage=damage
        self.add_child(HitboxNode(
            shape=Circle(15),
            mask=HitboxMask.player,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER
        ))
        self.acceleration_per_second = 150
        self.delta=delta
        self.go_point=go_point
        self.mx=0
        self.my=0
        self.is_atacking=False
        self.buldier=True
        self.work=None
        self.name="Barack"



    def choop_tree(self,a):

        self.go_point=a.position
        self.delta=(self.position-a.position).length()
        self.work=a
        

    def choop_gold(self):
        print("chpoikon")
        
        
        
        
        

        