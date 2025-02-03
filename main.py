import pygame
from player import Player

# from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_SPAWN_RATE
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    PLAYER_START_POSITION = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    # Make all player instances part of these two groups
    Player.containers = (updatable_group, drawable_group)
    player = Player(PLAYER_START_POSITION[0], PLAYER_START_POSITION[1])

    while True:
        screen.fill(color="black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        for drawable in drawable_group:
            drawable.draw(screen=screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
