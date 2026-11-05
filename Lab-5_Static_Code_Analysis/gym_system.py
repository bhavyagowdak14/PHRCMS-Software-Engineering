"""Fitness club class booking and roster management system."""

import json
from pathlib import Path

# Global state
class_capacity = {"Yoga": 3, "HIIT": 2, "Spin": 4}
rosters = {}


def book_class(member_id, class_name, attendance_log=None):
    """Book a member into a fitness class."""
    if attendance_log is None:
        attendance_log = []

    if class_name not in rosters:
        rosters[class_name] = []

    if len(rosters[class_name]) >= class_capacity.get(class_name, 0):
        print(f"Class full: {class_name}")
        return False

    rosters[class_name].append(member_id)
    attendance_log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id, class_name):
    """Cancel an existing member booking."""
    try:
        rosters[class_name].remove(member_id)
    except (KeyError, ValueError):
        print("Nothing to cancel")


def set_capacity(class_name, seats):
    """Set the maximum capacity of a fitness class."""
    if not isinstance(seats, int) or seats < 0:
        raise ValueError("Capacity must be a non-negative integer.")

    class_capacity[class_name] = seats


def add_members(class_name, count):
    """Add the requested number of guest members."""
    if not isinstance(count, int) or count < 0:
        raise ValueError("Guest count must be a non-negative integer.")

    for i in range(count):
        book_class(f"GUEST-{i}", class_name)


def export_roster(file="gym_schedule.json"):
    """Export all class rosters to a JSON file."""
    with open(file, "w", encoding="utf-8") as file_obj:
        json.dump(rosters, file_obj, indent=4)


def clear_old_exports(prefix="old_"):
    """Remove old JSON export files matching the given prefix."""
    for file_path in Path(".").glob(f"{prefix}*.json"):
        if file_path.is_file():
            file_path.unlink()


def show_rosters():
    """Display all fitness class rosters."""
    for class_name, members in rosters.items():
        print(class_name, ":", ", ".join(str(member) for member in members))


def main():
    """Run the fitness club booking demonstration."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class(55, "HIIT")
    book_class("M5", "Pilates")

    try:
        set_capacity("Spin", -2)
    except ValueError as error:
        print(error)

    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    guest_input = input(
        "How many walk-in guests for HIIT? (Enter for 1): "
    ) or "1"

    try:
        add_members("HIIT", int(guest_input))
    except ValueError as error:
        print(f"Invalid guest count: {error}")

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
