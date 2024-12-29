import random  # Importing the random module to select a random movie

def play_game():
    # Get the user's name
    name = input("What is your name? ")  # Prompt the user for their name
    print("Good luck!", name)  # Display a friendly greeting

    # Read the movies from movies.txt
    try:
        # Open the file in read mode and read all lines into a list
        with open(r"Its_a_movie_guessing_game\movies.txt", "r") as file:
            movies = [line.strip() for line in file.readlines()]  # Strip newlines and spaces
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: The file 'movies.txt' was not found.")
        return  # Exit the function gracefully

    # Select a random movie from the list
    movie = random.choice(movies).lower()  # Convert to lowercase for case-insensitive matching
    print("Guess the Movie")  # Prompt the user to guess the movie

    # Initialize variables
    guesses = ''  # String to keep track of all guesses made by the user
    turns = 15  # Number of turns or chances the user has

    # Main game loop
    while turns > 0:
        failed = 0  # Counter to track the number of characters yet to be guessed

        # Display the current state of the movie
        for char in movie:
            if char in guesses or char == " ":  # Show guessed characters and spaces
                print(char, end=" ")  # Print the character
            else:
                print("_", end=" ")  # Print an underscore for unguessed characters
                failed += 1  # Increment the failed counter

        print()  # Print a newline after displaying the movie

        # Check if all characters have been guessed
        if failed == 0:
            print("You Win!")  # Congratulate the user
            print("The movie is:", movie)  # Display the full movie title
            break  # Exit the loop as the user has won

        # Prompt the user to guess a character
        guess = input("Guess a character: ").lower()  # Convert input to lowercase for consistency

        # Add the guess to the list of guessed characters
        guesses += guess

        # Check if the guess is incorrect
        if guess not in movie:
            turns -= 1  # Decrement the number of turns
            print("Wrong guess!")  # Inform the user
            print("You have", turns, "more guesses.")  # Display remaining turns

        # Check if the user has no turns left
        if turns == 0:
            print("You Lose! The movie was:", movie)  # Reveal the movie title

# Main loop for replaying the game
while True:
    play_game()  # Call the function to start the game
    # Ask the user if they want to play again
    retry = input("Do you want to play again? (y/n): ").lower()
    if retry != 'y':
        print("Thank you for playing! Goodbye!")
        break  # Exit the loop if the user doesn't want to play again
