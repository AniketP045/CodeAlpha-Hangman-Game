import random
from colorama import init

def main():
    # Initialize colorama
    init()

    # Welcome message with ANSI color codes
    welcome = [
        '\033[1;37mWelcome to \033[1;4m\033[1;31mHangman\033[0m\033[1;37m! You must try to guess the given word',
        'letter by letter before you run out of your ten attempts.',
        'A correct guess does not use up your attempts. \033[1;33m\033[1mGood luck!\033[0m'
    ]

    for line in welcome:
        print(line)

    # List of words
    word_list = ["python", "developer", "keyboard", "laptop", "hangman"]
    chosen_word = random.choice(word_list)
    word_guessed = ["-" for _ in chosen_word]
    guessed_letters = []
    attempts = 10

    while attempts > 0 and "-" in word_guessed:
        print("\033[1;31m\nAttempts Remaining:", attempts)
        print("\033[1;34mWord:", " ".join(word_guessed))
        print("\033[1;36mGuessed Letters:", ", ".join(guessed_letters))

        # Get input
        try:
            player_guess = input("\033[1;37m\nType in a letter: ").lower()
        except:
            print("That is not valid input. Please try again.")
            continue

        # Input validation
        if len(player_guess) != 1 or not player_guess.isalpha():
            print("\033[1;33mPlease enter only a single letter.")
            continue

        if player_guess in guessed_letters:
            print("\033[1;33mYou've already guessed that letter.")
            continue

        guessed_letters.append(player_guess)

        # Correct guess
        if player_guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == player_guess:
                    word_guessed[index] = player_guess
            print("\033[1;32mCorrect!")
        else:
            attempts -= 1
            print("\033[1;31mWrong guess.")

    # End of game
    if "-" not in word_guessed:
        print("\n\033[1;4m\033[1;32mCongratulations\033[0m\033[1;37m! You guessed the word:", chosen_word)
    else:
        print("\n\033[1;4m\033[1;31mYou lose\033[0m\033[1;37m! The word was:", chosen_word)

    print("\nThanks for playing Hangman!\n")

if __name__ == "__main__":
    main()
