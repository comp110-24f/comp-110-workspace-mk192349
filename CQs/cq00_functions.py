"""CQ00 Writing Functions"""

__author__ = "730796945"


def mimic(message: str) -> str:
    """Returns the input message"""
    return message


def main() -> None:
    """Pulls together your functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
