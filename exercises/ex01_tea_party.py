"""Here is where I will carry out the tea party excercise"""

__author__ = "730796945"


def main_planner(guests: int) -> None:
    """this is the entrypoint of my program"""

    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # "str" + str(total_cost) value allows $ to be connected to total_cost function
    # each print function utilizes arguments regarding each function and guest amount
    # the total value of each function is calculated, forming a total price 


def tea_bags(people: int) -> int:
    """this will see the amount of tea bags needed for the party based on guests"""
    return people * 2
# multiplies people * 2 because each person will drink two cups of tea (tea bags)
# simplest function created, extremely simple return value


def treats(people: int) -> int:
    """this function will calculate the amount of treats based on teas guests drink"""
    return int(tea_bags(people=people) * 1.5)
# each guest will drink two cups of tea, for each cup of tea that is 1.5 treats eaten
# return value is dependent on tea_bag function * 1.5
# number of a guests is a keyword argument (people=people)


def cost(tea_count: int, treat_count: int) -> float:
    """this will return the total cost of the tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)
# will reflect the cost based on the number of tea bags and treats needed
# function return value is dependent on the tea_count parameter, treat_count parameter
# parameter 1 is multiplied by 0.5 because each tea bag is $0.50
# parameter 2 is multiplied by 0.75 because each treat is $0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# makes the program runnable 
# can go to the "Run" tab of my program and be prompted for a guest count
# can then see the function output
# cannot be called before main_planner function because it will not be able to find it