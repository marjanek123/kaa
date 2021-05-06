import settings
from objects.player import Player
from kaa.geometry import Vector
from kaa.input import Keycode
from common.enums import WeaponType
import random
from objects.enemy import Enemy
from kaa.input import Keycode, MouseButton


class PlayerController:

    def __init__(self, scene):
        self.scene = scene
        self.player = Player(position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2))
        
        #self.scene.root.add_child(self.player)
        self.scene.space.add_child(self.player)

    def update(self, dt):
        ##### Tutorial 5####
        self.player.velocity=Vector(0,0) # reset velocity to zero, if no keys are pressed the player will stop

        if self.scene.input.keyboard.is_pressed(Keycode.w):
            self.player.velocity += Vector(0, -settings.PLAYER_SPEED)
        if self.scene.input.keyboard.is_pressed(Keycode.s):
            self.player.velocity += Vector(0, settings.PLAYER_SPEED)
        if self.scene.input.keyboard.is_pressed(Keycode.a):
            self.player.velocity += Vector(-settings.PLAYER_SPEED, 0)
        if self.scene.input.keyboard.is_pressed(Keycode.d):
            self.player.velocity += Vector(settings.PLAYER_SPEED, 0)

        if self.player.current_weapon is not None:
            # decrease weapons cooldown time by dt
            self.player.current_weapon.cooldown_time_remaining -= dt
            # if left mouse button pressed and weapon is ready to shoot, then, well, shoot a bullet!
            if self.scene.input.mouse.is_pressed(MouseButton.left) and self.player.current_weapon.cooldown_time_remaining<0:
                self.player.current_weapon.shoot_bullet()
        ##### Tutorial 5####

        if self.scene.input.keyboard.is_pressed(Keycode.w):
            self.player.position += Vector(0, -3)
        if self.scene.input.keyboard.is_pressed(Keycode.s):
            self.player.position += Vector(0, 3)
        if self.scene.input.keyboard.is_pressed(Keycode.a):
            self.player.position += Vector(-3, 0)
        if self.scene.input.keyboard.is_pressed(Keycode.d):
            self.player.position += Vector(3, 0)
            ########
        mouse_pos = self.scene.input.mouse.get_position()
        player_rotation_vector = mouse_pos - self.player.position
        self.player.rotation_degrees = player_rotation_vector.to_angle_degrees()

        for event in self.scene.input.events(): # iterate over all events which occurred during this frame
            if event.keyboard_key:
                  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    if event.keyboard_key.key == Keycode.tab:
                        self.player.cycle_weapons()
                    elif event.keyboard_key.key == Keycode.num_1:
                        self.player.change_weapon(WeaponType.MachineGun)
                    elif event.keyboard_key.key == Keycode.num_2:
                        self.player.change_weapon(WeaponType.GrenadeLauncher)
                    elif event.keyboard_key.key == Keycode.num_3:
                        self.player.change_weapon(WeaponType.ForceGun)
                    elif event.keyboard_key.key == Keycode.space:
                        self.scene.enemies_controller.add_enemy(Enemy(position=self.scene.input.mouse.get_position(),
                            rotation_degrees=random.randint(0,360)))
                    