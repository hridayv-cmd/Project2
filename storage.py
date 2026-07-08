"""
Program Name: QuestLog Storage Module
Author: Hriday Vermani
Purpose: Handles file persistence using JSON serialization and error handling.
Resources Used: Python Crash Course Chapter 10.
Date: July 8, 2026
"""
import json

# === CHAPTER 8: FUNCTIONS & MODULARIZATION ===
# Code is cleanly split into separate modules instead of one giant script.
def save_character(character, filename):
    """Serializes and saves a character object state to a JSON file."""
    data = {
        "name": character.name,
        "class": character.__class__.__name__,
        "health": character.health,
        "inventory": character.inventory.items
    }
    
    # === CHAPTER 10: FILE I/O & DATA PERSISTENCE (JSON) ===
    with open(filename, 'w') as file_object:
        json.dump(data, file_object, indent=4)


def load_character(filename):
    """Loads character data from a JSON file using robust exception handling."""
    from character import Warrior, Mage
    # === CHAPTER 10: EXCEPTION HANDLING (Try-Except) ===
    try:
        with open(filename, 'r') as file_object:
            data = json.load(file_object)
            
            # Reconstruct the OOP object from raw JSON data values
            if data["class"] == "Warrior":
                hero = Warrior(data["name"], data["health"])
            else:
                hero = Mage(data["name"], data["health"])
                
            hero.inventory.items = data["inventory"]
            return hero
            
    except FileNotFoundError:
        # Graceful recovery so the game doesn't crash if a save file isn't there
        print(f"\n[ERROR] Save file '{filename}' could not be found.")
        return None
