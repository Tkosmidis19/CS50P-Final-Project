# The King's Troubles
## Video Demo:  <[Video](https://www.youtube.com/watch?v=5h1sTPLkcfE)>
## Description:
This is my final project for CS50P.It is a simple game where the player
is tasked with serving the King of Games food from a pre-determined list.
If the King likes the plate he will grow more satisfied,if he does not his
attitude will lessen.If the player fails to serve the correct type of plate
many times then the King will punish the player by sending them to jail.
## Libraries:
[RANDOM](https://docs.python.org/3/library/random.html):This module allows for the generation of semi-random numbers.
[ART](https://pypi.org/project/art/):This module allows for the conversion of text to ASCII art.
[TABULATE](https://pypi.org/project/tabulate/):This module allows for printing tables in a more readable way.
To install the libraries that are not installed by default(Art and Tabulate) simply execute the command:
>pip install -r requirements.txt
#### Execution:
To start the game write the command:
>python project.py

After which you will be welcomed to the title screen.
![Title_screen](https://github.com/code50/108869208/assets/108869208/9f2867a8-8c8d-485e-b7ed-dd477bc9e839)


Press Enter to progress through the game.

## Functions:
The game consists of 12 Functions(including main) and 1 Class as per the below explanations.

#### King class:
A simple class that is used to store the attributes that control the outcome and current
situation of the game.

#### clear() function:
A function that was created to clear the screen.It is used instead of os.system('cls) so that
the game can be run on all Operating Systems.

#### title_screen() function:
By using the text2art function of the art module,print the game's title on the screen
after clearing previous text on screen.

#### play_game() function:
Function called at the start of the game asking the user if they would like to play.
If the answer N the game exits with sys.exit()

#### display_king_status() function:
Function that receives a number as an argumentt and determines the King's hunger status
then prints it to the screen.If the King's hunger is over 10 or less than 10
the function returns a string that gets passed into the check_game() function that
determines whether the game is over or not.

#### check_game_status() function:
Function that is run after every round to determine if the player has won or lost.
Takes in as an argument the status variable that is generated when display_king_status()
is run.

#### feed_status() function:
A function that takes in as an argument the King's attitude and prints to the screen
the desired type of meal he wants to be served.

#### attitude_check() function:
A function that checks whether the player chose a correct plate and depending on
the choice increases or decreases the King's attitude.

#### feed() function:
The function that handles the serving of the plates to the King.

#### check_plate() function:
A function that checks the user's input to see if it is a valid plate.

#### display_food() function:
Prints the servable plates to the screen.

#### game_over() function:
Takes in the flag variable as an argument and proceeds to end the game
depending on the value of the flag variable.At the end also asks the player
if they want to play again.
