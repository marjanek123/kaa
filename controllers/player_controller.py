import settings
from objects.player import Player
from kaa.geometry import Vector
from kaa.input import Keycode
from common.enums import WeaponType
import random
from objects.enemy import Enemy
from kaa.input import Keycode, MouseButton
from kaa.geometry import Vector
from kaa.sprites import Sprite
import os
import math
from objects.objects import Objects
import json


# Player(position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2))
class PlayerController:

    def __init__(self, scene):
        self.scene = scene
        self.player = Player(position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2))
        self.players=[]
        self.presed=False
        self.basket=[]
        self.mx=0
        self.my=0
        
       

        # self.scene.root.add_child(self.player)
        
        
        # self.scene.space.add_child(self.player)

        self.add_player(Player(position=Vector(100, 400)))
        self.add_player(Player(position=Vector(1075, 220)))
        self.add_player(Player(position=Vector(1345, 240)))
        self.add_player(Player(position=Vector(1011, 780)))

    def add_player(self, player):
        self.players.append(player)  # add to the internal list
        self.scene.space.add_child(player)

    def update(self, dt):
        ##### Tutorial 5####
 # reset velocity to zero, if no keys are pressed the player will stop
        player_pos = self.player.position
        self.player.velocity=Vector(0,0) 
        basket_pozysion=[Vector(0,0), Vector(45,45),Vector(-45,-45),Vector(90,90)]
        


        # if self.scene.input.keyboard.is_pressed(Keycode.w):
        #     self.player.velocity += Vector(0, -settings.PLAYER_SPEED)
        # if self.scene.input.keyboard.is_pressed(Keycode.s):
        #     self.player.velocity += Vector(0, settings.PLAYER_SPEED)
        # if self.scene.input.keyboard.is_pressed(Keycode.a):
        #     self.player.velocity += Vector(-settings.PLAYER_SPEED, 0)
        # if self.scene.input.keyboard.is_pressed(Keycode.d):
        #     self.player.velocity += Vector(settings.PLAYER_SPEED, 0)

        

        if self.presed==False and self.scene.input.mouse.is_pressed(MouseButton.left):
            self.basket=[]
            self.presed=True
            m=self.scene.input.mouse.get_position()
            self.mx=m.x
            self.my=m.y
            
        if self.presed==True and self.scene.input.mouse.is_released(MouseButton.left):
            self.presed=False
            m1=self.scene.input.mouse.get_position()
            mx1=m1.x
            my1=m1.y
            print("last")
            print("mx1,my1",mx1,my1)
            for playe in self.players:
                px = playe.position.x
                py = playe.position.y
                print(px,py)
                if px > self.mx and py > self.my and px < mx1 and py < my1:
                    # if py > my and py < my1:
                    self.basket.append(playe)
                else:
                    pass

        
        if self.scene.input.mouse.is_pressed(MouseButton.right):
            for count,playe in enumerate(self.basket):
                
                playe.go_point=self.scene.input.mouse.get_position() + basket_pozysion[count]
                # print(playe.go_point)
            

        
        ####kontroler chodzenia########
        for playe in self.players:
            player_pos = playe.position
            playe.velocity=Vector(0,0) 


            if playe.go_point!=None:
                playe.delta=(player_pos-playe.go_point).length()
                # print(playe.delta)
                playe.rotation_degrees = (playe.go_point - player_pos).to_angle_degrees()
                playe.velocity += Vector.from_angle_degrees(playe.rotation_degrees)*\
                                    (playe.acceleration_per_second)
            if playe.delta :
                if playe.delta<=4:
                    playe.go_point=None
                    playe.delta=None
        
        
        ####kontroler chodzenia############kontroler chodzenia########  
        # 
        #                 
            # self.player.position=self.scene.input.mouse.get_position()
            
        ##### Tutorial 5####

            ########
        mouse_pos = self.scene.camera.unproject_position(self.scene.input.mouse.get_position())
        player_rotation_vector = mouse_pos - self.player.position
        

        for event in self.scene.input.events(): # iterate over all events which occurred during this frame
            if event.keyboard_key:
                  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    # if event.keyboard_key.key == Keycode.tab:
                    #     self.player.cycle_weapons()
                    # elif event.keyboard_key.key == Keycode.num_1:
                    #     self.player.change_weapon(WeaponType.MachineGun)
                    # elif event.keyboard_key.key == Keycode.num_2:
                    #     self.player.change_weapon(WeaponType.GrenadeLauncher)
                    # elif event.keyboard_key.key == Keycode.num_3:
                    #     self.player.change_weapon(WeaponType.ForceGun)
                    if event.keyboard_key.key == Keycode.space:
                        self.scene.enemies_controller.add_enemy(Enemy(position=self.scene.camera.unproject_position(
                            self.scene.input.mouse.get_position()), rotation_degrees=random.randint(0,360)))

    # def do_map(self):
    #         with open("maplypos.json") as f:
    #             data = json.load(f)
    #         for a in range(0, len(data)):
    #             obj=data[a]["ob"]
    #             pos=data[a]["pos"]
    #             with open("maplyobj.json") as fr:
    #                 cdata = json.load(fr)
    #             for a in range(0, len(cdata)):
    #                 if cdata[a]["ob"]==obj:
    #                     ob=Objects(position=Vector(settings.VIEWPORT_WIDTH/2-settings.MAP_X/2*48+pos[0]*48, settings.VIEWPORT_HEIGHT/2-settings.MAP_Y/2*48+pos[1] * 48),)
    #                     self.objects.append(ob)
    #                     self.scene.space.add_child(ob)                                       