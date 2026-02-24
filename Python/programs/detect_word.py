"""Detect Lowercase Words


Create a function detect_lowercase_words that:

Reads one line at a time using the input function.
Checks if the word contains any capital letters:
If not — it prints {word} detected, where word is the word entered by the user.
Continues running until it reads the word exit.
💡 Use a while True loop and the break statement.

"""
def detect_lowercase_words() -> None:
    while True:
        word = input()
        lower_word = word.lower()
        if word == "exit":
            break
        else:
            if word == lower_word:
                print(f"{word} Word Detected!")


detect_lowercase_words()

