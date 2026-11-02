"""
hit_detection: figures out whether a click landed on a target.
"""


"""def check_hit(targets, click_pos):
    
    Returns the target that was clicked, or None if the click missed
    every target.
    
    for target in targets:
        rect = target.get_bounding_rect()
        if rect.collidepoint(click_pos):
            return target
    return None"""

def check_hit(targets, pos):
    """Return the target clicked by the mouse, or None if no target is hit."""

    mouse_x, mouse_y = pos

    for target in targets:
        dx = mouse_x - target.x
        dy = mouse_y - target.y

        # Check whether the click is inside the circular target
        if dx * dx + dy * dy <= target.radius * target.radius:
            return target

    return None



