"""
Target: a circular target the player clicks on.
(x, y) represents the CENTER of the circle.
"""

import pygame


class Target:
    def __init__(
        self,
        x,
        y,
        radius=28,
        color=(230, 90, 70),
        vx=2,
        vy=2
    ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        # Movement velocity
        self.vx = vx
        self.vy = vy

    def update(self, width, height):
        """Move the target and bounce it off the window boundaries."""

        # Move the target
        self.x += self.vx
        self.y += self.vy

        # Bounce off the left and right boundaries
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx = abs(self.vx)

        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.vx = -abs(self.vx)

        # Bounce off the top and bottom boundaries
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy = abs(self.vy)

        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.vy = -abs(self.vy)