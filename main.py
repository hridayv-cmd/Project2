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
            # === CHAPTER 10: USER INPUT EXCEPTION HANDLING ===
            try:
                weight = float(input("Enter item weight (lbs): "))
                hero.inventory.add_item(name, weight)
                print(f"[SUCCESS] Added {name} to inventory.")
            except ValueError:
                print("[ERROR] Invalid weight entry. Please enter a valid number (e.g., 4.5).")
                
        elif choice == '3':
            print(f"\n[SYSTEM] Saving character data to '{filename}'...")
            save_character(hero, filename)
            print("[SUCCESS] Data saved successfully. Goodbye!")
            break

def main():
    choice = main_menu()
    if choice == '1':
        name = input("\nEnter character name: ")
        char_class = input("Choose a class (Warrior / Mage): ").strip().lower()
        
        if char_class == 'mage':
            hero = Mage(name)
        else:
            hero = Warrior(name) # Default to warrior
            
        print(f"\n[SUCCESS] Created {hero.name} the {hero.__class__.__name__}!")
        gameplay_loop(hero)
        
    elif choice == '2':
        name = input("\nEnter the character name to load: ").strip().lower()
        hero = load_character(f"{name}_save.json")
        if hero:
            print(f"\n[SUCCESS] Welcome back, {hero.name}!")
            gameplay_loop(hero)
            
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()