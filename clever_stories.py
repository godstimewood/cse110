# Added new features: the user can now choose a place and a friend's name to include in the story, making it more interactive and personalized.
# Clever Stories - Interactive Mad Libs Game

def main():
    # Prompt user for inputs
    print("Please enter the following:\n")
    adjective = input("adjective: ")
    animal = input("animal: ")
    verb1 = input("verb: ")
    exclamation = input("exclamation: ").capitalize()
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    place = input("place: ")
    # Ask the user for a friend's name to add to the story
    friend = input("friend's name: ").capitalize()

    # Print the story with user inputs
    print("\nYour story is:\n")
    print(f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway at {place}. \"{exclamation}!\" I yelled. My friend {friend} was with me. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.")

# Call the main function to run the game
if __name__ == "__main__":
    main()