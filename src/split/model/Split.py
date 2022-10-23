import pygame
from src.split.model.Player import *
from src.split.model.Config import  *
from src.split.model.Platforms import *

class Split:
    """
    Logic for "Split", the game
    """
    # Attributes
    player1, player2 = None, None
    timeForLastHit = 0

    # Game Logic

    @classmethod
    def update(cls, now):
        p1 = cls.player1
        p2 = cls.player2
        add_gravity = 1
        if (p1 is None or p2 is None) and now - cls.timeForLastHit > HALF_SEC:
            if p1 is None:
                p1 = cls.create_player()[0]
                cls.player1 = p1
                cls.timeForLastHit = now
            if p2 is None:
                p2 = cls.create_player()[1]
                cls.player2 = p2
                cls.timeForLastHit = now
                if p2.get_dy() < 10:
                    p2.set_dy(add_gravity)
        elif p1 is not None or p2 is not None:
            p1.move()
            p2.move()

    @classmethod
    def platform(cls):
        platforms = pygame.sprite.Group()
        platforms.add()
            # IMPLEMENT COLLISION WITH OBJECTS
    # Used by GUI

    @classmethod
    def get_players(cls):
        return cls.player1, cls.player2

    @classmethod
    def create_player(cls):
        x1, x2, y = int(SIZE[0] * 0.015), int(SIZE[0] * 0.975), int(SIZE[1] * 0.975)
        width = height = 0.0075 * (SIZE[0] + SIZE[1])
        return Player(x1, y, width, height), Player(x2, y, width, height)

    @classmethod
    def set_player1_speed(cls, dx, dy):
        cls.player1.set_dy(dy)
        cls.player1.set_dx(dx)

    @classmethod
    def set_player2_speed(cls, dx, dy):
        cls.player2.set_dy(dy)
        cls.player2.set_dx(dx)

    @classmethod
    def player1_jump(cls, player):
        pass