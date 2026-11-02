import random
import pygame

from game.target import Target
from game.hit_detection import check_hit
from game.renderer import WIDTH, HEIGHT

NUM_TARGETS = 3
TARGET_RADIUS = 28
ROUND_DURATION = 30


class GameEngine:
    def __init__(self):
        self.round_duration = ROUND_DURATION
        self.start_new_round()

    def start_new_round(self):
        """Start a new round and reset all statistics and the timer."""

        self.targets = [
            self._random_target()
            for _ in range(NUM_TARGETS)
        ]

        self.hits = 0
        self.misses = 0
        self.score = 0
        self.combo = 1

        self.start_time = pygame.time.get_ticks()
        self.remaining_time = self.round_duration
        self.game_over = False

    def _random_target(self):
        x = random.randint(
            TARGET_RADIUS + 10,
            WIDTH - TARGET_RADIUS - 10
        )

        y = random.randint(
            TARGET_RADIUS + 10,
            HEIGHT - TARGET_RADIUS - 10
        )

        speed = random.choice([2, 4])
        vx = random.choice([-speed, speed])
        vy = random.choice([-speed, speed])

        return Target(
            x,
            y,
            radius=TARGET_RADIUS,
            vx=vx,
            vy=vy
        )

    def handle_click(self, pos):
        """Process a shot only while the round is active."""

        if self.game_over:
            return

        # Check the timer before accepting a shot.
        self.update_timer()

        if self.game_over:
            return

        target = check_hit(self.targets, pos)

        if target is not None:
            self.hits += 1

            # Task 3: Combo scoring
            self.score += 10 * self.combo
            self.combo += 1

            self.targets.remove(target)
            self.targets.append(self._random_target())

        else:
            self.misses += 1
            self.combo = 1

    def update_timer(self):
        """Update the countdown and end the round at zero."""

        if self.game_over:
            return

        elapsed_seconds = (
            pygame.time.get_ticks() - self.start_time
        ) / 1000

        self.remaining_time = max(
            0,
            self.round_duration - elapsed_seconds
        )

        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.game_over = True

    def update(self):
        """Update the timer and move targets during the round."""

        self.update_timer()

        if not self.game_over:
            for target in self.targets:
                target.update(WIDTH, HEIGHT)

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(surface, self.targets)

        # Display hits and misses.
        renderer.draw_text(
            surface,
            font,
            f"Hits: {self.hits}  Misses: {self.misses}",
            (10, 10)
        )

        # Display the score.
        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}",
            (10, 40)
        )

        # Display the combo multiplier.
        renderer.draw_text(
            surface,
            font,
            f"Combo: {self.combo}x",
            (10, 70)
        )

        # Display the countdown.
        seconds_left = int(self.remaining_time + 0.999)

        renderer.draw_text(
            surface,
            font,
            f"Time: {seconds_left}s",
            (10, 100)
        )

        if self.game_over:
            # Dark overlay to make the final message stand out.
            overlay = pygame.Surface(
                surface.get_size(),
                pygame.SRCALPHA
            )
            overlay.fill((0, 0, 0, 180))
            surface.blit(overlay, (0, 0))

            renderer.draw_banner(
                surface,
                font,
                "ROUND OVER!"
            )

            renderer.draw_text(
                surface,
                font,
                f"Final Score: {self.score}",
                (surface.get_width() // 2 - 95,
                 surface.get_height() // 2 + 35)
            )

            renderer.draw_text(
                surface,
                font,
                "Press R to play again",
                (surface.get_width() // 2 - 125,
                 surface.get_height() // 2 + 70)
            )

