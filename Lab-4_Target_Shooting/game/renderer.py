"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (25, 25, 35)
COLOR_TEXT = (255, 255, 255)


def draw_scene(surface, targets):
    """Draw the background and all targets."""

    surface.fill(COLOR_BG)

    for target in targets:
        pygame.draw.circle(
            surface,
            target.color,
            (int(target.x), int(target.y)),
            target.radius
        )

        # Draw the white outline around each target
        pygame.draw.circle(
            surface,
            (255, 255, 255),
            (int(target.x), int(target.y)),
            target.radius,
            2
        )


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    """Render text at the specified position."""

    surface.blit(
        font.render(text, True, color),
        pos
    )


def draw_banner(surface, font, text):
    """Display a banner in the center of the screen."""

    surf = font.render(
        text,
        True,
        (255, 220, 80)
    )

    rect = surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2
        )
    )

    surface.blit(surf, rect)