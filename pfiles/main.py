import pandas as pd
import pyfiglet as pyf
from Designer.ForeGroundColor import *
from ascii_magic import AsciiArt

welcomeMessage = "Welcome  to  Astral  Express!!"  # The welcome message
GameExit = False  # Game's exit status
Line = "*"*70

# Main menu items
mainMenu = {1: "New game",
            2: "Continue",
            3: "Exit"
            }

# State of game
states = {
    "CurrentGalaxy": "",
    "CurrentSystem": "",
    "CurrentPlanet": "",
}


# Default paths
defaults = {
    "NewStartPoint": "~//Desktop//galaxy-pro//csvs//galaxy.csv",
    "mainPath": "~//Desktop//galaxy-pro//csvs//",
    "mainPathSystems": "~//Desktop//galaxy-pro//csvs//systems//system",
    "mainPathPlanets": "~//Desktop//galaxy-pro//csvs//systems//planets//system",
    "LastEndingPoint": ""
}


# To decorate the DataFrame output
def df_deco(df):
    """
    Decorates the input DataFrame.
    :param df: The DataFrame to be decorated.
    :return: The Decorated output
    """
    print(yellow(Line))
    for i in range(len(df.index)):
        row = f"{i+1}:{df.iloc[i,1]}"
        spacing = (68-len(row))//2
        print(yellow(f"*{' '*spacing}{row}{' '*spacing}*"))
    print(yellow(Line))


# To output decorated description
def you_are_on(dataframe, num: int):
    """
    Output a decorated description of the users choice.
    :param dataframe: The DataFrame holding the description
    :param num: The index number of element to be described
    :return: An output of the decorated description
    """
    print(yellowgreen("\n"+"#"*200))
    print(yellowgreen(f"{pyf.figlet_format(dataframe.iloc[num-1,1])}\n\n{dataframe.iloc[num-1,2]}"))
    print(yellowgreen("#"*200+"\n\n"))


# To exit the game
def exit_game(*args):
    """
    Exits the game when exit status is changed to `True`.
    :return:
    """
    pass


# The main function that runs recursively for the game to run.
def compact(num: str, typ: int):
    """
    The main function that runs recursively for the game to run.
    :param num: `int` value for the `states`
    :param typ: `int` value for galaxy, system or planet respectively
    :return:
    """
    new_num = ""
    df = ""
    if typ == 0:
        df = pd.read_csv(defaults["NewStartPoint"])
        df_deco(df)
        new_num = input("Choose the Galaxy you want to visit or type 0 to go back--> ")
        if new_num == "0":
            show_main_menu()
            return
        else:
            states["CurrentGalaxy"] = new_num
    elif typ == 1:
        df = pd.read_csv(f"{defaults['mainPathSystems']}{states['CurrentGalaxy']}.csv")
        df_deco(df)
        new_num = input("Choose the system want to visit or type 0 to go back--> ")
        states["CurrentSystem"] = new_num
    elif typ >= 2:
        typ = 2
        df = pd.read_csv(f"{defaults['mainPathPlanets']}{states['CurrentGalaxy']}//planets{states['CurrentSystem']}.csv")
        df_deco(df)
        new_num = input("Choose the planet want to visit or type 0 to go back--> ")
        states['CurrentPlanet'] = new_num

    if new_num == "0":
        compact(num, typ-1)
    elif int(new_num) <= len(df.index):
        you_are_on(df, int(new_num))
        compact(new_num, typ+1)
    else:
        print(red("Please enter a valid input!\n"))
        compact(num, typ)


# To continue
def game_continue(a: str, b: int):
    compact(a, b)


# To display the main menu
def show_main_menu():
    AsciiArt.from_image('./giphy.gif').to_terminal(columns=150, width_ratio=2.75)
    print(cyan1(pyf.figlet_format(welcomeMessage)))
    print(cyan1(Line))
    for i in mainMenu.keys():
        men_str = f"{i}:{mainMenu[i]}"
        s_len = (66-len(men_str))//2
        print(cyan1("**"+" "*s_len+men_str+" "*s_len+"**"))
    print(cyan1(Line))
    user_input = int(input("Enter--> "))
    print()
    if user_input in mainMenu.keys():
        funcs[user_input]("0", 0)
    else:
        print(red("\nPlease enter a valid input!\n"))
        show_main_menu()


# Main menu functions
funcs = {1: compact,
         2: game_continue,
         3: exit_game}

# Main program
if __name__ == "__main__":
    show_main_menu()
