import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import random
import sys
from PIL import Image
from PIL import ImageTk


class RPSClass:
    """
    Definition of the RPS game with lifes
    """

    # Maximum number of lifes
    max_lifes = 3

    # Sizes of the icons
    icon_dx = 50
    icon_dy = 50

    def __init__(self):
        """
        Initialization of the variables and window
        """

        # result
        self.lifes_player = RPSClass.max_lifes
        self.lifes_cpu = RPSClass.max_lifes
        self.last_won = None
        self.answer = None

        # possible options and choices
        self.possible_options = ["rock", "paper", "scissors"]
        self.player_choice = None
        self.cpu_choice = None

        # Text options
        self.text = "Let's try!"
        self.color = "black"

        # Initialize the window method
        self.root = tk.Tk()
        self.initialize_tk_window()

        # Initialize text label and name labels
        self.text_label = tk.Label(self.root, text=self.text, bd=0, font=10, width=30, fg=self.color)
        self.text_label.grid(row=0, column=1)

        self.name_label = tk.Label(self.root, text="Player1", bg="green", font=10, fg="black")
        self.name_label.grid(row=1, column=0, pady=0)

        self.cpu_label = tk.Label(self.root, text="CPU", font=10, bg="red", fg="black")
        self.cpu_label.grid(row=1, column=2, pady=0)

        # Initialize progressbar
        self.player_life_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=100,
                                               maximum=RPSClass.max_lifes,
                                               value=self.lifes_player)
        self.player_life_bar.grid(row=2, column=0, pady=0)

        self.cpu_life_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=100,
                                            maximum=RPSClass.max_lifes,
                                            value=self.lifes_cpu)
        self.cpu_life_bar.grid(row=2, column=2, pady=0)

        # Images
        self.images_dict = {"paper": self.make_image("paper_icon.png", RPSClass.icon_dx, RPSClass.icon_dy),
                            "rock": self.make_image("rock_icon.png", RPSClass.icon_dx, RPSClass.icon_dy),
                            "scissors": self.make_image("scissor_icon.png", RPSClass.icon_dx, RPSClass.icon_dy),
                            "question": self.make_image("question_icon.png", RPSClass.icon_dx, RPSClass.icon_dy),
                            "vs": self.make_image("vs_icon.png", RPSClass.icon_dx, RPSClass.icon_dy)}

        # Buttons with the choice players made
        self.player_choice_icon = tk.Button(self.root, text="Your choice!", image=self.images_dict["question"])
        self.player_choice_icon.grid(row=3, column=0, pady=50)

        self.vs_icon = tk.Button(self.root, image=self.images_dict["vs"])
        self.vs_icon.grid(row=3, column=1, pady=50)

        self.cpu_choice_icon = tk.Button(self.root, text="Your opponent choice!", image=self.images_dict["question"])
        self.cpu_choice_icon.grid(row=3, column=2, pady=50)

        # buttons
        tk.Button(self.root, text="PAPER", width=10, bd=10, relief="raised",
                  command=lambda: self.game("paper")).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="ROCK", width=10, bd=10, relief="raised",
                  command=lambda: self.game("rock")).grid(row=4, column=1, pady=10)
        tk.Button(self.root, text="SCISSORS", width=10, bd=10, relief="raised",
                  command=lambda: self.game("scissors")).grid(row=4, column=2, pady=10)

        # menu
        self.menu = tk.Menu(self.root)
        self.menu_setting()

        # Buttons with paper/rock/scissors
        tk.Button(self.root, bd=0, image=self.images_dict["paper"]).grid(row=5, column=0, pady=0)
        tk.Button(self.root, bd=0, image=self.images_dict["rock"]).grid(row=5, column=1, pady=0)
        tk.Button(self.root, bd=0, image=self.images_dict["scissors"]).grid(row=5, column=2, pady=0)

        self.root.mainloop()

    def initialize_tk_window(self):
        """
        Setting the title and dimensions of the window
        """
        # tkinter window
        self.root.title("Paper rock scissors")

        # window middle of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        dx = 600
        dy = 400
        x0 = int((screen_width - dx) / 2)
        y0 = int((screen_height - dy) / 2)
        self.root.geometry(f"{dx}x{dy}+{x0}+{y0}")

    def menu_setting(self):
        """
        Setting the menu
        """
        self.menu.add_command(label="Change Name", command=self.menu_change_name)
        self.menu.add_command(label="Restart", command=self.menu_restart)
        self.menu.add_command(label="Quit", command=self.menu_quit)
        self.menu.add_command(label="Change max lifes", command=self.menu_change_max_lifes)
        self.root.config(menu=self.menu)

    def menu_get_name(self):
        """
        Function to change the name in a separate window - used in def menu_change_name
        """
        read_name = self.name_entry.get()
        self.name_label.config(text=f"{read_name}")
        self.name_window.destroy()

    def menu_change_name(self):
        """
        Method used in the menu - changing name of the player
        """
        self.name_window = tk.Tk()
        self.name_window.title("Change name")
        tk.Label(self.name_window, text="Give your name:").grid(row=0, column=0)
        tk.Button(self.name_window, text="Confirm", command=self.menu_get_name).grid(row=1, column=0)
        self.name_entry = tk.Entry(self.name_window)
        self.name_entry.grid(row=0, column=1)

    def menu_restart(self):
        """
        Method restarting all the values
        """
        self.lifes_player = RPSClass.max_lifes
        self.lifes_cpu = RPSClass.max_lifes
        self.last_won = None
        self.player_life_bar.config(value=self.lifes_player, max=RPSClass.max_lifes)
        self.cpu_life_bar.config(value=self.lifes_cpu, max=RPSClass.max_lifes)
        self.text_label.config(text="lets try again!", fg="black")
        self.player_choice_icon.config(image=self.images_dict["question"])
        self.cpu_choice_icon.config(image=self.images_dict["question"])

    def menu_quit(self):
        """
        Changes app
        """
        self.root.destroy()
        sys.exit()

    def menu_get_lifes(self):
        """
        Function to read the new number of lifes
        """
        lifes = self.lifes_entry.get()
        try:
            lifes = int(lifes)
            if lifes <= 0:
                tk.messagebox.showerror("The value has to be positive!\nnSetting lifes = 3")
                RPSClass.max_lifes = 3
            elif lifes > 100:
                tk.messagebox.showerror("Error", "You must be crazy.\nSetting lifes = 100")
                RPSClass.max_lifes = 100
            else:
                RPSClass.max_lifes = lifes
        except TypeError:
            tk.messagebox.showerror("Wrong type", "The value has to be integer!\nSetting lifes = 3")
            RPSClass.max_lifes = 3
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error!\n{e}\nSetting lifes = 3")
            RPSClass.max_lifes = 3
        self.menu_restart()
        print(RPSClass.max_lifes)
        self.lifes_window.destroy()

    def menu_change_max_lifes(self):
            """
            Method used in the menu - changing name of the player
            """
            self.lifes_window = tk.Tk()
            self.lifes_window.title("Give new number of lifes")
            tk.Label(self.lifes_window, text="Give max number of lifes:\n(game will restart)").grid(row=0, column=0)
            tk.Button(self.lifes_window, text="Confirm", command=self.menu_get_lifes).grid(row=1, column=0)
            self.lifes_entry = tk.Entry(self.lifes_window)
            self.lifes_entry.grid(row=0, column=1)

    def check_if_player_wins(self):
        """
        Checks if player wins, changes results and defines new text and color of the text
        """

        # Dict: val beats key
        what_beats = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        if self.cpu_choice == self.player_choice:
            self.text = "Great minds think alike!"
            self.color = "black"
            self.last_won = None

        elif self.cpu_choice == what_beats[self.player_choice]:
            self.lifes_player -= 1
            self.text = "Sorry, maybe next time..."
            self.color = "red"
            self.last_won = False
            self.player_life_bar.config(value=self.lifes_player)

        else:
            self.lifes_cpu -= 1
            self.text = "Wow! You won!"
            self.color = "green"
            self.last_won = True
            self.cpu_life_bar.config(value=self.lifes_cpu)

    def print_messagebox(self):
        end_text = "You won" if self.lifes_cpu == 0 else "You lost"
        answer = messagebox.askquestion(end_text, end_text+"\nDo you want to play again?")
        if answer == "yes":
            self.menu_restart()
        else:
            self.menu_quit()

    def make_cpu_choice(self):
        self.cpu_choice = random.choice(list(self.possible_options))

    def game(self, choice):
        self.player_choice = choice
        self.player_choice_icon.config(image=self.images_dict[self.player_choice])

        self.make_cpu_choice()
        self.cpu_choice_icon.config(image=self.images_dict[self.cpu_choice])

        self.check_if_player_wins()

        if self.lifes_cpu == 0 or self.lifes_player == 0:
            self.print_messagebox()

        self.text_label.config(text=self.text, fg=self.color)

    @staticmethod
    def make_image(fpath, dx, dy):
        """
        Changing sizes of the window
        :param fpath: path of the file
        :param dx: x-dimension to set
        :param dy: y-dimension to set
        """
        image = Image.open(fpath)
        resized = image.resize((dx, dy), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized)


game = RPSClass()
