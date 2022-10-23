import pygame
import time

from src.split.model.Config import *
from src.split.model.Split import *

class SplitGUI:
    """
    GUI for Split game and menu
    """
    # ATTRIBUTES
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    running = True


    @classmethod
    def run(cls):
        while cls.running:
            cls.clock.tick(GAME_SPEED)
            Split.update(time.time_ns())
            cls.render()
            cls.update()
            for event in pygame.event.get():
                cls.key_pressed(event)
                cls.key_released(event)
                if event.type == pygame.QUIT:
                    cls.running = False

    @classmethod
    def render(cls):
        cls.screen.fill(BLACK)
        pygame.draw.line(cls.screen, WHITE, [SIZE[0]/2, 0], [SIZE[0]/2, SIZE[1]], 3)

        platform_ground = pygame.Rect(0, SIZE[1] - 5, SIZE[0], 5)
        pygame.draw.rect(cls.screen, WHITE, platform_ground)

        p1, p2 = Split.get_players()
        if p1 is not None:
            rect_p1 = pygame.Rect(p1.get_x(), p1.get_y(), p1.get_width(), p1.get_height())
            player1 = pygame.draw.rect(cls.screen, WHITE, rect_p1)

        if p2 is not None:
            player2 = pygame.Rect(p2.get_x(), p2.get_y(), p2.get_width(), p2.get_height())
            pygame.draw.rect(cls.screen, WHITE, player2)

        pygame.display.flip()
        return platform_ground, player1, player2

    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Split.set_player1_speed(-PLAYER_SPEED, 0)
            elif event.key == pygame.K_d:
                Split.set_player1_speed(PLAYER_SPEED, 0)
            elif event.key == pygame.K_LEFT:
                Split.set_player2_speed(-PLAYER_SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                Split.set_player2_speed(PLAYER_SPEED, 0)
            if event.key == pygame.K_UP:
                Split.set_player2_speed(0, -PLAYER_SPEED)
            if event.key == pygame.K_UP:
                pass

    @classmethod
    def key_released(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Split.set_player1_speed(0, 0)
            elif event.key == pygame.K_d:
                Split.set_player1_speed(0, 0)
            elif event.key == pygame.K_LEFT:
                Split.set_player2_speed(0, 0)
            elif event.key == pygame.K_RIGHT:
                Split.set_player2_speed(0, 0)

    @classmethod
    def update(cls):
        collide1 = pygame.Rect.colliderect(cls.render()[0], cls.render()[1])
        collide2 = pygame.Rect.colliderect(cls.render()[0], cls.render()[2])
        p1, p2 = Split.get_players()
        print(collide1, collide2)
        if collide1:
            cls.render()[1].bottom = cls.render()[0].top
        if collide2:
            cls.render()[2].bottom = cls.render()[0].top

if __name__ == "__main__":
    SplitGUI.run()
