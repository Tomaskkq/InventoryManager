import json

from pyllist import sllist
from pyllist import dllist

class Character:
    def __init__(self, name, character_class, hp, mp, defense, strength, head_slot, torso_slot, left_hand, right_hand, items):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.mp = mp
        self.defense = defense
        self.strength = strength
        self.head_slot = head_slot
        self.torso_slot = torso_slot
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.items = items # list of items

    def print_short_character_info(self):
        print(self.name + ", " + self.character_class)

    def print_full_character_info(self):
        head_name = self.head_slot
        torso_name = self.torso_slot
        left_name = self.left_hand
        right_name = self.right_hand
        if isinstance(self.head_slot, CharacterItem):
            head_name = self.head_slot.name

        if isinstance(self.torso_slot, CharacterItem):
            torso_name = self.torso_slot.name

        if isinstance(self.left_hand, CharacterItem):
            left_name = self.left_hand.name

        if isinstance(self.right_hand, CharacterItem):
            right_name = self.right_hand.name

        print("Name: " + self.name + "\nClass: " + self.character_class + "\nHP: " + str(self.hp) + "\nMP: " + str(self.mp) +
              "\nDefense: " + str(self.defense) + "\nStrength: " + str(self.strength) +
              "\nHead slot: " + head_name + "\nTorso slot: " + torso_name +
              "\nLeft hand: " + left_name + "\nRight hand: " + right_name + "\n")


class LibraryItem:
    def __init__(self, item_id, name, item_type, description, heal_value, defense_value, attack_value, mp_value, edible, wearable, equippable, usable, drinkable):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.description = description
        self.heal_value = heal_value
        self.defense_value = defense_value
        self.attack_value = attack_value
        self.mp_value = mp_value
        self.edible = edible
        self.wearable = wearable
        self.equippable = equippable
        self.usable = usable
        self.drinkable = drinkable


class CharacterItem(LibraryItem):
    def __init__(self, item_id, name, item_type, description, quantity, heal_value, defense_value, attack_value,
                 mp_value, edible, wearable, equippable, usable, drinkable):
        LibraryItem.__init__(self, item_id, name, item_type, description, heal_value, defense_value, attack_value,
                             mp_value, edible, wearable, equippable, usable, drinkable)
        self.quantity = quantity

    def print_character_item(self):
        print(self.name + " " + str(self.quantity) + " | " + self.item_type)

def get_item_name(list_item):
    return list_item.name

def get_item_type(list_item):
    return list_item.item_type

def sort_dllist(dllist_object, func):
    temp_list = []
    for list_item in dllist_object:
        temp_list.append(list_item)
    temp_list.sort(key=func)
    node = dllist_object.first

    while node is not None:
        next_node = node.next
        dllist_object.remove(node)
        node = next_node

    for list_item in temp_list:
        dllist_object.append(list_item)

def character_item_to_dict(ch_item):
    return {"item_id": ch_item.item_id, "name": ch_item.name, "item_type": ch_item.item_type, "description": ch_item.description,
            "quantity": ch_item.quantity, "heal_value": ch_item.heal_value, "defense_value": ch_item.defense_value,
            "attack_value": ch_item.attack_value, "mp_value": ch_item.mp_value, "edible": ch_item.edible, "wearable": ch_item.wearable,
            "equippable": ch_item.equippable, "usable": ch_item.usable, "drinkable": ch_item.drinkable
    }

def dict_item_to_character_item(dc_item):
    return CharacterItem(dc_item["item_id"], dc_item["name"], dc_item["item_type"],
                             dc_item["description"], dc_item["quantity"], dc_item["heal_value"],
                             dc_item["defense_value"], dc_item["attack_value"], dc_item["mp_value"],
                             dc_item["edible"], dc_item["wearable"], dc_item["equippable"],
                             dc_item["usable"], dc_item["drinkable"])

def get_single_item(node):
    return CharacterItem(node.value.item_id, node.value.name, node.value.item_type, node.value.description,
                  1, node.value.heal_value, node.value.defense_value, node.value.attack_value, node.value.mp_value,
                  node.value.edible, node.value.wearable, node.value.equippable, node.value.usable, node.value.drinkable)

