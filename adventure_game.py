# Adventure Game Code Snippet
# This is a simple text-based adventure game where the player makes choices to navigate through a story.
# I showed this game to my friends, and they enjoyed it. They found it engaging and fun.

choice1 = input("You wake up in a dark forest. You see a path leading north, a river to the east, and a mountain to the west. Do you want to go NORTH, EAST, or WEST? (type 'north', 'east', or 'west'): ")
if choice1.lower() == "north":
    print("You walk north and find a cabin, a cave, and a mysterious tree.")
    choice2 = input("Do you want to enter the CABIN, explore the CAVE, climb the TREE, or search the BUSHES? (type 'cabin', 'cave', 'tree', or 'bushes'): ")
    if choice2.lower() == "cabin":
        print("You enter the cabin and find a map, a locked chest, and a friendly cat.")
        choice3 = input("Do you want to FOLLOW the map, OPEN the chest, or PET the cat? (type 'follow', 'open', or 'pet'): ")
        if choice3.lower() == "follow":
            print("You follow the map and discover a beautiful garden full of magical flowers. You win!")
        elif choice3.lower() == "open":
            print("You open the chest and find a pile of gold coins. You win!")
        elif choice3.lower() == "pet":
            print("You pet the cat. It purrs and leads you to a secret passage out of the forest. You are safe!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "cave":
        print("You enter the cave and meet a hungry bear, a sleeping owl, and a sparkling stream.")
        choice3 = input("Do you want to RUN, OFFER food, TALK to the bear, WAKE the owl, or DRINK from the stream? (type 'run', 'offer', 'talk', 'wake', or 'drink'): ")
        if choice3.lower() == "run":
            print("You try to run, but the bear catches up. Game over!")
        elif choice3.lower() == "offer":
            print("You offer the bear some food from your bag. The bear is happy and shows you a hidden exit. You escape safely!")
        elif choice3.lower() == "talk":
            print("You talk to the bear. Surprisingly, it understands you and gives you a golden key. You win!")
        elif choice3.lower() == "wake":
            print("You wake the owl. It gives you wise advice and helps you find your way home. You are safe!")
        elif choice3.lower() == "drink":
            print("You drink from the stream and feel refreshed. Suddenly, you gain the ability to speak to animals. You win!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "tree":
        print("You climb the tree and find a nest with a sparkling egg, a telescope, and a mysterious rope.")
        choice3 = input("Do you want to TAKE the egg, USE the telescope, GRAB the rope, or LOOK around? (type 'take', 'use', 'grab', or 'look'): ")
        if choice3.lower() == "take":
            print("The egg hatches into a baby dragon! It becomes your friend and flies you to safety. You win!")
        elif choice3.lower() == "use":
            print("You use the telescope and spot a rescue team approaching. You are saved!")
        elif choice3.lower() == "grab":
            print("You grab the rope and swing to another tree, where you find a hidden treehouse full of treasure. You win!")
        elif choice3.lower() == "look":
            print("You look around and spot a hidden door in the tree. You enter and find a room full of treasure. You win!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "bushes":
        print("You search the bushes and find berries, a shiny coin, and a lost puppy.")
        choice3 = input("Do you want to EAT the berries, TAKE the coin, or HELP the puppy? (type 'eat', 'take', or 'help'): ")
        if choice3.lower() == "eat":
            print("The berries are delicious and give you energy to find your way home. You are safe!")
        elif choice3.lower() == "take":
            print("You take the coin and discover it's magical. It grants you a wish. You win!")
        elif choice3.lower() == "help":
            print("You help the puppy and it becomes your loyal companion. Together, you find a way out of the forest. You are safe!")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
elif choice1.lower() == "east":
    print("You walk east and find a river, a bridge, and a boat.")
    choice2 = input("Do you want to CROSS the river, FOLLOW it downstream, use the BRIDGE, or take the BOAT? (type 'cross', 'follow', 'bridge', or 'boat'): ")
    if choice2.lower() == "cross":
        print("You try to cross the river but get swept away by the current. Game over!")
    elif choice2.lower() == "follow":
        print("You follow the river downstream and find a small village, a waterfall, and a mysterious cave.")
        choice3 = input("Do you want to EXPLORE the village, REST at the inn, CLIMB the waterfall, or ENTER the cave? (type 'explore', 'rest', 'climb', or 'enter'): ")
        if choice3.lower() == "explore":
            print("You explore the village and find a festival in progress. You join the fun and make new friends. You win!")
        elif choice3.lower() == "rest":
            print("You rest at the inn and recover your strength. The villagers help you return home. You are safe!")
        elif choice3.lower() == "climb":
            print("You climb the waterfall and discover a hidden cave full of crystals. You win!")
        elif choice3.lower() == "enter":
            print("You enter the cave and find a wise old turtle who gives you advice and helps you get home. You are safe!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "bridge":
        print("You cross the bridge and meet a troll, a merchant, and a group of travelers.")
        choice3 = input("Do you want to TALK to the troll, TRADE with the merchant, or JOIN the travelers? (type 'talk', 'trade', or 'join'): ")
        if choice3.lower() == "talk":
            print("You talk to the troll and solve his riddle. He lets you pass and you find a treasure chest. You win!")
        elif choice3.lower() == "trade":
            print("You trade with the merchant and receive a magic potion. You use it to safely return home. You are safe!")
        elif choice3.lower() == "join":
            print("You join the travelers and embark on a new adventure. You make lifelong friends. You win!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "boat":
        print("You take the boat and sail down the river. You encounter a storm, a flock of birds, and a floating island.")
        choice3 = input("Do you want to WEATHER the storm, FOLLOW the birds, or EXPLORE the island? (type 'weather', 'follow', or 'explore'): ")
        if choice3.lower() == "weather":
            print("You weather the storm and reach a safe harbor. You are safe!")
        elif choice3.lower() == "follow":
            print("You follow the birds and they lead you to a magical land. You win!")
        elif choice3.lower() == "explore":
            print("You explore the island and find a hidden treasure. You win!")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
elif choice1.lower() == "west":
    print("You head west and approach a tall mountain. At its base, you find a cave, a rope bridge, and a mysterious door carved into the rock.")
    choice2 = input("Do you want to ENTER the cave, CROSS the rope bridge, OPEN the door, or CLIMB the mountain? (type 'cave', 'bridge', 'door', or 'climb'): ")
    if choice2.lower() == "cave":
        print("Inside the cave, you find glowing crystals, a sleeping dragon, and a pile of bones.")
        choice3 = input("Do you want to TAKE a crystal, WAKE the dragon, or SEARCH the bones? (type 'take', 'wake', or 'search'): ")
        if choice3.lower() == "take":
            print("You take a crystal and it lights your way out. You are safe!")
        elif choice3.lower() == "wake":
            print("The dragon wakes up and gives you a ride to the top of the mountain. You win!")
        elif choice3.lower() == "search":
            print("You search the bones and find a magic ring. You win!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "bridge":
        print("You cross the rope bridge and encounter a gusty wind, a flock of birds, and a treasure chest dangling from the bridge.")
        choice3 = input("Do you want to HOLD tight, FOLLOW the birds, or OPEN the chest? (type 'hold', 'follow', or 'open'): ")
        if choice3.lower() == "hold":
            print("You hold tight and make it safely across. You are safe!")
        elif choice3.lower() == "follow":
            print("You follow the birds and they lead you to a hidden valley full of fruit trees. You win!")
        elif choice3.lower() == "open":
            print("You open the chest and find a map to a secret cave. You win!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "door":
        print("You open the mysterious door and find a spiral staircase, a glowing orb, and a talking statue.")
        choice3 = input("Do you want to CLIMB the staircase, TOUCH the orb, or TALK to the statue? (type 'climb', 'touch', or 'talk'): ")
        if choice3.lower() == "climb":
            print("You climb the staircase and reach a lookout with a beautiful view. You are safe!")
        elif choice3.lower() == "touch":
            print("You touch the orb and are granted a wish. You win!")
        elif choice3.lower() == "talk":
            print("You talk to the statue and it gives you wise advice for your journey. You are safe!")
        else:
            print("Invalid choice.")
    elif choice2.lower() == "climb":
        print("You climb the mountain and find a nest of golden eggs, a flag, and a mysterious mist.")
        choice3 = input("Do you want to TAKE an egg, PLANT the flag, or ENTER the mist? (type 'take', 'plant', or 'enter'): ")
        if choice3.lower() == "take":
            print("You take a golden egg and it hatches into a phoenix. You win!")
        elif choice3.lower() == "plant":
            print("You plant the flag and claim the mountain as your own. You win!")
        elif choice3.lower() == "enter":
            print("You enter the mist and are transported to a magical kingdom. You win!")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice")