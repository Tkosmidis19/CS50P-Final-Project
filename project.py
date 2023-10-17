# imports section
import sys
import random
from os import system, name
from art import text2art
from tabulate import tabulate


# Plates to be served to the King
Spicy = {
    "Curry": random.randint(1, 4),
    "Chicken Masala": random.randint(1, 4),
    "Chili Pepper Soup": random.randint(1, 4),
}
Sweet = {
    "Raspberry Cake": random.randint(1, 4),
    "Pudding": random.randint(1, 4),
    "Honey Biscuits": random.randint(1, 4)
}
Savoury = {
    "Meatballs": random.randint(1, 4),
    "Sausage": random.randint(1, 4),
    "Steak": random.randint(1, 4),
}
GAME = True

# Main function
def main():
    while GAME:
        clear()
        input("Welcome to :")
        title_screen()
        input()
        input("You will be tasked with cooking for the King of Games")
        input("Be careful what you bring him or he may punish you!")
        king = King(random.randint(1, 9), 1)
        if play_game():
            while True:
                title_screen()
                status = display_king_status(king.hunger)
                if check_game(status) == "Win":
                    play_ = game_over("Win")
                    if play_ == "no":
                        clear()
                        sys.exit("See you again!")
                    if play_ == "yes":
                        print("Time rewinds!")
                        break
                elif check_game(status) == "Loss":
                    play_ = game_over("Loss")
                    if play_ == "no":
                        clear()
                        sys.exit("See you again!")
                    if play_ == "yes":
                        print("Time rewinds!")
                        break
                print(status)
                input()
                clear()
                title_screen()
                print("")
                print(feed_status(king.attitude))
                input()
                plate = feed()
                king.hunger += attitude_check(king.attitude, plate)
                king.attitude = random.randint(1, 9)

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Making a class to store the two attributes that will be used.
class King:
    def __init__(self, attitude, hunger):
        self.attitude = attitude
        self.hunger = hunger

# Print on screen the title of the game
def title_screen():
    clear()
    print(text2art("The King's Troubles!"))

# Ask the user if they want to play
def play_game():
    while True:
        try:
            play = input("Would you like to play?(Y/N) ").lower().strip()
            if play == "y":
                clear()
                return True
            elif play == "n":
                sys.exit("The game will now exit.")
            else:
                raise ValueError
        except ValueError:
            print("Answer with Y or N")

# Print to the screen the King's status
def display_king_status(hunger):
    if 1 <= int(hunger) <= 3:
        return "The King is very hungry!"
    if 4 <= int(hunger) <= 6:
        return "The King is feeling good"
    if 7 <= int(hunger) <= 9:
        return "The King is nearly satisfied!"
    if int(hunger) >= 10:
        flag = "Done"
        return flag
    if int(hunger) <= 0:
        flag = "Over"
        return flag

# Check if the game ends in a win or loss
def check_game(status):
    if status == "Done":
        flag = "Win"
        return flag
    if status == "Over":
        flag = "Loss"
        return flag

# Check the King's desired meal
def feed_status(attitude):
    title_screen()
    print("")
    if 1 <= attitude <= 3:
        return "My royal taste buds require a Juicy Meal!"
    if 4 <= attitude <= 6:
        return "Right now I desire to taste something with strong flavor."
    if 7 <= attitude <= 9:
        return "Prepare for me something sugary I need energy!"
# Check if the plate is the one the King asked for
def attitude_check(attitude, plate):
    title_screen()
    if 1 <= attitude <= 3 and plate in Savoury.keys():
        return Savoury[plate]
    if 4 <= attitude <= 6 and plate in Spicy.keys():
        return Spicy[plate]
    if 7 <= attitude <= 9 and plate in Sweet.keys():
        return Sweet[plate]
    if 1 <= attitude <= 3 and plate not in Savoury.keys():
        input("What is this?Are you deaf cook?")
        return -random.randint(1, 3)
    if 4 <= attitude <= 6 and plate not in Spicy.keys():
        input("What?This food is not what I asked!")
        return -random.randint(1, 4)
    if 7 <= attitude <= 9 and plate not in Sweet.keys():
        input("Maybe this was too much to ask of you.")
        return -random.randint(1, 4)

# Decide which plate to serve to the King
def feed():
    input("What would you like to cook for the king?")
    print("")
    display_food()
    print("")
    while True:
        try:
            plate = input("Make : ")
            if check_plate(plate):
                return plate
            else:
                raise ValueError
        except ValueError:
            print("Incorrect plate")

# Check if the plate is servable
def check_plate(food):
    if food in Spicy.keys() or food in Savoury.keys() or food in Sweet.keys():
        return True

# Display the available plates
def display_food():
    print(
        tabulate(
            {
                "Spicy": ["Curry", "Chicken Masala", "Chili Pepper Soup"],
                "Sweet": ["Raspberry Cake", "Pudding", "Honey Biscuits"],
                "Savoury": ["Meatballs", "Sausage", "Steak"],
            },
            headers="keys",
        )
    )

# End the game depending on the outcome
def game_over(flag):
    if flag == "Loss":
        title_screen()
        print(
            """What manner of Cook are you?Begone from my sight,
            you are banished!"""
        )
        print("")
        input("The King was unsatisfied with your performance.")
        print("")
        input("You have been sentenced to life in jail")
        print("")
        input(
            """As you enter your cell you find that you are in a room
with two doors the left one takes you to right before you started 
the day and the right one takes you home"""
        )
        print("Go through which door? (Left or Right)")
        print("")
        while True:
            try:
                door = input(":").lower()
                if door == "left":
                    flag = "yes"
                elif door == "right":
                    flag = "no"
                else:
                    raise ValueError
                return flag
            except ValueError:
                print("Please pick a door.")
    if flag == "Win":
        input("Congratulations Cook!You have satisfied me!")
        title_screen()
        input("The King was satisfied with your performance.")
        print("")
        input(
            """As you exit the castle you find yourself in front of
two doors.The left one takes you to right before you started 
the day and the right one takes you home"""
        )
        print("")
        print("Go through which door? (Left or Right)")
        print("")
        while True:
            try:
                door = input(":").lower()
                if door == "left":
                    flag = "yes"
                elif door == "right":
                    flag = "no"
                else:
                    raise ValueError
                return flag
            except ValueError:
                print("Please pick a door.")


if __name__ == "__main__":
    main()
