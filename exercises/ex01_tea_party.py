"""Here is where I will carry out the tea party excercise"""

___author___ = "730796945"


def main_planner(guests: int) -> None:
    """this is the entrypoint of my program"""
    teabag_num: int = tea_bags(guests)
    treat_num: int = treats(guests)
    total_cost: float = cost(teabag_num, treat_num)
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", teabag_num)
    print("Treats:", treat_num)
    print("Cost: $" + str(total_cost))
    # "str" + str(total_cost) value allows $ to be connected to total_cost


def tea_bags(people: int) -> int:
    """this will see the amount of tea bags needed for the party based on guests"""
    return people * 2


# will return number of tea bags needed based on number of guests


def treats(people: int) -> int:
    """this function will calculate the amount of treats based on guests"""
    tea_count = tea_bags(people=people)
    treat_count = tea_count * 1.5
    return int(treat_count)


# got more practice and understanding with using arguments


def cost(tea_count: int, treat_count: int) -> float:
    """this will return the total cost of the tea bags and treats combined"""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


# will reflect the cost based on the number of tea bags and treats needed


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
