import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collision_check(self, colliding_object):

        distance = self.position.distance_to(colliding_object.position)
        r1 = self.radius
        r2 = colliding_object.radius

        combined_radius = r1 + r2

        return distance <= combined_radius
