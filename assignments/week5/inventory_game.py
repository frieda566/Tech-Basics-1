# --- Game State ---
inventory = []
MAX_INVENTORY_SIZE = 5

rooms = {
    "crash_site": {
        "description": "You wake up at a plane crash site. \nEverything is scattered everywhere. \nYou need to find a way of this island.",
        "items": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "Key", "type": "tool", "description": "Found near the cockpit. Might unlock something important."}
        ],
        "locked": False
    },

    "jungle": {
        "description": "Thick jungle surrounds you. \nThe air is humid and full of unfamiliar sounds.",
        "items": [
            {"name": "Machete", "type": "tool", "description": "Cuts through thick vegetation."}
         ],
        "locked": False
    },

    "cave": {
        "description": "A pitch black cave entrance lies ahead. \nWithout light, it's too dangerous to enter.",
        "items": [
            {"name": "Raft Map", "type": "clue", "description": "A torn map showing the location of a hidden raft on the island's shore."}
        ],
        "locked": True
    },

    "raft": {
        "description": "You've reached the hidden raft! It's your way off the island.",
        "items": [],
        "locked": True
    }
}

current_room = "crash_site"

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if not inventory:
        print("You don't have any inventory!")
    else:
        print("Your inventory:")
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")
    pass

def show_room_items():
    # list all items in current room
    print(rooms[current_room]["description"])
    if not rooms[current_room]["items"]:
        print("You don't have any items in that room!")
    else:
        for item in rooms[current_room]["items"]:
            print(f"- {item['name']} ({item['type']})")
    pass

def find_item(item_name, item_list):
    return next((item for item in item_list if item["name"].lower() == item_name.lower()), None)

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full!")
        return
    item = find_item(item_name, rooms[current_room]["items"])
    if item:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"You picked up the {item['name']}.")
    else:
        print("That item is not here.")
    pass

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    item = find_item(item_name, inventory)
    if item:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"You dropped the {item['name']}.")
    else:
        print("You don't have that item.")
    pass

def use(item_name):
    # Ex: use the item differently depends on the type
    item = find_item(item_name, inventory)
    if not item:
        print("You don't have that item.")
        return

    if item["type"] == "tool" and item["name"].lower() == "torch":
        if current_room == "cave":
            print("You light the torch. The cave is illuminated, revealing a passage!")
            rooms["raft"]["locked"] = False
            print("A narrow tunnel leads you toward the raft.")
        else:
            print("You light the torch, but it doesn't reveal anything useful here.")
    elif item["type"] == "tool" and item["name"].lower() == "key":
        if current_room == "jungle":
            rooms["cave"]["locked"] = False
            print("You use the key to open a rusty gate into a cave path.")
        else:
            print("You try the key, but there's nothing to unlock here.")
    elif item["type"] == "food":
        print(f"You eat the {item['name']}. It's refreshing")
        inventory.remove(item)
    elif item["type"] == "clue":
        print(item["description"])
    else:
        print("You can't use that now.")
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    item = find_item(item_name, inventory) or find_item(item_name, rooms[current_room]["items"])
    if item:
        print(f"{item['name']}: {item['description']}")
    else:
        print("You don't see that item here or in your inventory.")
    pass

def change_room(new_room):
    global current_room
    if new_room not in rooms:
        print("That room doesn't exist.")
    elif rooms[new_room]["locked"]:
        print("The path to that area is locked.\nYou need something to open it.")
    else:
        current_room = new_room
        print(f"You move to the {new_room}.")

# --- Game Loop ---

def game_loop():
    print("🏝️Welcome to the Island Escape Game!")
    print("You survived a plane crash and must explore to escape the island.")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands:")
            print(" inventory - check your items")
            print(" look - view room and item")
            print(" pickup [item] - take an item")
            print(" drop [item] - leave an item")
            print(" use [item] - use an item")
            print(" examine [item] - inspect an item")
            print(" go [place] - move to a different location (crash_site, jungle, cave, raft)")
            print(" quit - exit the game")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command.startswith("go "):
            destination = command[3:]
            change_room(destination)
            if current_room == "raft" and not rooms["raft"]["locked"]:
                print("🎉You found the raft and escaped the island! Congratulations!")
                break
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
