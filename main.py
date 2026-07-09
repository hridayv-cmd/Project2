"""
Program Name: QuestLog Main Application
Author: Hriday vermani
Purpose: Houses the core game loop and user interaction terminal interface.
Resources Used: Python Crash Course Chapter 8.
Date: July 8, 2026
"""
from character import Warrior, Mage
from storage import save_character, load_character

def main_menu():
    """Displays the main options to the player."""
    print("\n========================================")
    print("       Welcome to QuestLog RPG!         ")
    print("========================================")
    print("1. Create New Character")
    print("2. Load Existing Character")
    print("3. Exit")
    return input("Choose an option: ")

def gameplay_loop(hero):
    """Keeps the player engaged in managing their profile until they exit."""
    filename = f"{hero.name.lower()}_save.json"
    
    while True:
        print("\n=================== MENU ===================")
        print("1. View Profile & Inventory")
        print("2. Add Item to Inventory")
        print("3. Save and Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("\n--- CHARACTER PROFILE ---")
            print(hero.get_details())
            print(f"--- INVENTORY (Total Weight: {hero.inventory.get_total_weight()} lbs) ---")
            for item in hero.inventory.items:
                print(f"* {item['name']} ({item['weight']} lbs)")
                
        elif choice == '2':
            name = input("\nEnter item name: ")