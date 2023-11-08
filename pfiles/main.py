import pandas as pd
import pyfiglet as pyf
from Designer.ForeGroundColor import *
from ascii_magic import AsciiArt
import matplotlib.pyplot as plt

welcomeMessage = "Welcome  to  Astral  Express!!"  # The welcome message
GameExit = False  # Game's exit status
Line = "*"*70  # Just for formatting

# Main menu items
mainMenu = {1: "Start the game",
            2: "Customize your world in this game!",
            3: "Visualize",
            4: "How to play?",
            5: "Exit"
            }

# State of game
states = {
    "CurrentGalaxy": "",
    "CurrentSystem": "",
    "CurrentPlanet": ""}


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
    Decorates the input DataFrame to print it as a menu.
    :param df: The DataFrame to be decorated.
    :return: The Decorated output
    """
    print(yellow(Line))
    for i in range(len(df.index)):  # Iterating through the length of provided DataFrame
        row = f"{i+1}:{df.iloc[i,1]}"  # Creating contents of each row
        spacing = (68-len(row))//2  # Adding even spacing
        print(yellow(f"*{' '*spacing}{row}{' '*spacing}*"))  # Printing each formatted row
    print(yellow(Line))

    return 0


# To output decorated description
def you_are_on(dataframe, num: int):
    """
    Output a decorated description of the users choice.
    :param dataframe: The DataFrame holding the description
    :param num: The index number of element to be described
    :return: An output of the decorated description
    """
    print(yellowgreen("\n"+"#"*200))
    # Decorating and displaying the name of the DataFrame item and description with provided DataFrame end index no.
    print(yellowgreen(f"{pyf.figlet_format(dataframe.iloc[num-1,1])}\n\n{dataframe.iloc[num-1,2]}"))
    print(yellowgreen("#"*200+"\n\n"))
    return 0


# To exit the game
def exit_game():
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
    new_num = ""  # Variable holding the choices being made
    df = ""  # Variable for holding the DataFrame at each step

    # Checking Where the player is 0: Galaxy, 1: systems 2: planets and assigning the appropriate variables for same
    if typ == 0:  # Condition where player is selecting galaxies
        df = pd.read_csv(defaults["NewStartPoint"])
        df_deco(df)
        new_num = input("Choose the Galaxy you want to visit or type 0 to go back--> ")
        if new_num == "0":  # If player chooses the is taken back to the main menu
            show_main_menu()
            return 0
        else:
            states["CurrentGalaxy"] = new_num
    elif typ == 1:  # condition where player is choosing the system
        df = pd.read_csv(f"{defaults['mainPathSystems']}{states['CurrentGalaxy']}.csv")
        df_deco(df)
        new_num = input("Choose the system want to visit or type 0 to go back--> ")
        states["CurrentSystem"] = new_num
    elif typ >= 2:  # Condition where player is choosing planets
        typ = 2
        df = pd.read_csv(f""""{defaults['mainPathPlanets']}{states['CurrentGalaxy']}//planets{states['CurrentSystem']}\
    .csv""")
        df_deco(df)
        new_num = input("Choose the planet want to visit or type 0 to go back--> ")
        states['CurrentPlanet'] = new_num

    # Checking what input has been given and performing actions based on the same
    if new_num == "0":
        compact(num, typ-1)
    elif int(new_num) <= len(df.index):
        you_are_on(df, int(new_num))
        compact(new_num, typ+1)
    else:
        print(red("Please enter a valid input!\n"))
        compact(num, typ)

    return 0


# To have numeric visualization of number of planets in each galaxy
def visualize():
    """
    This function will be used to visualize number of planets in a system
    :return: A graphical representation of all the planets in chosen galaxy
    """
    # Variable holding the value for galaxy to be visualized
    flow = input("""What do you want the visual of the Milky Way galaxy Planets (m/M) or Outer Planets (o/O) or your \
planets (c/C)?""")
    main = {
        "m": 1, "o": 2, "c": 3
    }
    # Flow control to manage which galaxy the planets has to be selected from
    if flow.casefold() in main.keys():
        df = pd.read_csv(f"{defaults['mainPathSystems']}{main[flow.lower()]}.csv")
        sys = main[flow.lower()]
    else:
        visualize()
        return 0

    x = []  # Values for x-axis (The systems)
    y = []  # Values for y-axis (The number of planets)

    # Adding the needed values (systems) to y
    for i in range(1, len(df.index)+1):
        dfi = pd.read_csv(f"{defaults['mainPathPlanets']}{sys}/planets{i}.csv")
        y.append(len(dfi.index))

    # Adding the needed values (The number of planets) to x
    for i in range(len(df.index)):
        dfi = pd.read_csv(f"{defaults['mainPathSystems']}{sys}.csv")
        x.append(dfi.iloc[i, 1])

    # Plotting the graph
    plt.bar(x, y)
    plt.xlabel("Galaxies \u279c")
    plt.ylabel("Number of planets \u279c")
    plt.show()
    show_main_menu()

    return 0


