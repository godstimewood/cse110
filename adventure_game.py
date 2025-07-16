# Adventure Game Code Snippet
# This is a simple text-based adventure game where the player makes choices to navigate through a story.
# I showed this game to my friends, and they enjoyed it. They found it engaging and fun.

choice1 = input("You wake up in a dark forest. You see a path leading north and a river to the east. Do you want to go NORTH or EAST? (type 'north' or 'east'): ")
if choice1.lower() == "north":
    print("You walk north and find a cabin and a cave.")
    choice2 = input("Do you want to enter the CABIN or CAVE? (type 'cabin' or 'cave'): ")
    if choice2.lower() == "cabin":
        print("You enter the cabin and find it's full of treasure. You win!")
    elif choice2.lower() == "cave":
        print("You enter the cave and met a hungry bear. Game over!")
    else:
        print("Invalid choice.")
elif choice1.lower() == "east":
    print("You walk east and find a river. You can either try to cross it or follow it downstream.")
    choice2 = input("Do you want to CROSS the river or FOLLOW it downstream? (type 'cross' or 'follow'): ")
    if choice2.lower() == "cross":
        print("You try to cross the river but get swept away by the current. Game over!")
    elif choice2.lower() == "follow":
        print("You follow the river downstream and find a small village. You are safe!")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice")