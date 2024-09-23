"""Here is where I will carry out the while loops challenge question"""

__author__ = "730796945"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # count of occurences
    count_idx: int = 0  # will go through the phrase given
    
    while count_idx < len(phrase):
       
        if phrase[count_idx] == search_char:
            count += 1  # will see how many times search_char appears
        count_idx += 1  # will tell index to go to next character in phrase

    print(f'phrase = "{phrase}", search_char = "{search_char}"')
    # prints phrase and character being searched
    return count


print(num_instances(phrase="fortnitisawesome", search_char="e"))
# will print the amount of times a character appears in the given phrase










