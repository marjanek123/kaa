from kaa.engine import Engine
from kaa.geometry import Vector
import settings
from scenes.gameplay import GameplayScene
import registry
from controllers.assets_controller import AssetsController


with Engine(virtual_resolution=Vector(settings.VIEWPORT_WIDTH, settings.VIEWPORT_HEIGHT)) as engine:
    # initialize global controllers and keep them in the registry
    registry.global_controllers.assets_controller = AssetsController()
    # set window to fullscreen mode
    engine.window.fullscreen = True
    # initialize and run the scene
    gameplay_scene = GameplayScene()
    engine.run(gameplay_scene)
    # initialize scenes and keep them in the registry
    registry.scenes.gameplay_scene = GameplayScene()
    engine.run(registry.scenes.gameplay_scene)