import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():

    # initialization code
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    PLAYER_START_POSITION = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # Instantiant classes with groups
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group

    player = Player(PLAYER_START_POSITION[0], PLAYER_START_POSITION[1])
    asteroid_field = AsteroidField()

    dt = 0

    # Game loop
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
