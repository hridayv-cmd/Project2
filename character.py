"""
Program Name: QuestLog Character Module
Author: Hriday Vermani
Purpose: Defines the character classes and inventory system.
Resources Used: Python Crash Course Chapters 9 (OOP) and 8 (Functions).
Date: July 8, 2026
"""

# === CHAPTER 9: OOP (Composition) ===
# The Inventory class is composed of a list of items.
class Inventory:
    """Manages a character's collected items."""
    def __init__(self):
        self.items = []

    def add_item(self, item_name, weight):
        """Adds an item to the collection."""
        self.items.append({"name": item_name, "weight": weight})

    def get_total_weight(self):
        """Calculates total weight of all items using a loop."""
        return sum(item["weight"] for item in self.items)