item_library_lst = sllist()
with open("item_library.json", "r") as f:
    data = json.load(f)

for item in data["items"]:
    item_object = LibraryItem(item["item_id"], item["name"], item["item_type"], item["description"], item["heal_value"],
                              item["defense_value"], item["attack_value"], item["mp_value"], item["edible"],
                              item["wearable"], item["equippable"], item["usable"], item["drinkable"])
    item_library_lst.append(item_object)


character_lst = sllist()
with open("characters.json", "r") as f:
    data = json.load(f)

for character in data["characters"]:

    character_item_lst = dllist()
    for character_item in character["items"]:
        item = CharacterItem(character_item["item_id"], character_item["name"], character_item["item_type"],
                             character_item["description"], character_item["quantity"], character_item["heal_value"],
                             character_item["defense_value"], character_item["attack_value"], character_item["mp_value"],
                             character_item["edible"], character_item["wearable"], character_item["equippable"],
                             character_item["usable"], character_item["drinkable"])
        character_item_lst.append(item)

    head_slot = character["head_slot"]
    if head_slot != "None":
        head_slot = dict_item_to_character_item(head_slot)
    torso_slot = character["torso_slot"]
    if torso_slot != "None":
        torso_slot = dict_item_to_character_item(torso_slot)
    left_hand = character["left_hand"]
    if left_hand != "None":
        left_hand = dict_item_to_character_item(left_hand)
    right_hand = character["right_hand"]
    if right_hand != "None":
        right_hand = dict_item_to_character_item(right_hand)
    character_object = Character(character["name"], character["class"], character["hp"], character["mp"],
                                 character["defense"], character["strength"],head_slot,
                                 torso_slot, left_hand,
                                 right_hand, character_item_lst)
    character_lst.append(character_object)