# A function that will help players navigate through the game
def game_help():
    """
    This function is about telling players how to navigate through the game.
    :return:
    """
    print(cyan1(pyf.figlet_format("HELP!!!")))
    print(cyan("Use the numbers from the displayed menu to navigate through the space.\n", bg="blue"))
    input(cyan1("Press any key to continue-->"))
    show_main_menu()

    return 0


# To display the main menu
def show_main_menu():
    """
    This function manages the landing menu of the game
    :return:
    """

    # To print a display image to the terminal
    AsciiArt.from_image('./giphy.gif').to_terminal(columns=150, width_ratio=2.75)
    print(cyan1(pyf.figlet_format(welcomeMessage)))
    print(cyan1(Line))

    # Printing each item of the main menu
    for i in mainMenu.keys():
        men_str = f"{i}:{mainMenu[i]}"
        s_len = (66-len(men_str))//2
        print(cyan1("**"+" "*s_len+men_str+" "*s_len+"**"))
    print(cyan1(Line))
    user_input = int(input("Enter--> "))
    print()

    # Running the selected function
    if user_input in mainMenu.keys():
        if user_input == 1:
            funcs[1]("0", 0)
        else:
            funcs[user_input]()
    else:
        print(red("\nPlease enter a valid input!\n"))
        show_main_menu()

    return 0


# Function to customize the world inside the game
def custom():
    """
    This function manages customization of players' items.
    :return:
    """

    # Taking choice from players about what they want to edit
    choice = input("Do you want to add/del a system(s/S) or planets(p/P)?")
    name = ""
    df = ""
    i = 0

    # Assigning variables with proper values according to the choice of the player
    if choice.casefold() == "s":
        name = "System"
        df = pd.read_csv(f"{defaults['mainPathSystems']}3.csv")
    elif choice.casefold() == "p":
        df = pd.read_csv(f"{defaults['mainPathSystems']}3.csv")
        print(df['sysname'].to_string(index=False))
        gname = input("Enter the Galaxy name you want to add planet in: ")
        i = len(df[df['sysname'] == gname].index)
        df = pd.read_csv(f"{defaults['mainPathPlanets']}3/planets{i}.csv")
        print(df["planet"].to_string(index=False))
        name = "Planet"
    else:
        custom()
        return 0

    n = input(f"Enter the name of your {name}: ")

    # Asking for the action they want to perform with their choice
    while True:
        ad = input(f"Do you want to add (a/A) or delete(d/D) it?")
        if ad.casefold() == "a":
            d = input(f"Enter a description for {n}: ")
            break
        elif ad.casefold() == "d":
            break
        else:
            pass

    length = len(df)
    d = ""

    # Editing database according to the action
    if choice.casefold() == 's':
        if ad.casefold() == "d":
            df = df.drop(df[df["sysname"] == n].index)
        else:
            df.loc[length + 1] = [300 + length, f'{n}', f"{d}"]
        df.to_csv(f"{defaults['mainPathSystems']}3.csv", index=False)
        print("System edited! Check it out...")
    elif choice.casefold() == 'p':
        if ad.casefold() == "d":
            df = df.drop(df[df["planet"] == n].index)
        else:
            df.loc[length + 1] = [30000 + i*100 + length, f'{n}', f"{d}"]
        df.to_csv(f"{defaults['mainPathPlanets']}3/planets{i}.csv", index=False)
        print("Planet edited! Check it out...")
    show_main_menu()

    return 0


# Main menu functions
funcs = {1: compact,
         2: custom,
         3: visualize,
         4: game_help,
         5: exit_game}

# Main program
if __name__ == "__main__":
    show_main_menu()
