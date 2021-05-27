import enum




class HitboxMask(enum.IntFlag):
    naturalobject=enum.auto()
    player = enum.auto()
    enemy = enum.auto()
    bullet = enum.auto()
    all = player | enemy | bullet | naturalobject

class EnemyMovementMode(enum.Enum):
    MoveToWaypoint = 1
    MoveToPlayer = 2



