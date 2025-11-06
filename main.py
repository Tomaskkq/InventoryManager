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
        print(self.name + ", " + self.character_class)

    def save_character_info(self):
        pass #rewrites character info in json file

class LibraryItem:
    def __init__(self, item_id, name, item_type, description, edible, wearable, equippable, usable, drinkable):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.description = description
        self.edible = edible
        self.wearable = wearable
        self.equippable = equippable
        self.usable = usable
        self.drinkable = drinkable

    def print_item(self):
        print(self.name + ", " + self.description)

class CharacterItem(LibraryItem):
    def __init__(self, item_id, name, item_type, description, quantity, edible, wearable, equippable, usable, drinkable):
        LibraryItem.__init__(self, item_id, name, item_type, description, edible, wearable, equippable, usable, drinkable)
        self.quantity = quantity

while True:
    print("1 - open character list, 2 - open item library, 3 - exit\nInput command: ")
    command = input()
    if command == "1":
        character_lst = sllist()
        with open("characters.json", "r") as f:
            data = json.load(f)

        for character in data["characters"]:
            character_item_lst = sllist()
            for character_item in character["items"]:
                item = CharacterItem(character_item["item_id"], character_item["name"], character_item["item_type"],
                                                character_item["description"], character_item["quantity"], character_item["edible"],
                                                character_item["wearable"], character_item["equippable"], character_item["usable"],
                                                character_item["drinkable"])
                character_item_lst.append(item)
            character_object = Character(character["name"], character["class"], character["hp"], character["mp"],
                                         character["head_slot"], character["torso_slot"], character["left_hand"],
                                         character["right_hand"], character_item_lst)
            character_lst.append(character_object)


        curNode = character_lst.first
        while True:
            print("---- Characters  ----")
            for character_from_list in character_lst:
                character_from_list.print_character_info()
            print("----------------------")
            print("Current character: ")
            curNode.value.print_character_info()
            print("----------------------")
            print("1 - next character, 2 - open current character menu, 3 - exit\nInput command: ")
            character_command = input()
            print("\n")

            if character_command == "1":
                if curNode.next is not None:
                    curNode = curNode.next
                else:
                    curNode = character_lst.first

            elif character_command == "2":
                pass

            elif character_command == "3":
                break


    elif command == "2":
        item_library_lst = sllist()
        with open("item_library.json", "r") as f:
            data = json.load(f)

        for item in data["items"]:
            item_object = LibraryItem(item["item_id"], item["name"], item["item_type"], item["description"], item["edible"],
                                      item["wearable"], item["equippable"], item["usable"], item["drinkable"])
            item_library_lst.append(item_object)

        curNode = item_library_lst.first
        while True:

            print("---- Item Library ----")
            for item in item_library_lst:
                item.print_item()
            print("----------------------")
            print("Current item: ")
            curNode.value.print_item()
            print("----------------------")
            print("1 - first item, 2 - next item, 3 - add current item into inventory, 4 - exit\nInput command: ")
            item_library_command = input()
            print("\n")

            if item_library_command == "1":
                curNode = item_library_lst.first

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
