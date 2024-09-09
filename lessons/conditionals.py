"""Practicing my conditionals."""


def check_first_letter(word: str, letter: str) -> str:
    """will return bool value based on result"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))