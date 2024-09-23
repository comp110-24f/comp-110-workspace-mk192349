"""Here is where I will carry out the Chardle excercise"""

__author__ = "730796945"


def input_word() -> str:
    """Prompts the user to enter a 5-character word and exits if invalid."""
    word = input("Enter a 5-character word: ")
    
    # checks if the word length is not 5
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        return ""  # will return an empty string if the input is invalid
    
    return word


def input_letter() -> str:
    """Prompts the user to enter a single character and exits if invalid."""
    letter = input("Enter a single character: ")
    
    # check if the letter length is not specifically 1
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        return ""  # will return an empty string if the input is invalid
    
    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is in the word, reports the indices, and counts occurrences."""
    print(f"Searching for {letter} in {word}")
    
    count = 0  # counter for the number of matches seen
    
    # will check each index of the word to see if the letter matches
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1
    
    # will print the final message based on the length
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    """Main function to call input functions and check for matches."""
    word = input_word()  # gets the 5-character word
    if word == "":       # if word is invalud, then exit function
        return
    
    letter = input_letter()  # enter the single letter
    if letter == "":         # if letter is invalid, then exit function
        return
    
    contains_char(word, letter)  # will check for the letter in the word


# the entry point for my program
if __name__ == "__main__":
    main()


