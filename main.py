import pygame
from player import Player

# from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_SPAWN_RATE
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    player_start_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    player = Player(player_start_pos[0], player_start_pos[1])

    while True:
        screen.fill(color="black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.draw(screen=screen)
        delta = game_clock.tick(60)
        dt = delta / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
