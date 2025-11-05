import json

from pyllist import sllist
from pyllist import dllist

class Character:
    def __init__(self, name, character_class, hp, mp, head_slot, torso_slot, left_hand, right_hand, items):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.mp = mp
        self.head_slot = head_slot
        self.torso_slot = torso_slot
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.items = items # list of items

    def print_character_info(self):
        print(self.name + "\n" + self.character_class)

    def save_character_info(self):
        pass #rewrites character info in json file

class LibraryItem:
    def __init__(self, item_id, name, item_type, description, edible, wearable, holdable, usable, tradable):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.description = description
        self.edible = edible
        self.wearable = wearable
        self.holdable = holdable
        self.usable = usable
        self.tradable = tradable

    def print_item(self):
        print(self.name + ", " + self.description)

class CharacterItem:
    pass

while True:
    print("1 - open character menu, 2 - open item library, 3 - exit\nInput command: ")
    command = input()
    if command == "1":
        pass

    elif command == "2":
        lst = sllist()
        with open("item_library.json", "r") as f:
            data = json.load(f)

        for item in data["items"]:
            item_object = LibraryItem(item["item_id"], item["name"], item["item_type"], item["description"], item["edible"], item["wearable"], item["holdable"], item["usable"], item["tradable"])
            lst.append(item_object)

        curNode = lst.first
        while True:

            print("---- Item Library ----")
            for item in lst:
                item.print_item()
            print("----------------------")
            print("Current item: ")
            curNode.value.print_item()
            print("----------------------")
            print("1 - first item, 2 - next item, 3 - add current item into inventory, 4 - exit\nInput command: ")
            item_library_command = input()
            print("\n")

            if item_library_command == "1":
                curNode = lst.first

            elif item_library_command == "2":
                if curNode.next is not None:
                    curNode = curNode.next
                else:
                    print("Error: out of bounds\n")

            elif item_library_command == "3":
                pass

            elif item_library_command == "4":
                break


    elif command == "3":
        break