while True:
    print("1 - open character list, 2 - open item library, 3 - exit\nInput command: ")
    command = input()
    if command == "1":
        curNode = character_lst.first
        while True:
            print("---- Characters  ----")
            for character_from_list in character_lst:
                character_from_list.print_short_character_info()
            print("----------------------")
            print("Current character: ")
            curNode.value.print_short_character_info()
            print("----------------------")
            print("1 - next character, 2 - open current character menu, 3 - exit")
            character_command = input("Input command: ")
            print("\n")

            if character_command == "1":
                if curNode.next is not None:
                    curNode = curNode.next
                else:
                    curNode = character_lst.first

            elif character_command == "2":
                while True:
                    curNode.value.print_full_character_info()
                    print("1 - open inventory, 2 - equip on head slot, 3 - equip on torso slot, 4 - equip on left hand, "
                          "5 - equip on right hand, 6 - unequip head slot, 7 - unequip torso slot, 8 - unequip left hand, "
                          "9 - unequip right hand, 10 - exit")
                    character_menu_command = input("Input command: ")

                    if character_menu_command == "1":
                        cur_character_item_lst = curNode.value.items
                        curItemNode = cur_character_item_lst.first
                        while True:
                            print(curNode.value.name + "'s Inventory")
                            print("----")
                            for item in cur_character_item_lst:
                                item.print_character_item()
                            print("----")
                            if curItemNode is None:
                                print("Character has no items")
                            else:
                                print("Current item: " + curItemNode.value.name)
                            print("----")
                            print("1 - next item, 2 - previous item, 3 - display item description, 4 - remove current item,"
                                  " 5 - use item, 6 - add item from library, 7 - sort by item name, 8 - sort by item type, 9 - exit")
                            character_inventory_command = input("Input command: ")
                            if character_inventory_command == "1":
                                if curItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curItemNode.next is not None:
                                    curItemNode = curItemNode.next
                                else:
                                    print("Error: out of bounds\n")

                            elif character_inventory_command == "2":
                                if curItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curItemNode.prev is not None:
                                    curItemNode = curItemNode.prev
                                else:
                                    print("Error: out of bounds\n")

                            elif character_inventory_command == "3":
                                if curItemNode is not None:
                                    while True:
                                        print("Item description:\n-----")
                                        print(curItemNode.value.name)
                                        print(curItemNode.value.description + "\n-----")
                                        print("1 - exit")
                                        item_description_command = input("Input command: ")
                                        if item_description_command == "1":
                                            break
                                else:
                                    print("Error: item does not exist\n")

                            elif character_inventory_command == "4":
                                if curItemNode is not None:
                                    print("1 - remove all, 2 - input quantity, 3 - exit")
                                    choice = input("Input command:")
                                    if choice == "1":
                                        cur_character_item_lst.remove(curItemNode)
                                        curItemNode = cur_character_item_lst.first
                                        print("Item(s) removed")
                                    elif choice == "2":
                                        while True:
                                            while True:
                                                q = input("Input quantity (or input 'q' to exit): ")
                                                if q == "q":
                                                    break
                                                else:
                                                    try:
                                                        q = int(q)
                                                        break
                                                    except ValueError:
                                                        print("Invalid input, try again")

                                            if q == "q":
                                                break
                                            elif q < curItemNode.value.quantity:
                                                curItemNode.value.quantity -= q
                                                print("Item(s) removed")
                                                break
                                            elif q == curItemNode.value.quantity:
                                                cur_character_item_lst.remove(curItemNode)
                                                curItemNode = cur_character_item_lst.first
                                                print("Item(s) removed")
                                                break
                                            elif q > curItemNode.value.quantity:
                                                print("Invalid quantity, try again")

                                    elif choice == "3":
                                        break
                                else:
                                    print("Error: item does not exist\n")

                            elif character_inventory_command == "5":
                                if curItemNode is not None:
                                    print("Selected item: " + curItemNode.value.name)
                                    options = []
                                    if curItemNode.value.edible:
                                        options.append("1 - eat item")
                                    if curItemNode.value.wearable:
                                        options.append("2 - wear item")
                                    if curItemNode.value.equippable:
                                        options.append("3 - equip item")
                                    if curItemNode.value.drinkable:
                                        options.append("4 - drink item")
                                    if curItemNode.value.usable:
                                        options.append("5 - use item")

                                    if not options:
                                        print("There are no uses for this item")
                                    else:
                                        print("\n".join(options) + " 6 - exit")
                                        action = input("Input command: ")
                                        if action == "1" and curItemNode.value.edible:
                                            print(curNode.value.name + " eats " + curItemNode.value.name.lower() + "\n")
                                            curNode.value.hp += curItemNode.value.heal_value
                                            if curItemNode.value.quantity == 1:
                                                cur_character_item_lst.remove(curItemNode)
                                                curItemNode = cur_character_item_lst.first
                                            else:
                                                curItemNode.value.quantity-=1
                                        elif action == "2":
                                            if curItemNode.value.item_type == "Helmet" or curItemNode.value.item_type == "Hat":
                                                if curNode.value.head_slot == "None":
                                                    print(curNode.value.name + " puts on " + curItemNode.value.name.lower() + "\n")
                                                    curNode.value.head_slot = get_single_item(curItemNode)
                                                    curNode.value.defense += curItemNode.value.defense_value
                                                    curNode.value.mp += curItemNode.value.mp_value
                                                    if curItemNode.value.quantity == 1:
                                                        cur_character_item_lst.remove(curItemNode)
                                                        curItemNode = cur_character_item_lst.first
                                                    else:
                                                        curItemNode.value.quantity -= 1
                                                else:
                                                    print("Head slot is occupied\n")
                                            elif curItemNode.value.item_type == "Chainmail" or curItemNode.value.item_type == "Cloak" or curItemNode.value.item_type == "Robe":
                                                if curNode.value.torso_slot == "None":
                                                    print(curNode.value.name + " puts on " + curItemNode.value.name.lower() + "\n")
                                                    curNode.value.torso_slot = get_single_item(curItemNode)
                                                    curNode.value.defense += curItemNode.value.defense_value
                                                    curNode.value.mp += curItemNode.value.mp_value
                                                    if curItemNode.value.quantity == 1:
                                                        cur_character_item_lst.remove(curItemNode)
                                                        curItemNode = cur_character_item_lst.first
                                                    else:
                                                        curItemNode.value.quantity -= 1
                                                else:
                                                    print("Torso slot is occupied\n")

                                        elif action == "3":
                                            print("1 - left hand, 2 - right hand")
                                            choice = input("Input command: ")
                                            if choice == "1":
                                                if curNode.value.left_hand == "None":
                                                    print(curNode.value.name + " equips " + curItemNode.value.name.lower() + "\n")
                                                    curNode.value.left_hand = get_single_item(curItemNode)
                                                    curNode.value.strength += curItemNode.value.attack_value
                                                    curNode.value.mp += curItemNode.value.mp_value
                                                    curNode.value.defense += curItemNode.value.defense_value
                                                    if curItemNode.value.quantity == 1:
                                                        cur_character_item_lst.remove(curItemNode)
                                                        curItemNode = cur_character_item_lst.first
                                                    else:
                                                        curItemNode.value.quantity -= 1
                                                else:
                                                    print("Left hand is occupied\n")
                                            if choice == "2":
                                                if curNode.value.right_hand == "None":
                                                    print(curNode.value.name + " equips " + curItemNode.value.name.lower() + "\n")
                                                    curNode.value.right_hand = get_single_item(curItemNode)
                                                    curNode.value.strength += curItemNode.value.attack_value
                                                    curNode.value.mp += curItemNode.value.mp_value
                                                    curNode.value.defense += curItemNode.value.defense_value
                                                    if curItemNode.value.quantity == 1:
                                                        cur_character_item_lst.remove(curItemNode)
                                                        curItemNode = cur_character_item_lst.first
                                                    else:
                                                        curItemNode.value.quantity -= 1
                                                else:
                                                    print("Right hand is occupied\n")

                                        elif action == "4":
                                            print(curNode.value.name + " drinks " + curItemNode.value.name.lower() + "\n")
                                            curNode.value.hp += curItemNode.value.heal_value
                                            if curItemNode.value.quantity == 1:
                                                cur_character_item_lst.remove(curItemNode)
                                                curItemNode = cur_character_item_lst.first

                                        elif action == "5":
                                            print(curNode.value.name + " uses " + curItemNode.value.name.lower() + "\n")
                                            curNode.value.mp += curItemNode.value.mp_value
                                            curNode.value.hp += curItemNode.value.heal_value
                                            curNode.value.strength += curItemNode.value.attack_value
                                            curNode.value.defense += curItemNode.value.defense_value
                                            if curItemNode.value.quantity == 1:
                                                cur_character_item_lst.remove(curItemNode)
                                                curItemNode = cur_character_item_lst.first

                                        elif action == "6":
                                            continue

                                else:
                                    print("Error: item does not exist\n")

                            elif character_inventory_command == "6":
                                curLibraryItemNode = item_library_lst.first
                                while True:
                                    print("---- Item Library ----")
                                    for item in item_library_lst:
                                        print(item.name)
                                    print("----------------------")
                                    print("Current item: " + curLibraryItemNode.value.name)
                                    print("----------------------")
                                    print("1 - first item, 2 - next item, 3 - add current item into inventory, 4 - exit")
                                    item_library_command = input("Input command: \n")

                                    if item_library_command == "1":
                                        curLibraryItemNode = item_library_lst.first

                                    elif item_library_command == "2":
                                        if curLibraryItemNode.next is not None:
                                            curLibraryItemNode = curLibraryItemNode.next
                                        else:
                                            print("Error: out of bounds\n")

                                    elif item_library_command == "3":
                                        q = input("Input item quantity: ")
                                        found = False
                                        for character_item in curNode.value.items: # curNode - character list node
                                            if character_item.item_id == curLibraryItemNode.value.item_id:
                                                character_item.quantity += int(q)
                                                found = True
                                        if not found:
                                            item = CharacterItem(curLibraryItemNode.value.item_id, curLibraryItemNode.value.name,
                                                                 curLibraryItemNode.value.item_type, curLibraryItemNode.value.description,
                                                                 int(q), curLibraryItemNode.value.heal_value,
                                                                 curLibraryItemNode.value.defense_value,
                                                                 curLibraryItemNode.value.attack_value,
                                                                 curLibraryItemNode.value.mp_value, curLibraryItemNode.value.edible,
                                                                 curLibraryItemNode.value.wearable, curLibraryItemNode.value.equippable,
                                                                 curLibraryItemNode.value.usable, curLibraryItemNode.value.drinkable)
                                            curNode.value.items.append(item)
                                        print("Item(s) added\n")

                                    elif item_library_command == "4":
                                        break

                            elif character_inventory_command == "7":
                                sort_dllist(curNode.value.items, get_item_name)
                                curItemNode = cur_character_item_lst.first
                                print("List sorted")

                            elif character_inventory_command == "8":
                                sort_dllist(curNode.value.items, get_item_type)
                                curItemNode = cur_character_item_lst.first
                                print("List sorted")

                            elif character_inventory_command == "9":
                                break

                    elif character_menu_command == "2":
                        head_slot_items = dllist()
                        for character_item in curNode.value.items:
                            if character_item.item_type == "Helmet" or character_item.item_type == "Hat":
                                head_slot_items.append(character_item)
                        curHeadItemNode = head_slot_items.first
                        while True:
                            print("-----\nHead slot items:")
                            for head_slot_item in head_slot_items:
                                head_slot_item.print_character_item()
                            print("-----")
                            if curHeadItemNode is None:
                                print("Character has no head slot items")
                            else:
                                print("Current item: " + curHeadItemNode.value.name)

                            print("1 - next item, 2 - previous item, 3 - wear item, 4 - exit")
                            choice = input("Input command: ")
                            if choice == "1":
                                if curHeadItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHeadItemNode.next is not None:
                                    curHeadItemNode = curHeadItemNode.next
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "2":
                                if curHeadItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHeadItemNode.prev is not None:
                                    curHeadItemNode = curHeadItemNode.prev
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "3":
                                if curHeadItemNode is not None:
                                    if curNode.value.head_slot == "None":
                                        print(curNode.value.name + " puts on " + curHeadItemNode.value.name.lower() + "\n")
                                        curNode.value.head_slot = get_single_item(curHeadItemNode)
                                        curNode.value.defense += curHeadItemNode.value.defense_value
                                        k = 0
                                        if curHeadItemNode.value.quantity == 1:
                                            for character_item in curNode.value.items:
                                                if curHeadItemNode.value.item_id == character_item.item_id:
                                                    break
                                                else:
                                                    k += 1
                                            rem_node = curNode.value.items.nodeat(k)
                                            curNode.value.items.remove(rem_node)
                                            head_slot_items.remove(curHeadItemNode)
                                            curHeadItemNode = head_slot_items.first
                                        else:
                                            curHeadItemNode.value.quantity -= 1
                                    else:
                                        print("Head slot is occupied\n")
                                else:
                                    print("No items found")
                            elif choice == "4":
                                break

                    elif character_menu_command == "3":
                        torso_slot_items = dllist()
                        for character_item in curNode.value.items:
                            if character_item.item_type == "Chainmail" or character_item.item_type == "Cloak" or character_item.item_type == "Robe":
                                torso_slot_items.append(character_item)
                        curTorsoItemNode = torso_slot_items.first
                        while True:
                            print("-----\nTorso slot items:")
                            for torso_slot_item in torso_slot_items:
                                torso_slot_item.print_character_item()
                            print("-----")
                            if curTorsoItemNode is None:
                                print("Character has no torso slot items")
                            else:
                                print("Current item: " + curTorsoItemNode.value.name)

                            print("1 - next item, 2 - previous item, 3 - wear item, 4 - exit")
                            choice = input("Input command: ")
                            if choice == "1":
                                if curTorsoItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curTorsoItemNode.next is not None:
                                    curTorsoItemNode = curTorsoItemNode.next
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "2":
                                if curTorsoItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curTorsoItemNode.prev is not None:
                                    curTorsoItemNode = curTorsoItemNode.prev
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "3":
                                if curTorsoItemNode is not None:
                                    if curNode.value.head_slot == "None":
                                        print(curNode.value.name + " puts on " + curTorsoItemNode.value.name.lower() + "\n")
                                        curNode.value.torso_slot = get_single_item(curTorsoItemNode)
                                        curNode.value.defense += curTorsoItemNode.value.defense_value
                                        k = 0
                                        if curTorsoItemNode.value.quantity == 1:
                                            for character_item in curNode.value.items:
                                                if curTorsoItemNode.value.item_id == character_item.item_id:
                                                    break
                                                else:
                                                    k += 1
                                            rem_node = curNode.value.items.nodeat(k)
                                            curNode.value.items.remove(rem_node)
                                            torso_slot_items.remove(curTorsoItemNode)
                                            curTorsoItemNode = torso_slot_items.first
                                        else:
                                            curTorsoItemNode.value.quantity -= 1
                                    else:
                                        print("Torso slot is occupied\n")
                                else:
                                    print("No items found")
                            elif choice == "4":
                                break

                    elif character_menu_command == "4":
                        hands_items = dllist()
                        for character_item in curNode.value.items:
                            if character_item.equippable:
                                hands_items.append(character_item)
                        curHandsItemNode = hands_items.first
                        while True:
                            print("-----\nLeft hand slot items:")
                            for item in hands_items:
                                item.print_character_item()
                            print("-----")
                            if curHandsItemNode is None:
                                print("Character has no equippable items")
                            else:
                                print("Current item: " + curHandsItemNode.value.name)

                            print("1 - next item, 2 - previous item, 3 - equip item, 4 - exit")
                            choice = input("Input command: ")
                            if choice == "1":
                                if curHandsItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHandsItemNode.next is not None:
                                    curHandsItemNode = curHandsItemNode.next
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "2":
                                if curHandsItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHandsItemNode.prev is not None:
                                    curHandsItemNode = curHandsItemNode.prev
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "3":
                                if curHandsItemNode is not None:
                                    if curNode.value.left_hand == "None":
                                        print(curNode.value.name + " equips " + curHandsItemNode.value.name.lower() + "\n")
                                        curNode.value.left_hand = get_single_item(curHandsItemNode)
                                        curNode.value.strength += curHandsItemNode.value.attack_value
                                        curNode.value.mp += curHandsItemNode.value.mp_value
                                        curNode.value.defense += curHandsItemNode.value.defense_value
                                        k = 0
                                        if curHandsItemNode.value.quantity == 1:
                                            for character_item in curNode.value.items:
                                                if curHandsItemNode.value.item_id == character_item.item_id:
                                                    break
                                                else:
                                                    k += 1
                                            rem_node = curNode.value.items.nodeat(k)
                                            curNode.value.items.remove(rem_node)
                                            hands_items.remove(curHandsItemNode)
                                            curHandsItemNode = hands_items.first
                                        else:
                                            curHandsItemNode.value.quantity -= 1
                                    else:
                                        print("Left hand slot is occupied\n")
                                else:
                                    print("No items found")
                            elif choice == "4":
                                break

                    elif character_menu_command == "5":
                        hands_items = dllist()
                        for character_item in curNode.value.items:
                            if character_item.equippable:
                                hands_items.append(character_item)
                        curHandsItemNode = hands_items.first
                        while True:
                            print("-----\nRight hand slot items:")
                            for item in hands_items:
                                item.print_character_item()
                            print("-----")
                            if curHandsItemNode is None:
                                print("Character has no equippable items")
                            else:
                                print("Current item: " + curHandsItemNode.value.name)

                            print("1 - next item, 2 - previous item, 3 - equip item, 4 - exit")
                            choice = input("Input command: ")
                            if choice == "1":
                                if curHandsItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHandsItemNode.next is not None:
                                    curHandsItemNode = curHandsItemNode.next
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "2":
                                if curHandsItemNode is None:
                                    print("Error: item does not exist\n")
                                elif curHandsItemNode.prev is not None:
                                    curHandsItemNode = curHandsItemNode.prev
                                else:
                                    print("Error: out of bounds\n")

                            elif choice == "3":
                                if curHandsItemNode is not None:
                                    if curNode.value.right_hand == "None":
                                        print(curNode.value.name + " equips " + curHandsItemNode.value.name.lower() + "\n")
                                        curNode.value.right_hand = get_single_item(curHandsItemNode)
                                        curNode.value.strength += curHandsItemNode.value.attack_value
                                        curNode.value.mp += curHandsItemNode.value.mp_value
                                        curNode.value.defense += curHandsItemNode.value.defense_value
                                        k = 0
                                        if curHandsItemNode.value.quantity == 1:
                                            for character_item in curNode.value.items:
                                                if curHandsItemNode.value.item_id == character_item.item_id:
                                                    break
                                                else:
                                                    k += 1
                                            rem_node = curNode.value.items.nodeat(k)
                                            curNode.value.items.remove(rem_node)
                                            hands_items.remove(curHandsItemNode)
                                            curHandsItemNode = hands_items.first
                                        else:
                                            curHandsItemNode.value.quantity -= 1
                                    else:
                                        print("Right hand slot is occupied\n")
                                else:
                                    print("No items found")
                            elif choice == "4":
                                break

                    elif character_menu_command == "6":
                        if curNode.value.head_slot != "None":
                            found = False
                            for character_item in curNode.value.items:
                                if character_item.item_id == curNode.value.head_slot.item_id:
                                    character_item.quantity += 1
                                    found = True
                            if not found:
                                curNode.value.items.append(curNode.value.head_slot)
                            curNode.value.defense -= curNode.value.head_slot.defense_value
                            print(curNode.value.name + " took off " + curNode.value.head_slot.name.lower() + "\n")
                            curNode.value.head_slot = "None"
                        else:
                            print(curNode.value.name + " is not wearing anything on head slot\n")


                    elif character_menu_command == "7":
                        if curNode.value.torso_slot != "None":
                            found = False
                            for character_item in curNode.value.items:
                                if character_item.item_id == curNode.value.torso_slot.item_id:
                                    character_item.quantity += 1
                                    found = True
                            if not found:
                                curNode.value.items.append(curNode.value.torso_slot)
                            curNode.value.defense -= curNode.value.torso_slot.defense_value
                            print(curNode.value.name + " took of " + curNode.value.torso_slot.name.lower() + "\n")
                            curNode.value.torso_slot = "None"
                        else:
                            print(curNode.value.name + " is not wearing anything on torso slot\n")

                    elif character_menu_command == "8":
                        if curNode.value.left_hand != "None":
                            found = False
                            for character_item in curNode.value.items:
                                if character_item.item_id == curNode.value.left_hand.item_id:
                                    character_item.quantity += 1
                                    found = True
                            if not found:
                                curNode.value.items.append(curNode.value.left_hand)
                            curNode.value.defense -= curNode.value.left_hand.defense_value
                            curNode.value.strength -= curNode.value.left_hand.attack_value
                            curNode.value.mp -= curNode.value.left_hand.mp_value
                            print(curNode.value.name + " unequipped " + curNode.value.left_hand.name.lower() + "\n")
                            curNode.value.left_hand = "None"
                        else:
                            print(curNode.value.name + " is not holding anything in left hand\n")

                    elif character_menu_command == "9":
                        if curNode.value.right_hand != "None":
                            found = False
                            for character_item in curNode.value.items:
                                if character_item.item_id == curNode.value.right_hand.item_id:
                                    character_item.quantity += 1
                                    found = True
                            if not found:
                                curNode.value.items.append(curNode.value.right_hand)
                            curNode.value.defense -= curNode.value.right_hand.defense_value
                            curNode.value.strength -= curNode.value.right_hand.attack_value
                            curNode.value.mp -= curNode.value.right_hand.mp_value
                            print(curNode.value.name + " unequipped " + curNode.value.right_hand.name.lower() + "\n")
                            curNode.value.right_hand = "None"
                        else:
                            print(curNode.value.name + " is not holding anything in right hand\n")

                    elif character_menu_command == "10":
                        break

            elif character_command == "3":
                break


    elif command == "2":
        curNode = item_library_lst.first
        while True:
            print("---- Item Library ----")
            for item in item_library_lst:
                print(item.name)
            print("----------------------")
            print("Current item: " + curNode.value.name)
            print("----------------------")
            print("1 - first item, 2 - next item, 3 - add current item into inventory, 4 - exit")
            item_library_command = input("Input command: \n")

            if item_library_command == "1":
                curNode = item_library_lst.first

            elif item_library_command == "2":
                if curNode.next is not None:
                    curNode = curNode.next
                else:
                    print("Error: out of bounds\n")

            elif item_library_command == "3":
                curCharacterNode = character_lst.first
                while True:
                    print("---- Characters  ----")
                    for character_from_list in character_lst:
                        character_from_list.print_short_character_info()
                    print("----------------------")
                    print("Current character: ")
                    curCharacterNode.value.print_short_character_info()
                    print("----------------------")
                    print("1 - next character, 2 - choose current character, 3 - exit")
                    choice = input("Input command: ")
                    if choice == "1":
                        if curCharacterNode.next is not None:
                            curCharacterNode = curCharacterNode.next
                        else:
                            curCharacterNode = character_lst.first

                    elif choice == "2":
                        while True:
                            q = input("Input quantity (or input 'q' to exit): ")
                            if q == "q":
                                break
                            else:
                                try:
                                    q = int(q)
                                    break
                                except ValueError:
                                    print("Invalid input, try again")
                        if q == "q":
                            continue
                        found = False
                        for character_item in curCharacterNode.value.items:
                            if character_item.item_id == curNode.value.item_id:
                                character_item.quantity += q
                                found = True
                        if not found:
                            item = CharacterItem(curNode.value.item_id, curNode.value.name, curNode.value.item_type, curNode.value.description,
                                                     q, curNode.value.heal_value, curNode.value.defense_value, curNode.value.attack_value,
                                                     curNode.value.mp_value, curNode.value.edible, curNode.value.wearable, curNode.value.equippable,
                                                     curNode.value.usable, curNode.value.drinkable)
                            curCharacterNode.value.items.append(item)
                        print("Item(s) added\n")

                    elif choice == "3":
                        break

            elif item_library_command == "4":
                break


    elif command == "3":
        with open("characters.json", "w") as f:
            new_character_lst = []
            curNode = character_lst.first
            while curNode is not None:
                items_list = []
                for item in curNode.value.items:
                    items_list.append(character_item_to_dict(item))

                head_slot = curNode.value.head_slot
                if head_slot != "None":
                    head_slot = character_item_to_dict(head_slot)
                torso_slot = curNode.value.torso_slot
                if torso_slot != "None":
                    torso_slot = character_item_to_dict(torso_slot)
                left_hand = curNode.value.left_hand
                if left_hand != "None":
                    left_hand = character_item_to_dict(left_hand)
                right_hand = curNode.value.right_hand
                if right_hand != "None":
                    right_hand = character_item_to_dict(right_hand)

                new_character_lst.append({"name": curNode.value.name, "class": curNode.value.character_class,
                                          "hp": curNode.value.hp, "mp": curNode.value.mp, "defense": curNode.value.defense,
                                          "strength": curNode.value.strength, "head_slot": head_slot,
                                          "torso_slot": torso_slot, "left_hand": left_hand,
                                          "right_hand": right_hand, "items": items_list})
                curNode = curNode.next

            save_data = {
                "characters": new_character_lst
            }
            json.dump(save_data, f, indent=4)
        break
