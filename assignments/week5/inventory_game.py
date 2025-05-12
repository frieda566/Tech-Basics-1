# --- Game State ---
inventory = []
MAX_INVENTORY_SIZE = 5
current_room = "crash_site"
energy = 100
has_lit_torch = False
has_seen_map = False
solved_riddle = False
used_machete = False
ate_apple = False  # Track if apple was eaten

rooms = {
    "crash_site": {
        "description": "You wake up at a plane crash site.\nEverything is scattered everywhere.\nYou need to find a way off this island.",
        "items": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of energy."},
            {"name": "Key", "type": "tool", "description": "Found near the cockpit. Might unlock something important."}
        ],
        "next": []
    },

    "jungle": {
        "description": "Thick jungle surrounds you.\nThe air is humid and full of unfamiliar sounds.",
        "items": [
            {"name": "Machete", "type": "tool", "description": "Cuts through thick vegetation."}
        ],
        "next": [],
        "locked": False
    },

    "cave": {
        "description": "A pitch black cave entrance lies ahead.",
        "items": [],
        "locked": True,
        "next": []
    },

    "cliff": {
        "description": "A tall cliff overlooking the ocean. You can see a raft below.",
        "items": [],
        "locked": False,
        "next": ["raft"]
    },

    "raft": {
        "description": "You've reached the hidden raft! It's your way off the island.",
        "items": [],
        "locked": False,
        "next": []
    }
}

# --- Functions ---

def show_inventory():
    if not inventory:
        print("You don't have any inventory!")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

def show_room_items():
    print(rooms[current_room]["description"])
    if rooms[current_room]["items"]:
        for item in rooms[current_room]["items"]:
            print(f"- {item['name']} ({item['type']})")


def find_item(item_name, item_list):
    return next((item for item in item_list if item["name"].lower() == item_name.lower()), None)

def pick_up(item_name):
    global current_room
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full!")
        return
    item = find_item(item_name, rooms[current_room]["items"])
    if item:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"You picked up the {item['name']}.")

        if current_room == "crash_site" and len(rooms["crash_site"]["items"]) == 0:
            rooms["crash_site"]["next"].append("jungle")
            print("A path to the jungle is now visible.")
        elif item["name"].lower() == "machete":
            print("The jungle is thick with trees. You might need to cut your way through to discover the next area.")
        elif item["name"].lower() == "raft map":
            print("You picked up the Raft Map. You should use it to find your next destination.")
    else:
        print("That item is not here.")

def drop(item_name):
    item = find_item(item_name, inventory)
    if item:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"You dropped the {item['name']}.")
    else:
        print("You don't have that item.")

def use(item_name):
    global has_lit_torch, has_seen_map, energy, solved_riddle, used_machete, ate_apple

    item = find_item(item_name, inventory)
    if not item:
        print("You don't have that item.")
        return

    if item["name"].lower() == "key":
        if current_room == "cave" and rooms["cave"]["locked"]:
            rooms["cave"]["locked"] = False
            print("You use the key to unlock the cave entrance.")
            print("A pitch black cave entrance lies ahead. You can't see anything inside.")
        else:
            print("There's nothing to unlock here.")

    elif item["name"].lower() == "torch":
        if current_room == "cave" and not has_lit_torch:
            has_lit_torch = True
            print("You light the torch. A Raft Map lays on the ground now.")
            rooms["cave"]["items"].append({"name": "Raft Map", "type": "clue", "description": "A torn map showing the location of a hidden raft on the island's shore."})
        else:
            print("You light the torch but there's nothing new to see.")

    elif item["name"].lower() == "raft map":
        if not has_seen_map:
            has_seen_map = True
            if "cliff" not in rooms["cave"]["next"]:
                rooms["cave"]["next"].append("cliff")
            print("The raft map shows a trail leading to a cliff.")
        else:
            print("You've already used the map.")

    elif item["name"].lower() == "apple":
        print(f"You eat the {item['name']}. Your energy is restored.")
        inventory.remove(item)
        energy = 100
        ate_apple = True  # Mark that the apple was eaten

    elif item["name"].lower() == "machete":
        if current_room == "jungle" and not used_machete:
            used_machete = True
            rooms["jungle"]["next"].append("cave")
            print("You use the machete to cut through the jungle. A hidden cave is revealed!")
        else:
            print("You can't use that now.")

    else:
        print("You can't use that now.")

def examine(item_name):
    item = find_item(item_name, inventory) or find_item(item_name, rooms[current_room]["items"])
    if item:
        print(f"{item['name']}: {item['description']}")
    else:
        print("You don't see that item here or in your inventory.")

def change_room(destination):
    global current_room, energy, ate_apple

    if destination not in rooms:
        print("That place doesn't exist.")
        return

    if destination not in rooms[current_room].get("next", []):
        if rooms[destination].get("locked", False):
            print("That place is locked. Try using something to unlock it.")
        else:
            print("You can't go there yet.")
        return

    # If the player is at the cliff, they must eat the apple to proceed
    if destination == "cliff":
        print("\nYou move to the cliff.")
        print(rooms[destination]["description"])
        print("The climb has drained your energy.")
        print("Your energy is too low to move forward. Perhaps you should eat something to regain strength.")
        return

    # After the player eats the apple, they can go to the raft
    if destination == "raft" and not ate_apple:
        print("Your energy is too low to board the raft. You need to eat the apple first to regain strength.")
        return
    elif destination == "raft" and ate_apple:
        print("You move to the raft.")
        print(rooms[destination]["description"])
        # Add the riddle interaction once the player is ready
        if not solved_riddle:
            solve_raft_riddle()
        else:
            print("🎉 You found the raft and escaped the island! Congratulations!")
            exit()

    current_room = destination
    if current_room == "cliff":
        energy -= 50
    elif current_room == "raft":
        print("You move to the raft.")
        print(rooms[current_room]["description"])
        if not solved_riddle:
            solve_raft_riddle()
        else:
            print("🎉 You found the raft and escaped the island! Congratulations!")
            exit()
    else:
        print(f"\nYou move to the {destination}.")
        if destination == "cave" and rooms["cave"]["locked"]:
            print("The cave is locked. Maybe a key could open it.")
        show_room_items()

def solve_raft_riddle():
    global solved_riddle
    print("Before you can board the raft, a puzzle appears carved on wood:")
    print("'I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?'")
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer == "echo":
            solved_riddle = True
            print("Correct! The path is clear. You board the raft and escape the island. 🎉")
            exit()
        else:
            print("Wrong answer. Try again.")

# --- Game Loop ---

def game_loop():
    print("\U0001F3DD️ Welcome to the Island Escape Game!")
    print("You survived a plane crash and must explore to escape the island.")
    print("Type 'help' for a list of commands.")
    print("Available locations: crash_site")
    print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [place], quit")
    show_room_items()

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands:")
            print(" inventory - check your items")
            print(" look - view room and item")
            print(" pickup [item] - take an item")
            print(" drop [item] - leave an item")
            print(" use [item] - use an item")
            print(" examine [item] - inspect an item")
            print(" go [place] - move to an accessible place")
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
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()