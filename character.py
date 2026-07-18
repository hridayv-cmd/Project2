"""
Program Name: QuestLog Character Module
Author: Hriday Vermani
Purpose: Defines the character classes and inventory system.
Resources Used: Python Crash Course Chapters 9 (OOP) and 8 (Functions).
Date: July 8, 2026
"""

# CHAPTER 9: OOP (Composition) 
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
    #  CHAPTER 9: OOP (Base Class) 
class Character:
    """Represents a base hero in the game."""
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = Inventory()  # Composition in action

    def get_details(self):
        """Returns a formatted string of core attributes."""
        return f"Name: {self.name} | HP: {self.health}"


# CHAPTER 9: OOP (Inheritance) 
# Warrior and Mage inherit from the Character parent class
class Warrior(Character):
    """A specialized character type with stamina attributes."""
    def __init__(self, name, health=120, stamina=50):
        # Initializing the parent class attributes
        super().__init__(name, health)
        self.stamina = stamina

    # Overriding / extending parent class functionality
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Stamina: {self.stamina}"


class Mage(Character):
    """A specialized character type with mana attributes."""
    def __init__(self, name, health=80, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Mana: {self.mana}"