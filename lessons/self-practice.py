"""here is where I will practice writing functions"""

__author__ = "730796945"


def get_weather_report() -> str:
    """will utilize this to determine weather report"""
    weather = str(input("What is the weather? "))

    if weather == "rainy" or weather == "cold":
        print("bring a jacket")
    else:
        if weather == "hot":
            print("Keep cool out there!")
        else:
            print("I dont recognize this weather")
            return weather
        

get_weather_report()





