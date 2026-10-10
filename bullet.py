# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship, direction="up"):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store decimal values for the bullet's position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor_y = ai_settings.bullet_speed_factor_y
        self.speed_factor_x = ai_settings.bullet_speed_factor_x

        # Set direction
        self.direction = direction

    def update(self):
        """Update the bullets position"""
        if self.direction == "up":
            self.y -= self.speed_factor_y
        elif self.direction == "left":
            self.y -= self.speed_factor_y  # move up
            self.x -= self.speed_factor_x  # move slightly left
        elif self.direction == "right":
            self.y -= self.speed_factor_y  # move up
            self.x += self.speed_factor_x  # move slightly right

        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
