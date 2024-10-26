def start_game():
    print("You are walking in a dark forest.")
    print("You feel anxious in the surrounding silence, and in front of you are two items: 'match' and 'flashlight'.")
    print("Which one do you choose?")
    print("Choices: Match (MATCH) / Flashlight (FLASHLIGHT)")

    choice = input("Please enter your choice: ").strip().lower()

    if choice == "match":
        match_scene()
    elif choice == "flashlight":
        flashlight_scene()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def match_scene():
    print("\nYou choose the match and light it.")
    print("For a moment, everything becomes bright, and a huge grizzly appears in front of you.")
    print("What will you do?")
    print("Choices: Run (RUN) / Hide (HIDE) / Fight (FIGHT)")

    choice = input("Please enter your choice: ").strip().lower()

    if choice == "run":
        print("\nYou try to run away but are brought back to the starting point.")
        print("Protagonist: 'Running is useless. I am within you.'")
        game_over(dark_power=True)  # Game over due to dark power
    elif choice == "hide":
        print("\nYou hide behind a tree.")
        print("The grizzly leaves, and the protagonist lets out a chilling laugh.")
        print("Protagonist: 'Hiding won't let you escape. Your fate is tied to me.'")
        game_over(dark_power=True)  # Game over due to dark power
    elif choice == "fight":
        print("\nYou confront the grizzly.")
        print("The grizzly falls, and the protagonist says: 'You have only postponed your inevitable fate.'")
        game_continue()  # Continue the game
    else:
        print("Invalid choice. Please try again.")
        match_scene()

def flashlight_scene():
    print("\nYou choose the flashlight and shine it.")
    print("The path becomes bright, but eerie sounds echo around you.")
    print("Protagonist: 'Something is calling me. I must move forward.'")
    print("What will you do?")
    print("Choices: Follow the path (FOLLOW) / Look for a tree (LOOK)")

    choice = input("Please enter your choice: ").strip().lower()

    if choice == "follow":
        print("\nAs you follow the path, you encounter various adventures.")
        print("Gloomy shadows envelop you, and spirits of those you once hurt appear.")
        game_over(dark_power=True)  # Game over due to dark power
    elif choice == "look":
        print("\nYou search for a tree.")
        print("In that moment, you hear the protagonist's whisper.")
        print("Protagonist: 'My past is beautiful, but it does not bind me.'")
        game_over(dark_power=True)  # Game over due to dark power
    else:
        print("Invalid choice. Please try again.")
        flashlight_scene()

def game_over(dark_power=False):
    print("\nGame Over.")
    if dark_power:
        print("The weight of darkness envelops you.")
        print("Protagonist: 'You helped me regain my power. Now, I will dominate you.'")
    else:
        print("You need to find a way to escape this forest, but you cannot. You always return to the same place.")

    print("Do you want to end the nightmare? (yes/no)")

    choice = input("Please enter your choice: ").strip().lower()
    if choice == "yes":
        print("You decide to end the nightmare.")
        ending_scene()
    elif choice == "no":
        print("You choose to continue the nightmare.")
        start_game()  # Restart the game
    else:
        print("Invalid choice. Please try again.")
        game_over(dark_power)

def game_continue():
    print("\nAs you continue your journey, the darkness within you awakens.")
    print("As you progress through the forest, you begin to notice the protagonist's evil.")
    print("What will you do next?")
    print("Choices: Search for the truth (SEARCH) / Embrace the darkness (EMBRACE)")

    choice = input("Please enter your choice: ").strip().lower()

    if choice == "search":
        print("\nYou search for the truth about the protagonist's dark power.")
        print("It becomes clear that the protagonist was trying to regain power through you!")
        ending_scene()  # Proceed to ending scene
    elif choice == "embrace":
        print("\nYou embrace the darkness and become fully controlled by the protagonist.")
        print("A cold laugh echoes through the forest.")
        game_over(dark_power=True)  # Game over due to dark power
    else:
        print("Invalid choice. Please try again.")
        game_continue()

def ending_scene():
    print("\nYou decide to choose self-sacrifice to end the protagonist's evil.")
    print("Protagonist's inner voice: 'As long as I live within you, my darkness will never fade.'")
    
    print("\nThe final confrontation approaches.")
    print("You choose to kill the protagonist.")
    print("You understand this is the only way.")
    
    print("By choosing suicide, both the protagonist and you die, and the dark power vanishes.")
    print("This brings a moment of peace to the world.")
    
    print("\nThe spirit of the protagonist is staring at you.")

# Start the game
start_game()

